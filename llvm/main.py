from naiveCLexer import naiveCLexer
from naiveCParser import naiveCParser
from myVisitor import MyVisitor

from antlr4 import FileStream
from antlr4 import CommonTokenStream

if __name__ == '__main__':
    source = '../input/main.c'
    input_stream = FileStream(source)
    lexer = naiveCLexer(input_stream)
    token = CommonTokenStream(lexer)
    parser = naiveCParser(token)
    tree = parser.prog()
    visitor = MyVisitor()
    visitor.visit(tree)

    print(visitor.module)
    visitor.write('../output/main.ll')
