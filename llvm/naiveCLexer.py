# Generated from E:/Tsinghua/课程/大三上/汇编与编译原理/作业/编译/编译小组作业/src/Compile/antlr/src\naiveC.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\64")
        buf.write("\u0157\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3t\n\3")
        buf.write("\f\3\16\3w\13\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3")
        buf.write("\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\20\3\20\3")
        buf.write("\20\3\21\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25")
        buf.write("\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\35\3\35\3\36")
        buf.write("\3\36\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3#\3#\3$\3$")
        buf.write("\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3)\3)\3)\3*\3*\3*\3*")
        buf.write("\3*\3*\3+\3+\3+\3+\3+\3+\3+\3,\3,\7,\u010e\n,\f,\16,\u0111")
        buf.write("\13,\3-\3-\3-\3-\5-\u0117\n-\3-\3-\3.\5.\u011c\n.\3.\3")
        buf.write(".\7.\u0120\n.\f.\16.\u0123\13.\3.\5.\u0126\n.\3/\3/\7")
        buf.write("/\u012a\n/\f/\16/\u012d\13/\3\60\6\60\u0130\n\60\r\60")
        buf.write("\16\60\u0131\3\60\3\60\3\61\3\61\3\61\3\61\7\61\u013a")
        buf.write("\n\61\f\61\16\61\u013d\13\61\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\62\3\62\3\62\3\62\7\62\u0148\n\62\f\62\16\62\u014b")
        buf.write("\13\62\3\62\3\62\3\63\3\63\7\63\u0151\n\63\f\63\16\63")
        buf.write("\u0154\13\63\3\63\3\63\4\u013b\u0152\2\64\3\3\5\4\7\5")
        buf.write("\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35")
        buf.write("\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33")
        buf.write("\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[")
        buf.write("/]\60_\61a\62c\63e\64\3\2\n\4\2\f\f\17\17\3\2\63;\3\2")
        buf.write("\62;\3\2\2\u0081\3\2//\5\2C\\aac|\6\2\62;C\\aac|\5\2\13")
        buf.write("\f\17\17\"\"\2\u0161\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2")
        buf.write("\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2")
        buf.write("\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31")
        buf.write("\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2")
        buf.write("\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3")
        buf.write("\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2")
        buf.write("\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3")
        buf.write("\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G")
        buf.write("\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2")
        buf.write("Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2")
        buf.write("\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2")
        buf.write("\2\2e\3\2\2\2\3g\3\2\2\2\5i\3\2\2\2\7z\3\2\2\2\t~\3\2")
        buf.write("\2\2\13\u0083\3\2\2\2\r\u0088\3\2\2\2\17\u0092\3\2\2\2")
        buf.write("\21\u0099\3\2\2\2\23\u009f\3\2\2\2\25\u00a8\3\2\2\2\27")
        buf.write("\u00ab\3\2\2\2\31\u00b0\3\2\2\2\33\u00b7\3\2\2\2\35\u00bd")
        buf.write("\3\2\2\2\37\u00bf\3\2\2\2!\u00c2\3\2\2\2#\u00c5\3\2\2")
        buf.write("\2%\u00c7\3\2\2\2\'\u00c9\3\2\2\2)\u00cb\3\2\2\2+\u00cd")
        buf.write("\3\2\2\2-\u00cf\3\2\2\2/\u00d1\3\2\2\2\61\u00d4\3\2\2")
        buf.write("\2\63\u00d7\3\2\2\2\65\u00da\3\2\2\2\67\u00dd\3\2\2\2")
        buf.write("9\u00df\3\2\2\2;\u00e1\3\2\2\2=\u00e3\3\2\2\2?\u00e5\3")
        buf.write("\2\2\2A\u00e8\3\2\2\2C\u00eb\3\2\2\2E\u00ed\3\2\2\2G\u00ef")
        buf.write("\3\2\2\2I\u00f1\3\2\2\2K\u00f3\3\2\2\2M\u00f5\3\2\2\2")
        buf.write("O\u00f7\3\2\2\2Q\u00f9\3\2\2\2S\u00fe\3\2\2\2U\u0104\3")
        buf.write("\2\2\2W\u010b\3\2\2\2Y\u0112\3\2\2\2[\u0125\3\2\2\2]\u0127")
        buf.write("\3\2\2\2_\u012f\3\2\2\2a\u0135\3\2\2\2c\u0143\3\2\2\2")
        buf.write("e\u014e\3\2\2\2gh\7.\2\2h\4\3\2\2\2ij\7%\2\2jk\7k\2\2")
        buf.write("kl\7p\2\2lm\7e\2\2mn\7n\2\2no\7w\2\2op\7f\2\2pq\7g\2\2")
        buf.write("qu\3\2\2\2rt\n\2\2\2sr\3\2\2\2tw\3\2\2\2us\3\2\2\2uv\3")
        buf.write("\2\2\2vx\3\2\2\2wu\3\2\2\2xy\b\3\2\2y\6\3\2\2\2z{\7k\2")
        buf.write("\2{|\7p\2\2|}\7v\2\2}\b\3\2\2\2~\177\7x\2\2\177\u0080")
        buf.write("\7q\2\2\u0080\u0081\7k\2\2\u0081\u0082\7f\2\2\u0082\n")
        buf.write("\3\2\2\2\u0083\u0084\7e\2\2\u0084\u0085\7j\2\2\u0085\u0086")
        buf.write("\7c\2\2\u0086\u0087\7t\2\2\u0087\f\3\2\2\2\u0088\u0089")
        buf.write("\7n\2\2\u0089\u008a\7q\2\2\u008a\u008b\7p\2\2\u008b\u008c")
        buf.write("\7i\2\2\u008c\u008d\7\"\2\2\u008d\u008e\7n\2\2\u008e\u008f")
        buf.write("\7q\2\2\u008f\u0090\7p\2\2\u0090\u0091\7i\2\2\u0091\16")
        buf.write("\3\2\2\2\u0092\u0093\7f\2\2\u0093\u0094\7q\2\2\u0094\u0095")
        buf.write("\7w\2\2\u0095\u0096\7d\2\2\u0096\u0097\7n\2\2\u0097\u0098")
        buf.write("\7g\2\2\u0098\20\3\2\2\2\u0099\u009a\7d\2\2\u009a\u009b")
        buf.write("\7t\2\2\u009b\u009c\7g\2\2\u009c\u009d\7c\2\2\u009d\u009e")
        buf.write("\7m\2\2\u009e\22\3\2\2\2\u009f\u00a0\7e\2\2\u00a0\u00a1")
        buf.write("\7q\2\2\u00a1\u00a2\7p\2\2\u00a2\u00a3\7v\2\2\u00a3\u00a4")
        buf.write("\7k\2\2\u00a4\u00a5\7p\2\2\u00a5\u00a6\7w\2\2\u00a6\u00a7")
        buf.write("\7g\2\2\u00a7\24\3\2\2\2\u00a8\u00a9\7k\2\2\u00a9\u00aa")
        buf.write("\7h\2\2\u00aa\26\3\2\2\2\u00ab\u00ac\7g\2\2\u00ac\u00ad")
        buf.write("\7n\2\2\u00ad\u00ae\7u\2\2\u00ae\u00af\7g\2\2\u00af\30")
        buf.write("\3\2\2\2\u00b0\u00b1\7t\2\2\u00b1\u00b2\7g\2\2\u00b2\u00b3")
        buf.write("\7v\2\2\u00b3\u00b4\7w\2\2\u00b4\u00b5\7t\2\2\u00b5\u00b6")
        buf.write("\7p\2\2\u00b6\32\3\2\2\2\u00b7\u00b8\7y\2\2\u00b8\u00b9")
        buf.write("\7j\2\2\u00b9\u00ba\7k\2\2\u00ba\u00bb\7n\2\2\u00bb\u00bc")
        buf.write("\7g\2\2\u00bc\34\3\2\2\2\u00bd\u00be\7-\2\2\u00be\36\3")
        buf.write("\2\2\2\u00bf\u00c0\7-\2\2\u00c0\u00c1\7-\2\2\u00c1 \3")
        buf.write("\2\2\2\u00c2\u00c3\7/\2\2\u00c3\u00c4\7/\2\2\u00c4\"\3")
        buf.write("\2\2\2\u00c5\u00c6\7/\2\2\u00c6$\3\2\2\2\u00c7\u00c8\7")
        buf.write(",\2\2\u00c8&\3\2\2\2\u00c9\u00ca\7\61\2\2\u00ca(\3\2\2")
        buf.write("\2\u00cb\u00cc\7\'\2\2\u00cc*\3\2\2\2\u00cd\u00ce\7@\2")
        buf.write("\2\u00ce,\3\2\2\2\u00cf\u00d0\7>\2\2\u00d0.\3\2\2\2\u00d1")
        buf.write("\u00d2\7@\2\2\u00d2\u00d3\7?\2\2\u00d3\60\3\2\2\2\u00d4")
        buf.write("\u00d5\7>\2\2\u00d5\u00d6\7?\2\2\u00d6\62\3\2\2\2\u00d7")
        buf.write("\u00d8\7?\2\2\u00d8\u00d9\7?\2\2\u00d9\64\3\2\2\2\u00da")
        buf.write("\u00db\7#\2\2\u00db\u00dc\7?\2\2\u00dc\66\3\2\2\2\u00dd")
        buf.write("\u00de\7#\2\2\u00de8\3\2\2\2\u00df\u00e0\7?\2\2\u00e0")
        buf.write(":\3\2\2\2\u00e1\u00e2\7(\2\2\u00e2<\3\2\2\2\u00e3\u00e4")
        buf.write("\7~\2\2\u00e4>\3\2\2\2\u00e5\u00e6\7(\2\2\u00e6\u00e7")
        buf.write("\7(\2\2\u00e7@\3\2\2\2\u00e8\u00e9\7~\2\2\u00e9\u00ea")
        buf.write("\7~\2\2\u00eaB\3\2\2\2\u00eb\u00ec\7=\2\2\u00ecD\3\2\2")
        buf.write("\2\u00ed\u00ee\7*\2\2\u00eeF\3\2\2\2\u00ef\u00f0\7+\2")
        buf.write("\2\u00f0H\3\2\2\2\u00f1\u00f2\7]\2\2\u00f2J\3\2\2\2\u00f3")
        buf.write("\u00f4\7_\2\2\u00f4L\3\2\2\2\u00f5\u00f6\7}\2\2\u00f6")
        buf.write("N\3\2\2\2\u00f7\u00f8\7\177\2\2\u00f8P\3\2\2\2\u00f9\u00fa")
        buf.write("\7v\2\2\u00fa\u00fb\7t\2\2\u00fb\u00fc\7w\2\2\u00fc\u00fd")
        buf.write("\7g\2\2\u00fdR\3\2\2\2\u00fe\u00ff\7h\2\2\u00ff\u0100")
        buf.write("\7c\2\2\u0100\u0101\7n\2\2\u0101\u0102\7u\2\2\u0102\u0103")
        buf.write("\7g\2\2\u0103T\3\2\2\2\u0104\u0105\7u\2\2\u0105\u0106")
        buf.write("\7k\2\2\u0106\u0107\7|\2\2\u0107\u0108\7g\2\2\u0108\u0109")
        buf.write("\7q\2\2\u0109\u010a\7h\2\2\u010aV\3\2\2\2\u010b\u010f")
        buf.write("\t\3\2\2\u010c\u010e\t\4\2\2\u010d\u010c\3\2\2\2\u010e")
        buf.write("\u0111\3\2\2\2\u010f\u010d\3\2\2\2\u010f\u0110\3\2\2\2")
        buf.write("\u0110X\3\2\2\2\u0111\u010f\3\2\2\2\u0112\u0116\7)\2\2")
        buf.write("\u0113\u0117\t\5\2\2\u0114\u0115\7^\2\2\u0115\u0117\7")
        buf.write("\62\2\2\u0116\u0113\3\2\2\2\u0116\u0114\3\2\2\2\u0117")
        buf.write("\u0118\3\2\2\2\u0118\u0119\7)\2\2\u0119Z\3\2\2\2\u011a")
        buf.write("\u011c\t\6\2\2\u011b\u011a\3\2\2\2\u011b\u011c\3\2\2\2")
        buf.write("\u011c\u011d\3\2\2\2\u011d\u0121\t\3\2\2\u011e\u0120\t")
        buf.write("\4\2\2\u011f\u011e\3\2\2\2\u0120\u0123\3\2\2\2\u0121\u011f")
        buf.write("\3\2\2\2\u0121\u0122\3\2\2\2\u0122\u0126\3\2\2\2\u0123")
        buf.write("\u0121\3\2\2\2\u0124\u0126\7\62\2\2\u0125\u011b\3\2\2")
        buf.write("\2\u0125\u0124\3\2\2\2\u0126\\\3\2\2\2\u0127\u012b\t\7")
        buf.write("\2\2\u0128\u012a\t\b\2\2\u0129\u0128\3\2\2\2\u012a\u012d")
        buf.write("\3\2\2\2\u012b\u0129\3\2\2\2\u012b\u012c\3\2\2\2\u012c")
        buf.write("^\3\2\2\2\u012d\u012b\3\2\2\2\u012e\u0130\t\t\2\2\u012f")
        buf.write("\u012e\3\2\2\2\u0130\u0131\3\2\2\2\u0131\u012f\3\2\2\2")
        buf.write("\u0131\u0132\3\2\2\2\u0132\u0133\3\2\2\2\u0133\u0134\b")
        buf.write("\60\2\2\u0134`\3\2\2\2\u0135\u0136\7\61\2\2\u0136\u0137")
        buf.write("\7,\2\2\u0137\u013b\3\2\2\2\u0138\u013a\13\2\2\2\u0139")
        buf.write("\u0138\3\2\2\2\u013a\u013d\3\2\2\2\u013b\u013c\3\2\2\2")
        buf.write("\u013b\u0139\3\2\2\2\u013c\u013e\3\2\2\2\u013d\u013b\3")
        buf.write("\2\2\2\u013e\u013f\7,\2\2\u013f\u0140\7\61\2\2\u0140\u0141")
        buf.write("\3\2\2\2\u0141\u0142\b\61\2\2\u0142b\3\2\2\2\u0143\u0144")
        buf.write("\7\61\2\2\u0144\u0145\7\61\2\2\u0145\u0149\3\2\2\2\u0146")
        buf.write("\u0148\n\2\2\2\u0147\u0146\3\2\2\2\u0148\u014b\3\2\2\2")
        buf.write("\u0149\u0147\3\2\2\2\u0149\u014a\3\2\2\2\u014a\u014c\3")
        buf.write("\2\2\2\u014b\u0149\3\2\2\2\u014c\u014d\b\62\2\2\u014d")
        buf.write("d\3\2\2\2\u014e\u0152\7$\2\2\u014f\u0151\13\2\2\2\u0150")
        buf.write("\u014f\3\2\2\2\u0151\u0154\3\2\2\2\u0152\u0153\3\2\2\2")
        buf.write("\u0152\u0150\3\2\2\2\u0153\u0155\3\2\2\2\u0154\u0152\3")
        buf.write("\2\2\2\u0155\u0156\7$\2\2\u0156f\3\2\2\2\16\2u\u010f\u0116")
        buf.write("\u011b\u0121\u0125\u012b\u0131\u013b\u0149\u0152\3\b\2")
        buf.write("\2")
        return buf.getvalue()


class naiveCLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    Include = 2
    TypeInt = 3
    TypeVoid = 4
    TypeChar = 5
    TypeLL = 6
    TypeDouble = 7
    Break = 8
    Continue = 9
    If = 10
    Else = 11
    Return = 12
    While = 13
    ADD = 14
    ADDADD = 15
    SUBSUB = 16
    SUB = 17
    MUL = 18
    DIV = 19
    MOD = 20
    Greater = 21
    Less = 22
    GreaterEqual = 23
    LessEqual = 24
    Equal = 25
    NotEqual = 26
    Not = 27
    AssignOperator = 28
    ArithmeticAnd = 29
    ArithmeticOR = 30
    LogicAnd = 31
    LogicOR = 32
    Semicolon = 33
    LeftParentheses = 34
    RightParentheses = 35
    LeftBracket = 36
    RightBracket = 37
    LeftBrace = 38
    RightBrace = 39
    TRUE = 40
    FALSE = 41
    SIZEOF = 42
    PositiveINT = 43
    Char = 44
    INT = 45
    ID = 46
    WS = 47
    BlockComment = 48
    LineComment = 49
    String = 50

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "','", "'int'", "'void'", "'char'", "'long long'", "'double'", 
            "'break'", "'continue'", "'if'", "'else'", "'return'", "'while'", 
            "'+'", "'++'", "'--'", "'-'", "'*'", "'/'", "'%'", "'>'", "'<'", 
            "'>='", "'<='", "'=='", "'!='", "'!'", "'='", "'&'", "'|'", 
            "'&&'", "'||'", "';'", "'('", "')'", "'['", "']'", "'{'", "'}'", 
            "'true'", "'false'", "'sizeof'" ]

    symbolicNames = [ "<INVALID>",
            "Include", "TypeInt", "TypeVoid", "TypeChar", "TypeLL", "TypeDouble", 
            "Break", "Continue", "If", "Else", "Return", "While", "ADD", 
            "ADDADD", "SUBSUB", "SUB", "MUL", "DIV", "MOD", "Greater", "Less", 
            "GreaterEqual", "LessEqual", "Equal", "NotEqual", "Not", "AssignOperator", 
            "ArithmeticAnd", "ArithmeticOR", "LogicAnd", "LogicOR", "Semicolon", 
            "LeftParentheses", "RightParentheses", "LeftBracket", "RightBracket", 
            "LeftBrace", "RightBrace", "TRUE", "FALSE", "SIZEOF", "PositiveINT", 
            "Char", "INT", "ID", "WS", "BlockComment", "LineComment", "String" ]

    ruleNames = [ "T__0", "Include", "TypeInt", "TypeVoid", "TypeChar", 
                  "TypeLL", "TypeDouble", "Break", "Continue", "If", "Else", 
                  "Return", "While", "ADD", "ADDADD", "SUBSUB", "SUB", "MUL", 
                  "DIV", "MOD", "Greater", "Less", "GreaterEqual", "LessEqual", 
                  "Equal", "NotEqual", "Not", "AssignOperator", "ArithmeticAnd", 
                  "ArithmeticOR", "LogicAnd", "LogicOR", "Semicolon", "LeftParentheses", 
                  "RightParentheses", "LeftBracket", "RightBracket", "LeftBrace", 
                  "RightBrace", "TRUE", "FALSE", "SIZEOF", "PositiveINT", 
                  "Char", "INT", "ID", "WS", "BlockComment", "LineComment", 
                  "String" ]

    grammarFileName = "naiveC.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


