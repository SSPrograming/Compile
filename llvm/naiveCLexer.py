# Generated from E:/Tsinghua/课程/大三上/汇编与编译原理/作业/编译/编译小组作业/src/LLVM/antlr/src\naiveC.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\61")
        buf.write("\u0138\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4u\n\4\f")
        buf.write("\4\16\4x\13\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\20\3")
        buf.write("\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\31\3\32")
        buf.write("\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37")
        buf.write("\3\37\3\37\3 \3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3")
        buf.write("&\3&\3\'\3\'\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3*\3*\7")
        buf.write("*\u00f7\n*\f*\16*\u00fa\13*\3+\5+\u00fd\n+\3+\3+\7+\u0101")
        buf.write("\n+\f+\16+\u0104\13+\3+\5+\u0107\n+\3,\3,\7,\u010b\n,")
        buf.write("\f,\16,\u010e\13,\3-\6-\u0111\n-\r-\16-\u0112\3-\3-\3")
        buf.write(".\3.\3.\3.\7.\u011b\n.\f.\16.\u011e\13.\3.\3.\3.\3.\3")
        buf.write(".\3/\3/\3/\3/\7/\u0129\n/\f/\16/\u012c\13/\3/\3/\3\60")
        buf.write("\3\60\7\60\u0132\n\60\f\60\16\60\u0135\13\60\3\60\3\60")
        buf.write("\4\u011c\u0133\2\61\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n")
        buf.write("\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'")
        buf.write("\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ")
        buf.write("?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61\3\2\t\4\2\f\f")
        buf.write("\17\17\3\2\63;\3\2\62;\3\2//\5\2C\\aac|\6\2\62;C\\aac")
        buf.write("|\5\2\13\f\17\17\"\"\2\u0141\2\3\3\2\2\2\2\5\3\2\2\2\2")
        buf.write("\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3")
        buf.write("\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2")
        buf.write("\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2")
        buf.write("\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2")
        buf.write("\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y")
        buf.write("\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\3a\3\2\2\2\5")
        buf.write("h\3\2\2\2\7j\3\2\2\2\t{\3\2\2\2\13\177\3\2\2\2\r\u0084")
        buf.write("\3\2\2\2\17\u0089\3\2\2\2\21\u008f\3\2\2\2\23\u0098\3")
        buf.write("\2\2\2\25\u009b\3\2\2\2\27\u00a0\3\2\2\2\31\u00a7\3\2")
        buf.write("\2\2\33\u00ad\3\2\2\2\35\u00af\3\2\2\2\37\u00b2\3\2\2")
        buf.write("\2!\u00b5\3\2\2\2#\u00b7\3\2\2\2%\u00b9\3\2\2\2\'\u00bb")
        buf.write("\3\2\2\2)\u00bd\3\2\2\2+\u00bf\3\2\2\2-\u00c1\3\2\2\2")
        buf.write("/\u00c4\3\2\2\2\61\u00c7\3\2\2\2\63\u00ca\3\2\2\2\65\u00cd")
        buf.write("\3\2\2\2\67\u00cf\3\2\2\29\u00d1\3\2\2\2;\u00d3\3\2\2")
        buf.write("\2=\u00d5\3\2\2\2?\u00d8\3\2\2\2A\u00db\3\2\2\2C\u00dd")
        buf.write("\3\2\2\2E\u00df\3\2\2\2G\u00e1\3\2\2\2I\u00e3\3\2\2\2")
        buf.write("K\u00e5\3\2\2\2M\u00e7\3\2\2\2O\u00e9\3\2\2\2Q\u00ee\3")
        buf.write("\2\2\2S\u00f4\3\2\2\2U\u0106\3\2\2\2W\u0108\3\2\2\2Y\u0110")
        buf.write("\3\2\2\2[\u0116\3\2\2\2]\u0124\3\2\2\2_\u012f\3\2\2\2")
        buf.write("ab\7u\2\2bc\7k\2\2cd\7|\2\2de\7g\2\2ef\7q\2\2fg\7h\2\2")
        buf.write("g\4\3\2\2\2hi\7.\2\2i\6\3\2\2\2jk\7%\2\2kl\7k\2\2lm\7")
        buf.write("p\2\2mn\7e\2\2no\7n\2\2op\7w\2\2pq\7f\2\2qr\7g\2\2rv\3")
        buf.write("\2\2\2su\n\2\2\2ts\3\2\2\2ux\3\2\2\2vt\3\2\2\2vw\3\2\2")
        buf.write("\2wy\3\2\2\2xv\3\2\2\2yz\b\4\2\2z\b\3\2\2\2{|\7k\2\2|")
        buf.write("}\7p\2\2}~\7v\2\2~\n\3\2\2\2\177\u0080\7x\2\2\u0080\u0081")
        buf.write("\7q\2\2\u0081\u0082\7k\2\2\u0082\u0083\7f\2\2\u0083\f")
        buf.write("\3\2\2\2\u0084\u0085\7e\2\2\u0085\u0086\7j\2\2\u0086\u0087")
        buf.write("\7c\2\2\u0087\u0088\7t\2\2\u0088\16\3\2\2\2\u0089\u008a")
        buf.write("\7d\2\2\u008a\u008b\7t\2\2\u008b\u008c\7g\2\2\u008c\u008d")
        buf.write("\7c\2\2\u008d\u008e\7m\2\2\u008e\20\3\2\2\2\u008f\u0090")
        buf.write("\7e\2\2\u0090\u0091\7q\2\2\u0091\u0092\7p\2\2\u0092\u0093")
        buf.write("\7v\2\2\u0093\u0094\7k\2\2\u0094\u0095\7p\2\2\u0095\u0096")
        buf.write("\7w\2\2\u0096\u0097\7g\2\2\u0097\22\3\2\2\2\u0098\u0099")
        buf.write("\7k\2\2\u0099\u009a\7h\2\2\u009a\24\3\2\2\2\u009b\u009c")
        buf.write("\7g\2\2\u009c\u009d\7n\2\2\u009d\u009e\7u\2\2\u009e\u009f")
        buf.write("\7g\2\2\u009f\26\3\2\2\2\u00a0\u00a1\7t\2\2\u00a1\u00a2")
        buf.write("\7g\2\2\u00a2\u00a3\7v\2\2\u00a3\u00a4\7w\2\2\u00a4\u00a5")
        buf.write("\7t\2\2\u00a5\u00a6\7p\2\2\u00a6\30\3\2\2\2\u00a7\u00a8")
        buf.write("\7y\2\2\u00a8\u00a9\7j\2\2\u00a9\u00aa\7k\2\2\u00aa\u00ab")
        buf.write("\7n\2\2\u00ab\u00ac\7g\2\2\u00ac\32\3\2\2\2\u00ad\u00ae")
        buf.write("\7-\2\2\u00ae\34\3\2\2\2\u00af\u00b0\7-\2\2\u00b0\u00b1")
        buf.write("\7-\2\2\u00b1\36\3\2\2\2\u00b2\u00b3\7/\2\2\u00b3\u00b4")
        buf.write("\7/\2\2\u00b4 \3\2\2\2\u00b5\u00b6\7/\2\2\u00b6\"\3\2")
        buf.write("\2\2\u00b7\u00b8\7,\2\2\u00b8$\3\2\2\2\u00b9\u00ba\7\61")
        buf.write("\2\2\u00ba&\3\2\2\2\u00bb\u00bc\7\'\2\2\u00bc(\3\2\2\2")
        buf.write("\u00bd\u00be\7@\2\2\u00be*\3\2\2\2\u00bf\u00c0\7>\2\2")
        buf.write("\u00c0,\3\2\2\2\u00c1\u00c2\7@\2\2\u00c2\u00c3\7?\2\2")
        buf.write("\u00c3.\3\2\2\2\u00c4\u00c5\7>\2\2\u00c5\u00c6\7?\2\2")
        buf.write("\u00c6\60\3\2\2\2\u00c7\u00c8\7?\2\2\u00c8\u00c9\7?\2")
        buf.write("\2\u00c9\62\3\2\2\2\u00ca\u00cb\7#\2\2\u00cb\u00cc\7?")
        buf.write("\2\2\u00cc\64\3\2\2\2\u00cd\u00ce\7#\2\2\u00ce\66\3\2")
        buf.write("\2\2\u00cf\u00d0\7?\2\2\u00d08\3\2\2\2\u00d1\u00d2\7(")
        buf.write("\2\2\u00d2:\3\2\2\2\u00d3\u00d4\7~\2\2\u00d4<\3\2\2\2")
        buf.write("\u00d5\u00d6\7(\2\2\u00d6\u00d7\7(\2\2\u00d7>\3\2\2\2")
        buf.write("\u00d8\u00d9\7~\2\2\u00d9\u00da\7~\2\2\u00da@\3\2\2\2")
        buf.write("\u00db\u00dc\7=\2\2\u00dcB\3\2\2\2\u00dd\u00de\7*\2\2")
        buf.write("\u00deD\3\2\2\2\u00df\u00e0\7+\2\2\u00e0F\3\2\2\2\u00e1")
        buf.write("\u00e2\7]\2\2\u00e2H\3\2\2\2\u00e3\u00e4\7_\2\2\u00e4")
        buf.write("J\3\2\2\2\u00e5\u00e6\7}\2\2\u00e6L\3\2\2\2\u00e7\u00e8")
        buf.write("\7\177\2\2\u00e8N\3\2\2\2\u00e9\u00ea\7v\2\2\u00ea\u00eb")
        buf.write("\7t\2\2\u00eb\u00ec\7w\2\2\u00ec\u00ed\7g\2\2\u00edP\3")
        buf.write("\2\2\2\u00ee\u00ef\7h\2\2\u00ef\u00f0\7c\2\2\u00f0\u00f1")
        buf.write("\7n\2\2\u00f1\u00f2\7u\2\2\u00f2\u00f3\7g\2\2\u00f3R\3")
        buf.write("\2\2\2\u00f4\u00f8\t\3\2\2\u00f5\u00f7\t\4\2\2\u00f6\u00f5")
        buf.write("\3\2\2\2\u00f7\u00fa\3\2\2\2\u00f8\u00f6\3\2\2\2\u00f8")
        buf.write("\u00f9\3\2\2\2\u00f9T\3\2\2\2\u00fa\u00f8\3\2\2\2\u00fb")
        buf.write("\u00fd\t\5\2\2\u00fc\u00fb\3\2\2\2\u00fc\u00fd\3\2\2\2")
        buf.write("\u00fd\u00fe\3\2\2\2\u00fe\u0102\t\3\2\2\u00ff\u0101\t")
        buf.write("\4\2\2\u0100\u00ff\3\2\2\2\u0101\u0104\3\2\2\2\u0102\u0100")
        buf.write("\3\2\2\2\u0102\u0103\3\2\2\2\u0103\u0107\3\2\2\2\u0104")
        buf.write("\u0102\3\2\2\2\u0105\u0107\7\62\2\2\u0106\u00fc\3\2\2")
        buf.write("\2\u0106\u0105\3\2\2\2\u0107V\3\2\2\2\u0108\u010c\t\6")
        buf.write("\2\2\u0109\u010b\t\7\2\2\u010a\u0109\3\2\2\2\u010b\u010e")
        buf.write("\3\2\2\2\u010c\u010a\3\2\2\2\u010c\u010d\3\2\2\2\u010d")
        buf.write("X\3\2\2\2\u010e\u010c\3\2\2\2\u010f\u0111\t\b\2\2\u0110")
        buf.write("\u010f\3\2\2\2\u0111\u0112\3\2\2\2\u0112\u0110\3\2\2\2")
        buf.write("\u0112\u0113\3\2\2\2\u0113\u0114\3\2\2\2\u0114\u0115\b")
        buf.write("-\2\2\u0115Z\3\2\2\2\u0116\u0117\7\61\2\2\u0117\u0118")
        buf.write("\7,\2\2\u0118\u011c\3\2\2\2\u0119\u011b\13\2\2\2\u011a")
        buf.write("\u0119\3\2\2\2\u011b\u011e\3\2\2\2\u011c\u011d\3\2\2\2")
        buf.write("\u011c\u011a\3\2\2\2\u011d\u011f\3\2\2\2\u011e\u011c\3")
        buf.write("\2\2\2\u011f\u0120\7,\2\2\u0120\u0121\7\61\2\2\u0121\u0122")
        buf.write("\3\2\2\2\u0122\u0123\b.\2\2\u0123\\\3\2\2\2\u0124\u0125")
        buf.write("\7\61\2\2\u0125\u0126\7\61\2\2\u0126\u012a\3\2\2\2\u0127")
        buf.write("\u0129\n\2\2\2\u0128\u0127\3\2\2\2\u0129\u012c\3\2\2\2")
        buf.write("\u012a\u0128\3\2\2\2\u012a\u012b\3\2\2\2\u012b\u012d\3")
        buf.write("\2\2\2\u012c\u012a\3\2\2\2\u012d\u012e\b/\2\2\u012e^\3")
        buf.write("\2\2\2\u012f\u0133\7$\2\2\u0130\u0132\13\2\2\2\u0131\u0130")
        buf.write("\3\2\2\2\u0132\u0135\3\2\2\2\u0133\u0134\3\2\2\2\u0133")
        buf.write("\u0131\3\2\2\2\u0134\u0136\3\2\2\2\u0135\u0133\3\2\2\2")
        buf.write("\u0136\u0137\7$\2\2\u0137`\3\2\2\2\r\2v\u00f8\u00fc\u0102")
        buf.write("\u0106\u010c\u0112\u011c\u012a\u0133\3\b\2\2")
        return buf.getvalue()


class naiveCLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    Include = 3
    TypeInt = 4
    TypeVoid = 5
    TypeChar = 6
    Break = 7
    Continue = 8
    If = 9
    Else = 10
    Return = 11
    While = 12
    ADD = 13
    ADDADD = 14
    SUBSUB = 15
    SUB = 16
    MUL = 17
    DIV = 18
    MOD = 19
    Greater = 20
    Less = 21
    GreaterEqual = 22
    LessEqual = 23
    Equal = 24
    NotEqual = 25
    Not = 26
    AssignOperator = 27
    ArithmeticAnd = 28
    ArithmeticOR = 29
    LogicAnd = 30
    LogicOR = 31
    Semicolon = 32
    LeftParentheses = 33
    RightParentheses = 34
    LeftBracket = 35
    RightBracket = 36
    LeftBrace = 37
    RightBrace = 38
    TRUE = 39
    FALSE = 40
    PositiveINT = 41
    INT = 42
    ID = 43
    WS = 44
    BlockComment = 45
    LineComment = 46
    String = 47

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'sizeof'", "','", "'int'", "'void'", "'char'", "'break'", "'continue'", 
            "'if'", "'else'", "'return'", "'while'", "'+'", "'++'", "'--'", 
            "'-'", "'*'", "'/'", "'%'", "'>'", "'<'", "'>='", "'<='", "'=='", 
            "'!='", "'!'", "'='", "'&'", "'|'", "'&&'", "'||'", "';'", "'('", 
            "')'", "'['", "']'", "'{'", "'}'", "'true'", "'false'" ]

    symbolicNames = [ "<INVALID>",
            "Include", "TypeInt", "TypeVoid", "TypeChar", "Break", "Continue", 
            "If", "Else", "Return", "While", "ADD", "ADDADD", "SUBSUB", 
            "SUB", "MUL", "DIV", "MOD", "Greater", "Less", "GreaterEqual", 
            "LessEqual", "Equal", "NotEqual", "Not", "AssignOperator", "ArithmeticAnd", 
            "ArithmeticOR", "LogicAnd", "LogicOR", "Semicolon", "LeftParentheses", 
            "RightParentheses", "LeftBracket", "RightBracket", "LeftBrace", 
            "RightBrace", "TRUE", "FALSE", "PositiveINT", "INT", "ID", "WS", 
            "BlockComment", "LineComment", "String" ]

    ruleNames = [ "T__0", "T__1", "Include", "TypeInt", "TypeVoid", "TypeChar", 
                  "Break", "Continue", "If", "Else", "Return", "While", 
                  "ADD", "ADDADD", "SUBSUB", "SUB", "MUL", "DIV", "MOD", 
                  "Greater", "Less", "GreaterEqual", "LessEqual", "Equal", 
                  "NotEqual", "Not", "AssignOperator", "ArithmeticAnd", 
                  "ArithmeticOR", "LogicAnd", "LogicOR", "Semicolon", "LeftParentheses", 
                  "RightParentheses", "LeftBracket", "RightBracket", "LeftBrace", 
                  "RightBrace", "TRUE", "FALSE", "PositiveINT", "INT", "ID", 
                  "WS", "BlockComment", "LineComment", "String" ]

    grammarFileName = "naiveC.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


