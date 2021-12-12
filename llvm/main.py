import sys

from naiveCLexer import naiveCLexer
from naiveCParser import naiveCParser
from myVisitor import MyVisitor
from myErrorListener import MyErrorListener

from antlr4 import FileStream
from antlr4 import CommonTokenStream

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Can\'t get filename, use default = \'main\' ')
        input_filename = '../input/main.c'
        output_filename = '../output/main.ll'
    else:
        input_filename = sys.argv[1]
        output_filename = sys.argv[2]

    input_stream = FileStream(input_filename, encoding='utf-8')
    lexer = naiveCLexer(input_stream)
    token = CommonTokenStream(lexer)
    parser = naiveCParser(token)
    myErrorListener = MyErrorListener()
    parser.addErrorListener(myErrorListener)
    # 语法解析
    try:
        tree = parser.prog()
    except SyntaxError as e:
        print(e)
    else:
        visitor = MyVisitor()
        # 语义解析 + 中间代码生成
        try:
            visitor.visit(tree)
        except Exception as e:
            print(e)
            print('Semantic Error')
        else:
            visitor.write(output_filename)
            print('generate successfully：' + input_filename + ' -> ' + output_filename)
