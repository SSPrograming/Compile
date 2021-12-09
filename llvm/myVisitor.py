from naiveCParser import naiveCParser
from naiveCVisitor import naiveCVisitor

from utils.llvm_output import *
from utils.llvm_construct import *


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

    def write(self, filename) -> None:
        write_ir(filename, str(self.module))

    def visitTypeInt(self, ctx: naiveCParser.TypeIntContext):
        return ctx.TypeInt().getSymbol().text

    def visitTypeChar(self, ctx: naiveCParser.TypeCharContext):
        return ctx.TypeChar().getSymbol().text

    def visitTypeVoid(self, ctx: naiveCParser.TypeVoidContext):
        return ctx.TypeVoid().getSymbol().text

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

    def visitInt(self, ctx: naiveCParser.IntContext) -> ir.Constant:
        return ir.Constant(int32, int(ctx.INT().getSymbol().text))

    def visitId(self, ctx: naiveCParser.IdContext):
        identity = ctx.ID().getSymbol().text
        if identity in self.ST:
            return self.ST[identity]
        else:
            print('未定义的标识符: ' + identity)

    def visitParens(self, ctx: naiveCParser.ParensContext):
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
        self.visit(ctx.statements())
        self.visit(ctx.returnLine())
