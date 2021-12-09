from naiveCParser import naiveCParser
from naiveCVisitor import naiveCVisitor

from utils.llvm_output import *
from utils.llvm_construct import *
from utils.string import *
from utils.SymbolTable import *


class MyVisitor(naiveCVisitor):
    def __init__(self):
        self.ST = SymbolTable()
        self.module = ir.Module()
        self.builder = ir.IRBuilder()
        # Printf Function
        printf_ty = ir.FunctionType(int32, [ir.PointerType(char)], var_arg=True)
        ir.Function(self.module, printf_ty, name='printf')
        # Scanf Function
        scanf_ty = ir.FunctionType(int32, [ir.PointerType(char)], var_arg=True)
        ir.Function(self.module, scanf_ty, name='scanf')

    def write(self, filename: str) -> None:
        write_ir(filename, str(self.module))

    def visitTypeInt(self, ctx: naiveCParser.TypeIntContext) -> str:
        return ctx.TypeInt().getSymbol().text

    def visitTypeChar(self, ctx: naiveCParser.TypeCharContext) -> str:
        return ctx.TypeChar().getSymbol().text

    def visitTypeVoid(self, ctx: naiveCParser.TypeVoidContext) -> str:
        return ctx.TypeVoid().getSymbol().text

    def visitTypeIdentifierPointer(self, ctx: naiveCParser.TypeIdentifierPointerContext) -> str:
        typeIdentifier = self.visit(ctx.typeIdentifier())
        return typeIdentifier + '*'

    def visitDefinition(self, ctx: naiveCParser.DefinitionContext) -> None:
        if ctx.typeIdentifier():
            typeIdentifier = self.visit(ctx.typeIdentifier())
        elif ctx.typeIdentifierPointer():
            typeIdentifier = self.visit(ctx.typeIdentifierPointer())
        else:
            raise 'panic: visitDefinition'
        pointer_count = typeIdentifier.count('*')
        ir_type = str2irType[typeIdentifier.replace('*', '')]
        for i in range(pointer_count):
            ir_type = ir.PointerType(ir_type)
        identity = ctx.ID().getSymbol().text
        l_value = self.builder.alloca(ir_type, name=identity)
        self.ST.insert(identity, l_value)
        # 如果有初值
        if ctx.AssignOperator():
            r_value = self.visit(ctx.expr())
            self.builder.store(r_value, l_value)

    def visitAssignment(self, ctx: naiveCParser.AssignmentContext):
        identity = ctx.ID().getSymbol().text
        l_value = self.ST.get(identity)
        if not l_value:
            raise 'panic: visitAssignment'
        if ctx.index:
            pass
        r_value = self.visit(ctx.value)
        self.builder.store(r_value, l_value)

    def visitMulDiv(self, ctx: naiveCParser.MulDivContext) -> ir.Value:
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if left.type != right.type:
            raise 'panic: visitAddSub'
        if ctx.op.type == naiveCParser.MUL:
            return self.builder.mul(left, right)
        else:
            return self.builder.sdiv(left, right)

    def visitAddSub(self, ctx: naiveCParser.AddSubContext) -> ir.Value:
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if left.type != right.type:
            raise 'panic: visitAddSub'
        if ctx.op.type == naiveCParser.ADD:
            return self.builder.add(left, right)
        else:
            return self.builder.sub(left, right)

    def visitGetP(self, ctx: naiveCParser.GetPContext) -> ir.Value:
        identity = ctx.ID().getSymbol().text
        symbol = self.ST.get(identity)
        if symbol:
            return symbol
        else:
            print('未定义的标识符: ' + identity)
            raise 'panic: visitGetP'

    def visitInt(self, ctx: naiveCParser.IntContext) -> ir.Constant:
        return ir.Constant(int32, int(ctx.INT().getSymbol().text))

    def visitId(self, ctx: naiveCParser.IdContext) -> ir.Value:
        identity = ctx.ID().getSymbol().text
        symbol = self.ST.get(identity)
        if symbol:
            return self.builder.load(symbol)
        else:
            print('未定义的标识符: ' + identity)
            raise 'panic: visitId'

    def visitParens(self, ctx: naiveCParser.ParensContext) -> ir.Value:
        return self.visit(ctx.expr())

    def visitReturnLine(self, ctx: naiveCParser.ReturnLineContext):
        value = self.visit(ctx.expr())
        self.builder.ret(value)
        self.ST = self.ST.prev()

    def visitFunctionDefine(self, ctx: naiveCParser.FunctionDefineContext):
        typeIdentifier = str2irType[self.visit(ctx.typeIdentifier())]
        identity = ctx.ID().getSymbol().text
        paramList = []
        paramList = [str2irType[item] for item in paramList]
        func_ty = ir.FunctionType(typeIdentifier, paramList)
        # TODO: 函数重定义
        func = ir.Function(self.module, func_ty, name=identity)
        block = func.append_basic_block(name='entry')
        self.ST = SymbolTable(self.ST)
        self.builder.position_at_end(block)
        self.visit(ctx.returnStatemts())

    def visitParamExpr(self, ctx: naiveCParser.ParamExprContext) -> ir.Value:
        return self.visit(ctx.expr())

    def visitParamFunc(self, ctx: naiveCParser.ParamFuncContext) -> ir.Value:
        return self.visit(ctx.functionCall())

    def visitParamString(self, ctx: naiveCParser.ParamStringContext) -> ir.Value:
        string = ctx.String().getSymbol().text
        g_string = add_global_string_constant(self.module, convert(string))
        return self.builder.bitcast(self.builder.gep(g_string, [ir.Constant(int32, 0)], inbounds=True),
                                    ir.PointerType(char))

    def visitParamList(self, ctx: naiveCParser.ParamListContext) -> []:
        if not ctx.param():
            return []
        param = self.visit(ctx.param())
        if ctx.paramList():
            paramList = self.visit(ctx.paramList())
            paramList.append(param)
            return paramList
        else:
            return [param]

    def visitFunctionCall(self, ctx: naiveCParser.FunctionCallContext):
        identity = ctx.ID().getSymbol().text
        func = self.module.get_global(identity)
        paramsList = self.visit(ctx.paramList())
        self.builder.call(func, paramsList)
