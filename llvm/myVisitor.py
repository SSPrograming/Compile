from naiveCParser import naiveCParser
from naiveCVisitor import naiveCVisitor

from utils.llvm_output import *
from utils.llvm_construct import *
from utils.string import *


class MyVisitor(naiveCVisitor):
    def __init__(self):
        self.ST = {}
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
        ir_type = str2type[typeIdentifier.replace('*', '')]
        for i in range(pointer_count):
            ir_type = ir.PointerType(ir_type)
        identity = ctx.ID().getSymbol().text
        self.ST[identity] = self.builder.alloca(ir_type, name=identity)

    def visitMulDiv(self, ctx: naiveCParser.MulDivContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == naiveCParser.MUL:
            return left * right
        else:
            return left / right

    def visitAddSub(self, ctx: naiveCParser.AddSubContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == naiveCParser.ADD:
            return left + right
        else:
            return left - right

    def visitGetP(self, ctx: naiveCParser.GetPContext):
        identity = ctx.ID().getSymbol().text
        if identity in self.ST:
            return self.ST[identity]
        else:
            print('未定义的标识符: ' + identity)

    def visitInt(self, ctx: naiveCParser.IntContext) -> ir.Constant:
        return ir.Constant(int32, int(ctx.INT().getSymbol().text))

    def visitId(self, ctx: naiveCParser.IdContext) -> ir.Value:
        identity = ctx.ID().getSymbol().text
        if identity in self.ST:
            return self.builder.load(self.ST[identity])
        else:
            print('未定义的标识符: ' + identity)

    def visitParens(self, ctx: naiveCParser.ParensContext) -> ir.Value:
        return self.visit(ctx.expr())

    def visitReturnLine(self, ctx: naiveCParser.ReturnLineContext):
        value = self.visit(ctx.expr())
        self.builder.ret(value)

    def visitFunctionDefine(self, ctx: naiveCParser.FunctionDefineContext):
        typeIdentifier = str2type[self.visit(ctx.typeIdentifier())]
        identity = ctx.ID().getSymbol().text
        paramList = []
        paramList = [str2type[item] for item in paramList]
        func_ty = ir.FunctionType(typeIdentifier, paramList)
        # TODO: 函数重定义
        func = ir.Function(self.module, func_ty, name=identity)
        block = func.append_basic_block(name='entry')
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
