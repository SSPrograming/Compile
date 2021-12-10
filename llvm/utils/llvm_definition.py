from llvmlite import ir

void = ir.VoidType()
boolean = ir.IntType(1)
char = ir.IntType(8)
int32 = ir.IntType(32)
int64 = ir.IntType(64)

str2irType = {
    'void': void,
    'boolean': boolean,
    'char': char,
    'int': int32,
    'long long': int64
}
