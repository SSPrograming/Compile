from llvmlite import ir

void = ir.VoidType()
char = ir.IntType(8)
int32 = ir.IntType(32)
double = ir.DoubleType()

str2irType = {
    'void': void,
    'int': int32,
    'char': char,
    'double': double
}
