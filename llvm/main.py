from naiveCLexer import naiveCLexer
from naiveCParser import naiveCParser
from stringVisitor import StringVisitor
from myVisitor import MyVisitor

from antlr4 import FileStream
from antlr4 import CommonTokenStream
from llvmlite import ir

if __name__ == '__main__':
    source = '../input/basic_io.c'
    input_stream = FileStream(source)
    lexer = naiveCLexer(input_stream)
    token = CommonTokenStream(lexer)
    parser = naiveCParser(token)
    tree = parser.prog()

    ST = {}
    module = ir.Module()
    stringVisitor = StringVisitor(ST, module)
    stringVisitor.visit(tree)
    visitor = MyVisitor(ST, module)
    visitor.visit(tree)

    print(visitor.module)
    visitor.write('../output/basic_io.ll')
