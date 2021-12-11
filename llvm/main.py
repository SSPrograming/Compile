import sys

from naiveCLexer import naiveCLexer
from naiveCParser import naiveCParser
from myVisitor import MyVisitor
from myErrorListener import MyErrorListener

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
            target = '../output/' + filename + '.ll'
            visitor.write(target)
            print('生成成功：' + source + ' -> ' + target)
