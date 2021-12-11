import sys

from naiveCLexer import naiveCLexer
from naiveCParser import naiveCParser
from myVisitor import MyVisitor

from antlr4 import FileStream
from antlr4 import CommonTokenStream

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Can\'t get filename, use default = \'main\' ')
        filename = 'main'
    else:
        filename = sys.argv[1]
    source = '../input/' + filename + '.c'
    input_stream = FileStream(source, encoding='utf-8')
    lexer = naiveCLexer(input_stream)
    token = CommonTokenStream(lexer)
    parser = naiveCParser(token)
    tree = parser.prog()

    visitor = MyVisitor()
    visitor.visit(tree)

    print(visitor.module)

    target = '../output/' + filename + '.ll'
    visitor.write(target)
