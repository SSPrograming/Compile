from naiveCParser import naiveCParser
from naiveCVisitor import naiveCVisitor

from utils.llvm_output import *
from utils.llvm_construct import *


class MyVisitor(naiveCVisitor):
    def __init__(self):
        self.ST = {}
        self.module = ir.Module()
        # Printf Function
        printf_ty = ir.FunctionType(int32, [ir.PointerType(char)], var_arg=True)
        ir.Function(self.module, printf_ty, name='printf')
        # Scanf Function
        scanf_ty = ir.FunctionType(int32, [ir.PointerType(char)], var_arg=True)
        ir.Function(self.module, scanf_ty, name='scanf')

    def write(self, filename):
        write_ir(filename, str(self.module))
