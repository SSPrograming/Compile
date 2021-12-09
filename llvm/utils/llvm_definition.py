from llvmlite import ir

void = ir.VoidType()
boolean = ir.IntType(1)
char = ir.IntType(8)
int32 = ir.IntType(32)

str2irType = {
    'void': void,
    'boolean': boolean,
    'int': int32,
    'char': char
}
