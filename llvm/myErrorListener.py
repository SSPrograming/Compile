from antlr4.error.ErrorListener import ErrorListener


class MyErrorListener(ErrorListener):

    def __init__(self):
        super(MyErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxError("Syntax Error")
