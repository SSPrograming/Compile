from utils.llvm_definition import *


def add_global_string_constant(module: ir.Module, string: str) -> ir.GlobalVariable:
    byte_string = bytearray(string.encode())
    ir_string = ir.Constant(ir.ArrayType(char, len(byte_string)), byte_string)
    g_string = ir.GlobalVariable(module, ir_string.type, module.get_unique_name('str'))
    g_string.global_constant = True
    g_string.initializer = ir_string
    return g_string
