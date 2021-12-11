from utils.llvm_definition import *


def add_global_string_constant(module: ir.Module, string: str) -> ir.GlobalVariable:
    byte_string = bytearray(string.encode())
    ir_string = ir.Constant(ir.ArrayType(char, len(byte_string)), byte_string)
    g_string = ir.GlobalVariable(module, ir_string.type, module.get_unique_name('str'))
    g_string.global_constant = True
    g_string.initializer = ir_string
    return g_string


def init_io(module: ir.Module) -> None:
    # Printf Function
    printf_ty = ir.FunctionType(int32, [ir.PointerType(char)], var_arg=True)
    ir.Function(module, printf_ty, name='printf')
    # Scanf Function
    scanf_ty = ir.FunctionType(int32, [ir.PointerType(char)], var_arg=True)
    ir.Function(module, scanf_ty, name='scanf')


def init_memory(module: ir.Module) -> None:
    # Malloc Function
    malloc_ty = ir.FunctionType(ir.PointerType(char), [int32])
    ir.Function(module, malloc_ty, name='malloc')
    # Free Function
    free_ty = ir.FunctionType(void, [ir.PointerType(char)])
    ir.Function(module, free_ty, name='free')


def init_system(module: ir.Module) -> None:
    # Exit Function
    exit_ty = ir.FunctionType(void, [int32])
    ir.Function(module, exit_ty, name='exit')
    # IsDigit Function
    isdigit_ty = ir.FunctionType(int32, [int32])
    ir.Function(module, isdigit_ty, name='isdigit')
