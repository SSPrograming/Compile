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
        init_io(self.module)
        init_memory(self.module)

    def _getIdentifier(self, ctx, real=True):
        if ctx.realTypeID():
            typeIdentifier = self.visit(ctx.realTypeID())
        elif ctx.realTypeIDPointer():
            typeIdentifier = self.visit(ctx.realTypeIDPointer())
        else:
            raise Exception('panic: visitDefinition')
        pointer_count = typeIdentifier.count('*')
        ir_type = str2irType[typeIdentifier.replace('*', '')]
        for i in range(pointer_count):
            ir_type = ir.PointerType(ir_type)
        return ir_type

    def write(self, filename: str) -> None:
        write_ir(filename, str(self.module))

    def visitRealTypeInt(self, ctx: naiveCParser.RealTypeIntContext) -> str:
        return ctx.TypeInt().getSymbol().text

    def visitRealTypeChar(self, ctx: naiveCParser.RealTypeCharContext) -> str:
        return ctx.TypeChar().getSymbol().text

    def visitRealTypeIDPointer(self, ctx: naiveCParser.RealTypeIDPointerContext) -> str:
        realTypeIdentifier = self.visit(ctx.realTypeID())
        return realTypeIdentifier + '*'

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
        ir_type = self._getIdentifier(ctx, real=True)
        identity = ctx.ID().getSymbol().text
        if ctx.LeftBracket() and ctx.RightBracket():
            size = int(ctx.PositiveINT().getSymbol().text)
            l_value = self.builder.alloca(ir.ArrayType(ir_type, size), name=identity)
        else:
            l_value = self.builder.alloca(ir_type, name=identity)
        self.ST.insert(identity, l_value)
        # 如果有初值
        if ctx.AssignOperator():
            r_value = self.visit(ctx.expr())
            self.builder.store(r_value, l_value)

    def visitCommonAssign(self, ctx: naiveCParser.CommonAssignContext):
        identity = ctx.ID().getSymbol().text
        l_value = self.ST.get(identity)
        if not l_value:
            print('未定义的标识符: ' + identity)
            raise Exception('panic: visitAssignment')
        r_value = self.visit(ctx.expr())
        self.builder.store(r_value, l_value)

    def visitTypeCast(self, ctx: naiveCParser.TypeCastContext):
        ir_type = self._getIdentifier(ctx, real=True)
        l_value = self.visit(ctx.expr())
        return self.builder.bitcast(l_value, ir_type)

    def visitArrayAssign(self, ctx: naiveCParser.ArrayAssignContext):
        identity = ctx.ID().getSymbol().text
        symbol = self.ST.get(identity)
        if not symbol:
            print('未定义的标识符: ' + identity)
            raise Exception('panic: visitAssignment')
        index = self.visit(ctx.expr(0))
        if isinstance(symbol.type.pointee, ir.ArrayType):
            # 数组
            l_value = self.builder.gep(symbol, [ir.Constant(int32, 0), index])
        else:
            # 指针
            symbol = self.builder.load(symbol)
            l_value = self.builder.gep(symbol, [index])
        r_value = self.visit(ctx.expr(1))
        self.builder.store(r_value, l_value)

    def visitMulDiv(self, ctx: naiveCParser.MulDivContext) -> ir.Value:
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if left.type != right.type:
            print('类型不匹配')
            raise Exception('panic: visitMulDiv')
        if ctx.op.type == naiveCParser.MUL:
            return self.builder.mul(left, right)
        else:
            return self.builder.sdiv(left, right)

    def visitAddSub(self, ctx: naiveCParser.AddSubContext) -> ir.Value:
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if left.type != right.type:
            print('类型不匹配')
            raise Exception('panic: visitAddSub')
        if ctx.op.type == naiveCParser.ADD:
            return self.builder.add(left, right)
        else:
            return self.builder.sub(left, right)

    def visitNegative(self, ctx: naiveCParser.NegativeContext) -> ir.Value:
        value = self.visit(ctx.expr())
        return self.builder.neg(value)

    def visitGetP(self, ctx: naiveCParser.GetPContext) -> ir.Value:
        identity = ctx.ID().getSymbol().text
        symbol = self.ST.get(identity)
        if symbol:
            return symbol
        else:
            print('未定义的标识符: ' + identity)
            raise Exception('panic: visitGetP')

    def visitPositiveINT(self, ctx: naiveCParser.PositiveINTContext):
        return ir.Constant(int32, int(ctx.PositiveINT().getSymbol().text))

    def visitInt(self, ctx: naiveCParser.IntContext) -> ir.Constant:
        return ir.Constant(int32, int(ctx.INT().getSymbol().text))

    def visitId(self, ctx: naiveCParser.IdContext) -> ir.Value:
        identity = ctx.ID().getSymbol().text
        symbol = self.ST.get(identity)
        if symbol:
            return self.builder.load(symbol)
        else:
            print('未定义的标识符: ' + identity)
            raise Exception('panic: visitId')

    def visitBoolExpr(self, ctx: naiveCParser.BoolExprContext) -> ir.Constant:
        if ctx.TRUE():
            return ir.Constant(boolean, True)
        elif ctx.FALSE():
            return ir.Constant(boolean, False)
        raise Exception('panic: visitBoolExpr')

    def visitArrayVisit(self, ctx: naiveCParser.ArrayVisitContext):
        identity = ctx.ID().getSymbol().text
        symbol = self.ST.get(identity)
        if symbol:
            index = self.visit(ctx.expr())
            if isinstance(symbol.type.pointee, ir.ArrayType):
                # 数组
                l_value = self.builder.gep(symbol, [ir.Constant(int32, 0), index])
            else:
                # 指针
                symbol = self.builder.load(symbol)
                l_value = self.builder.gep(symbol, [index])
            return self.builder.load(l_value)
        else:
            print('未定义的标识符: ' + identity)
            raise Exception('panic: visitId')

    def visitParens(self, ctx: naiveCParser.ParensContext) -> ir.Value:
        return self.visit(ctx.expr())

    def visitConditionOperator(self, ctx: naiveCParser.ConditionOperatorContext) -> str:
        return ctx.getChild(0).getSymbol().text

    def visitAnd(self, ctx: naiveCParser.AndContext) -> boolean:
        value0 = self.visit(ctx.conditionExpr(0))
        value1 = self.visit(ctx.conditionExpr(1))
        return self.builder.and_(value0, value1)

    def visitOr(self, ctx: naiveCParser.OrContext) -> boolean:
        value0 = self.visit(ctx.conditionExpr(0))
        value1 = self.visit(ctx.conditionExpr(1))
        return self.builder.or_(value0, value1)

    def visitCondParen(self, ctx: naiveCParser.CondParenContext) -> boolean:
        return self.visit(ctx.conditionExpr())

    def visitCondOp(self, ctx: naiveCParser.CondOpContext) -> boolean:
        value0 = self.visit(ctx.expr(0))
        value1 = self.visit(ctx.expr(1))
        return self.builder.icmp_signed(self.visit(ctx.conditionOperator()), value0, value1)

    def visitCondExp(self, ctx: naiveCParser.CondExpContext) -> boolean:
        value = self.visit(ctx.expr())
        return self.builder.icmp_signed('!=', value, ir.Constant(value.type, 0))

    def visitReturnLine(self, ctx: naiveCParser.ReturnLineContext) -> None:
        value = self.visit(ctx.expr())
        self.builder.ret(value)
        self.ST = self.ST.prev()

    def visitFunctionDefine(self, ctx: naiveCParser.FunctionDefineContext) -> None:
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
        self.visit(ctx.block())

    def visitParamExpr(self, ctx: naiveCParser.ParamExprContext) -> ir.Value:
        return self.visit(ctx.expr())

    def visitParamFunc(self, ctx: naiveCParser.ParamFuncContext) -> ir.Value:
        return self.visit(ctx.functionCall())

    def visitParamString(self, ctx: naiveCParser.ParamStringContext) -> ir.Value:
        string = ctx.String().getSymbol().text
        g_string = add_global_string_constant(self.module, convert(string))
        return self.builder.gep(g_string, [ir.Constant(int32, 0), ir.Constant(int32, 0)], inbounds=True)

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

    def visitFunctionCall(self, ctx: naiveCParser.FunctionCallContext) -> ir.Value:
        identity = ctx.ID().getSymbol().text
        func = self.module.get_global(identity)
        paramsList = self.visit(ctx.paramList())
        return self.builder.call(func, paramsList)

    def visitBlock(self, ctx: naiveCParser.BlockContext) -> None:
        self.ST = SymbolTable(self.ST)
        self.visit(ctx.statements())
        self.ST = self.ST.prev()

    def _visitIfBlock(self, ctx: naiveCParser.IfBlockContext, i) -> None:
        if i == len(ctx.conditionExpr()):
            if ctx.block(i):
                self.visit(ctx.block(i))
            return
        cond = self.visit(ctx.conditionExpr(i))
        with self.builder.if_else(cond) as (then, otherwise):
            with then:
                self.visit(ctx.block(i))
            with otherwise:
                self._visitIfBlock(ctx, i + 1)

    def visitIfBlock(self, ctx: naiveCParser.IfBlockContext) -> None:
        self._visitIfBlock(ctx, 0)

    def visitWhileBlock(self, ctx: naiveCParser.WhileBlockContext) -> None:
        cond = self.visit(ctx.conditionExpr())
        while_begin = self.builder.append_basic_block(name='while_begin')
        while_end = self.builder.append_basic_block(name='while_end')
        self.builder.cbranch(self.builder.not_(cond), while_end, while_begin)
        self.builder.position_at_end(while_begin)
        self.visit(ctx.block())
        cond = self.visit(ctx.conditionExpr())
        self.builder.cbranch(cond, while_begin, while_end)
        self.builder.position_at_end(while_end)
