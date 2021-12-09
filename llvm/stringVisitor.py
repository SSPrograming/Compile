from naiveCParser import naiveCParser
from naiveCVisitor import naiveCVisitor

from utils.llvm_construct import *


class StringVisitor(naiveCVisitor):
    def __init__(self, ST, module):
        self.ST = ST
        self.module = module

    def visitParamString(self, ctx: naiveCParser.ParamStringContext) -> None:
        string = ctx.String().getSymbol().text
        self.ST[string] = add_global_string_constant(self.module, string.replace('"', '') + '\0')
