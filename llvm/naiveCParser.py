# Generated from E:/Tsinghua/课程/大三上/汇编与编译原理/作业/编译/编译小组作业/src/Compile/antlr/src\naiveC.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\64")
        buf.write("\u014f\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\3\2\3\2")
        buf.write("\3\3\3\3\3\3\3\3\5\3A\n\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3")
        buf.write("I\n\3\f\3\16\3L\13\3\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\7\3")
        buf.write("\7\3\7\3\b\3\b\3\t\3\t\3\t\3\t\5\t^\n\t\3\n\3\n\3\n\3")
        buf.write("\n\5\nd\n\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\5\n\u0083\n\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\7\n\u008b\n\n\f\n\16\n\u008e\13\n\3\13\3\13\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u009e\n")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\f\7\f\u00a6\n\f\f\f\16\f\u00a9")
        buf.write("\13\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00be\n\r\3\16\3\16\5")
        buf.write("\16\u00c2\n\16\3\16\3\16\3\16\5\16\u00c7\n\16\3\16\3\16")
        buf.write("\3\16\3\16\5\16\u00cd\n\16\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\5\16\u00d5\n\16\3\17\3\17\3\17\3\20\3\20\5\20\u00dc")
        buf.write("\n\20\3\20\3\20\3\21\3\21\3\21\5\21\u00e3\n\21\3\22\3")
        buf.write("\22\5\22\u00e7\n\22\3\22\3\22\3\22\7\22\u00ec\n\22\f\22")
        buf.write("\16\22\u00ef\13\22\3\23\3\23\5\23\u00f3\n\23\3\23\3\23")
        buf.write("\3\24\3\24\5\24\u00f9\n\24\3\24\3\24\3\24\7\24\u00fe\n")
        buf.write("\24\f\24\16\24\u0101\13\24\3\25\3\25\3\25\3\25\3\26\3")
        buf.write("\26\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\7\30\u0116\n\30\f\30\16\30\u0119\13\30")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\7\32\u012d\n\32\f")
        buf.write("\32\16\32\u0130\13\32\3\32\3\32\5\32\u0134\n\32\3\33\3")
        buf.write("\33\3\33\3\33\3\33\3\34\3\34\5\34\u013d\n\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\35\3\35\5\35\u0147\n\35\3\35\3")
        buf.write("\35\3\35\3\35\3\35\3\35\3\35\2\7\4\22\26\"&\36\2\4\6\b")
        buf.write("\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668")
        buf.write("\2\b\4\2\5\5\7\t\3\2\5\t\3\2*+\3\2\24\25\4\2\20\20\23")
        buf.write("\23\3\2\27\34\2\u0167\2:\3\2\2\2\4@\3\2\2\2\6M\3\2\2\2")
        buf.write("\bO\3\2\2\2\nR\3\2\2\2\fT\3\2\2\2\16W\3\2\2\2\20]\3\2")
        buf.write("\2\2\22\u0082\3\2\2\2\24\u008f\3\2\2\2\26\u009d\3\2\2")
        buf.write("\2\30\u00bd\3\2\2\2\32\u00d4\3\2\2\2\34\u00d6\3\2\2\2")
        buf.write("\36\u00d9\3\2\2\2 \u00e2\3\2\2\2\"\u00e4\3\2\2\2$\u00f2")
        buf.write("\3\2\2\2&\u00f6\3\2\2\2(\u0102\3\2\2\2*\u0106\3\2\2\2")
        buf.write(",\u0109\3\2\2\2.\u0117\3\2\2\2\60\u011a\3\2\2\2\62\u0120")
        buf.write("\3\2\2\2\64\u0135\3\2\2\2\66\u013c\3\2\2\28\u0146\3\2")
        buf.write("\2\2:;\5\4\3\2;\3\3\2\2\2<=\b\3\1\2=A\5\64\33\2>A\5\66")
        buf.write("\34\2?A\58\35\2@<\3\2\2\2@>\3\2\2\2@?\3\2\2\2AJ\3\2\2")
        buf.write("\2BC\f\5\2\2CI\5\64\33\2DE\f\4\2\2EI\58\35\2FG\f\3\2\2")
        buf.write("GI\5\66\34\2HB\3\2\2\2HD\3\2\2\2HF\3\2\2\2IL\3\2\2\2J")
        buf.write("H\3\2\2\2JK\3\2\2\2K\5\3\2\2\2LJ\3\2\2\2MN\t\2\2\2N\7")
        buf.write("\3\2\2\2OP\5\6\4\2PQ\7\24\2\2Q\t\3\2\2\2RS\t\3\2\2S\13")
        buf.write("\3\2\2\2TU\5\n\6\2UV\7\24\2\2V\r\3\2\2\2WX\t\4\2\2X\17")
        buf.write("\3\2\2\2YZ\7\60\2\2Z[\7\3\2\2[^\5\20\t\2\\^\7\60\2\2]")
        buf.write("Y\3\2\2\2]\\\3\2\2\2^\21\3\2\2\2_`\b\n\1\2`c\7$\2\2ad")
        buf.write("\5\b\5\2bd\5\6\4\2ca\3\2\2\2cb\3\2\2\2de\3\2\2\2ef\7%")
        buf.write("\2\2fg\5\22\n\21g\u0083\3\2\2\2hi\7\23\2\2i\u0083\5\22")
        buf.write("\n\20jk\7\24\2\2k\u0083\5\22\n\17lm\7\37\2\2m\u0083\7")
        buf.write("\60\2\2n\u0083\7-\2\2o\u0083\7.\2\2p\u0083\7/\2\2q\u0083")
        buf.write("\7\60\2\2r\u0083\5\64\33\2st\7,\2\2tu\7$\2\2uv\5\n\6\2")
        buf.write("vw\7%\2\2w\u0083\3\2\2\2x\u0083\5\16\b\2yz\7\60\2\2z{")
        buf.write("\7&\2\2{|\5\22\n\2|}\7\'\2\2}\u0083\3\2\2\2~\177\7$\2")
        buf.write("\2\177\u0080\5\22\n\2\u0080\u0081\7%\2\2\u0081\u0083\3")
        buf.write("\2\2\2\u0082_\3\2\2\2\u0082h\3\2\2\2\u0082j\3\2\2\2\u0082")
        buf.write("l\3\2\2\2\u0082n\3\2\2\2\u0082o\3\2\2\2\u0082p\3\2\2\2")
        buf.write("\u0082q\3\2\2\2\u0082r\3\2\2\2\u0082s\3\2\2\2\u0082x\3")
        buf.write("\2\2\2\u0082y\3\2\2\2\u0082~\3\2\2\2\u0083\u008c\3\2\2")
        buf.write("\2\u0084\u0085\f\4\2\2\u0085\u0086\t\5\2\2\u0086\u008b")
        buf.write("\5\22\n\5\u0087\u0088\f\3\2\2\u0088\u0089\t\6\2\2\u0089")
        buf.write("\u008b\5\22\n\4\u008a\u0084\3\2\2\2\u008a\u0087\3\2\2")
        buf.write("\2\u008b\u008e\3\2\2\2\u008c\u008a\3\2\2\2\u008c\u008d")
        buf.write("\3\2\2\2\u008d\23\3\2\2\2\u008e\u008c\3\2\2\2\u008f\u0090")
        buf.write("\t\7\2\2\u0090\25\3\2\2\2\u0091\u0092\b\f\1\2\u0092\u0093")
        buf.write("\7\35\2\2\u0093\u009e\5\26\f\b\u0094\u0095\7$\2\2\u0095")
        buf.write("\u0096\5\26\f\2\u0096\u0097\7%\2\2\u0097\u009e\3\2\2\2")
        buf.write("\u0098\u0099\5\22\n\2\u0099\u009a\5\24\13\2\u009a\u009b")
        buf.write("\5\22\n\2\u009b\u009e\3\2\2\2\u009c\u009e\5\22\n\2\u009d")
        buf.write("\u0091\3\2\2\2\u009d\u0094\3\2\2\2\u009d\u0098\3\2\2\2")
        buf.write("\u009d\u009c\3\2\2\2\u009e\u00a7\3\2\2\2\u009f\u00a0\f")
        buf.write("\7\2\2\u00a0\u00a1\7!\2\2\u00a1\u00a6\5\26\f\b\u00a2\u00a3")
        buf.write("\f\6\2\2\u00a3\u00a4\7\"\2\2\u00a4\u00a6\5\26\f\7\u00a5")
        buf.write("\u009f\3\2\2\2\u00a5\u00a2\3\2\2\2\u00a6\u00a9\3\2\2\2")
        buf.write("\u00a7\u00a5\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8\27\3\2")
        buf.write("\2\2\u00a9\u00a7\3\2\2\2\u00aa\u00ab\7\60\2\2\u00ab\u00ac")
        buf.write("\7\36\2\2\u00ac\u00ad\5\22\n\2\u00ad\u00ae\7#\2\2\u00ae")
        buf.write("\u00be\3\2\2\2\u00af\u00b0\7\24\2\2\u00b0\u00b1\7\60\2")
        buf.write("\2\u00b1\u00b2\7\36\2\2\u00b2\u00b3\5\22\n\2\u00b3\u00b4")
        buf.write("\7#\2\2\u00b4\u00be\3\2\2\2\u00b5\u00b6\7\60\2\2\u00b6")
        buf.write("\u00b7\7&\2\2\u00b7\u00b8\5\22\n\2\u00b8\u00b9\7\'\2\2")
        buf.write("\u00b9\u00ba\7\36\2\2\u00ba\u00bb\5\22\n\2\u00bb\u00bc")
        buf.write("\7#\2\2\u00bc\u00be\3\2\2\2\u00bd\u00aa\3\2\2\2\u00bd")
        buf.write("\u00af\3\2\2\2\u00bd\u00b5\3\2\2\2\u00be\31\3\2\2\2\u00bf")
        buf.write("\u00c2\5\6\4\2\u00c0\u00c2\5\b\5\2\u00c1\u00bf\3\2\2\2")
        buf.write("\u00c1\u00c0\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3\u00c6\7")
        buf.write("\60\2\2\u00c4\u00c5\7\36\2\2\u00c5\u00c7\5\22\n\2\u00c6")
        buf.write("\u00c4\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7\u00c8\3\2\2\2")
        buf.write("\u00c8\u00c9\7#\2\2\u00c9\u00d5\3\2\2\2\u00ca\u00cd\5")
        buf.write("\6\4\2\u00cb\u00cd\5\b\5\2\u00cc\u00ca\3\2\2\2\u00cc\u00cb")
        buf.write("\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce\u00cf\7\60\2\2\u00cf")
        buf.write("\u00d0\7&\2\2\u00d0\u00d1\7-\2\2\u00d1\u00d2\7\'\2\2\u00d2")
        buf.write("\u00d3\7#\2\2\u00d3\u00d5\3\2\2\2\u00d4\u00c1\3\2\2\2")
        buf.write("\u00d4\u00cc\3\2\2\2\u00d5\33\3\2\2\2\u00d6\u00d7\5\64")
        buf.write("\33\2\u00d7\u00d8\7#\2\2\u00d8\35\3\2\2\2\u00d9\u00db")
        buf.write("\7\16\2\2\u00da\u00dc\5\22\n\2\u00db\u00da\3\2\2\2\u00db")
        buf.write("\u00dc\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\u00de\7#\2\2")
        buf.write("\u00de\37\3\2\2\2\u00df\u00e3\5\22\n\2\u00e0\u00e3\5\64")
        buf.write("\33\2\u00e1\u00e3\7\64\2\2\u00e2\u00df\3\2\2\2\u00e2\u00e0")
        buf.write("\3\2\2\2\u00e2\u00e1\3\2\2\2\u00e3!\3\2\2\2\u00e4\u00e6")
        buf.write("\b\22\1\2\u00e5\u00e7\5 \21\2\u00e6\u00e5\3\2\2\2\u00e6")
        buf.write("\u00e7\3\2\2\2\u00e7\u00ed\3\2\2\2\u00e8\u00e9\f\4\2\2")
        buf.write("\u00e9\u00ea\7\3\2\2\u00ea\u00ec\5 \21\2\u00eb\u00e8\3")
        buf.write("\2\2\2\u00ec\u00ef\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ed\u00ee")
        buf.write("\3\2\2\2\u00ee#\3\2\2\2\u00ef\u00ed\3\2\2\2\u00f0\u00f3")
        buf.write("\5\n\6\2\u00f1\u00f3\5\f\7\2\u00f2\u00f0\3\2\2\2\u00f2")
        buf.write("\u00f1\3\2\2\2\u00f3\u00f4\3\2\2\2\u00f4\u00f5\7\60\2")
        buf.write("\2\u00f5%\3\2\2\2\u00f6\u00f8\b\24\1\2\u00f7\u00f9\5$")
        buf.write("\23\2\u00f8\u00f7\3\2\2\2\u00f8\u00f9\3\2\2\2\u00f9\u00ff")
        buf.write("\3\2\2\2\u00fa\u00fb\f\4\2\2\u00fb\u00fc\7\3\2\2\u00fc")
        buf.write("\u00fe\5$\23\2\u00fd\u00fa\3\2\2\2\u00fe\u0101\3\2\2\2")
        buf.write("\u00ff\u00fd\3\2\2\2\u00ff\u0100\3\2\2\2\u0100\'\3\2\2")
        buf.write("\2\u0101\u00ff\3\2\2\2\u0102\u0103\7(\2\2\u0103\u0104")
        buf.write("\5.\30\2\u0104\u0105\7)\2\2\u0105)\3\2\2\2\u0106\u0107")
        buf.write("\7\n\2\2\u0107\u0108\7#\2\2\u0108+\3\2\2\2\u0109\u010a")
        buf.write("\7\13\2\2\u010a\u010b\7#\2\2\u010b-\3\2\2\2\u010c\u0116")
        buf.write("\5\30\r\2\u010d\u0116\5\32\16\2\u010e\u0116\5\34\17\2")
        buf.write("\u010f\u0116\5\60\31\2\u0110\u0116\5(\25\2\u0111\u0116")
        buf.write("\5\62\32\2\u0112\u0116\5\36\20\2\u0113\u0116\5*\26\2\u0114")
        buf.write("\u0116\5,\27\2\u0115\u010c\3\2\2\2\u0115\u010d\3\2\2\2")
        buf.write("\u0115\u010e\3\2\2\2\u0115\u010f\3\2\2\2\u0115\u0110\3")
        buf.write("\2\2\2\u0115\u0111\3\2\2\2\u0115\u0112\3\2\2\2\u0115\u0113")
        buf.write("\3\2\2\2\u0115\u0114\3\2\2\2\u0116\u0119\3\2\2\2\u0117")
        buf.write("\u0115\3\2\2\2\u0117\u0118\3\2\2\2\u0118/\3\2\2\2\u0119")
        buf.write("\u0117\3\2\2\2\u011a\u011b\7\17\2\2\u011b\u011c\7$\2\2")
        buf.write("\u011c\u011d\5\26\f\2\u011d\u011e\7%\2\2\u011e\u011f\5")
        buf.write("(\25\2\u011f\61\3\2\2\2\u0120\u0121\7\f\2\2\u0121\u0122")
        buf.write("\7$\2\2\u0122\u0123\5\26\f\2\u0123\u0124\7%\2\2\u0124")
        buf.write("\u012e\5(\25\2\u0125\u0126\7\r\2\2\u0126\u0127\7\f\2\2")
        buf.write("\u0127\u0128\7$\2\2\u0128\u0129\5\26\f\2\u0129\u012a\7")
        buf.write("%\2\2\u012a\u012b\5(\25\2\u012b\u012d\3\2\2\2\u012c\u0125")
        buf.write("\3\2\2\2\u012d\u0130\3\2\2\2\u012e\u012c\3\2\2\2\u012e")
        buf.write("\u012f\3\2\2\2\u012f\u0133\3\2\2\2\u0130\u012e\3\2\2\2")
        buf.write("\u0131\u0132\7\r\2\2\u0132\u0134\5(\25\2\u0133\u0131\3")
        buf.write("\2\2\2\u0133\u0134\3\2\2\2\u0134\63\3\2\2\2\u0135\u0136")
        buf.write("\7\60\2\2\u0136\u0137\7$\2\2\u0137\u0138\5\"\22\2\u0138")
        buf.write("\u0139\7%\2\2\u0139\65\3\2\2\2\u013a\u013d\5\n\6\2\u013b")
        buf.write("\u013d\5\f\7\2\u013c\u013a\3\2\2\2\u013c\u013b\3\2\2\2")
        buf.write("\u013d\u013e\3\2\2\2\u013e\u013f\7\60\2\2\u013f\u0140")
        buf.write("\7$\2\2\u0140\u0141\5&\24\2\u0141\u0142\7%\2\2\u0142\u0143")
        buf.write("\7#\2\2\u0143\67\3\2\2\2\u0144\u0147\5\n\6\2\u0145\u0147")
        buf.write("\5\f\7\2\u0146\u0144\3\2\2\2\u0146\u0145\3\2\2\2\u0147")
        buf.write("\u0148\3\2\2\2\u0148\u0149\7\60\2\2\u0149\u014a\7$\2\2")
        buf.write("\u014a\u014b\5&\24\2\u014b\u014c\7%\2\2\u014c\u014d\5")
        buf.write("(\25\2\u014d9\3\2\2\2\37@HJ]c\u0082\u008a\u008c\u009d")
        buf.write("\u00a5\u00a7\u00bd\u00c1\u00c6\u00cc\u00d4\u00db\u00e2")
        buf.write("\u00e6\u00ed\u00f2\u00f8\u00ff\u0115\u0117\u012e\u0133")
        buf.write("\u013c\u0146")
        return buf.getvalue()


class naiveCParser ( Parser ):

    grammarFileName = "naiveC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "<INVALID>", "'int'", "'void'", 
                     "'char'", "'long long'", "'double'", "'break'", "'continue'", 
                     "'if'", "'else'", "'return'", "'while'", "'+'", "'++'", 
                     "'--'", "'-'", "'*'", "'/'", "'%'", "'>'", "'<'", "'>='", 
                     "'<='", "'=='", "'!='", "'!'", "'='", "'&'", "'|'", 
                     "'&&'", "'||'", "';'", "'('", "')'", "'['", "']'", 
                     "'{'", "'}'", "'true'", "'false'", "'sizeof'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "Include", "TypeInt", "TypeVoid", 
                      "TypeChar", "TypeLL", "TypeDouble", "Break", "Continue", 
                      "If", "Else", "Return", "While", "ADD", "ADDADD", 
                      "SUBSUB", "SUB", "MUL", "DIV", "MOD", "Greater", "Less", 
                      "GreaterEqual", "LessEqual", "Equal", "NotEqual", 
                      "Not", "AssignOperator", "ArithmeticAnd", "ArithmeticOR", 
                      "LogicAnd", "LogicOR", "Semicolon", "LeftParentheses", 
                      "RightParentheses", "LeftBracket", "RightBracket", 
                      "LeftBrace", "RightBrace", "TRUE", "FALSE", "SIZEOF", 
                      "PositiveINT", "Char", "INT", "ID", "WS", "BlockComment", 
                      "LineComment", "String" ]

    RULE_prog = 0
    RULE_r = 1
    RULE_realTypeID = 2
    RULE_realTypeIDPointer = 3
    RULE_typeIdentifier = 4
    RULE_typeIdentifierPointer = 5
    RULE_boolExpr = 6
    RULE_idList = 7
    RULE_expr = 8
    RULE_conditionOperator = 9
    RULE_conditionExpr = 10
    RULE_assignment = 11
    RULE_definition = 12
    RULE_callProc = 13
    RULE_returnLine = 14
    RULE_param = 15
    RULE_paramList = 16
    RULE_defineParam = 17
    RULE_defineParamList = 18
    RULE_block = 19
    RULE_breakLine = 20
    RULE_continueLine = 21
    RULE_statements = 22
    RULE_whileBlock = 23
    RULE_ifBlock = 24
    RULE_functionCall = 25
    RULE_functionDeclare = 26
    RULE_functionDefine = 27

    ruleNames =  [ "prog", "r", "realTypeID", "realTypeIDPointer", "typeIdentifier", 
                   "typeIdentifierPointer", "boolExpr", "idList", "expr", 
                   "conditionOperator", "conditionExpr", "assignment", "definition", 
                   "callProc", "returnLine", "param", "paramList", "defineParam", 
                   "defineParamList", "block", "breakLine", "continueLine", 
                   "statements", "whileBlock", "ifBlock", "functionCall", 
                   "functionDeclare", "functionDefine" ]

    EOF = Token.EOF
    T__0=1
    Include=2
    TypeInt=3
    TypeVoid=4
    TypeChar=5
    TypeLL=6
    TypeDouble=7
    Break=8
    Continue=9
    If=10
    Else=11
    Return=12
    While=13
    ADD=14
    ADDADD=15
    SUBSUB=16
    SUB=17
    MUL=18
    DIV=19
    MOD=20
    Greater=21
    Less=22
    GreaterEqual=23
    LessEqual=24
    Equal=25
    NotEqual=26
    Not=27
    AssignOperator=28
    ArithmeticAnd=29
    ArithmeticOR=30
    LogicAnd=31
    LogicOR=32
    Semicolon=33
    LeftParentheses=34
    RightParentheses=35
    LeftBracket=36
    RightBracket=37
    LeftBrace=38
    RightBrace=39
    TRUE=40
    FALSE=41
    SIZEOF=42
    PositiveINT=43
    Char=44
    INT=45
    ID=46
    WS=47
    BlockComment=48
    LineComment=49
    String=50

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def r(self):
            return self.getTypedRuleContext(naiveCParser.RContext,0)


        def getRuleIndex(self):
            return naiveCParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = naiveCParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.r(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionCall(self):
            return self.getTypedRuleContext(naiveCParser.FunctionCallContext,0)


        def functionDeclare(self):
            return self.getTypedRuleContext(naiveCParser.FunctionDeclareContext,0)


        def functionDefine(self):
            return self.getTypedRuleContext(naiveCParser.FunctionDefineContext,0)


        def r(self):
            return self.getTypedRuleContext(naiveCParser.RContext,0)


        def getRuleIndex(self):
            return naiveCParser.RULE_r

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterR" ):
                listener.enterR(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitR" ):
                listener.exitR(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitR" ):
                return visitor.visitR(self)
            else:
                return visitor.visitChildren(self)



    def r(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = naiveCParser.RContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_r, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 59
                self.functionCall()
                pass

            elif la_ == 2:
                self.state = 60
                self.functionDeclare()
                pass

            elif la_ == 3:
                self.state = 61
                self.functionDefine()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 72
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 70
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = naiveCParser.RContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_r)
                        self.state = 64
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 65
                        self.functionCall()
                        pass

                    elif la_ == 2:
                        localctx = naiveCParser.RContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_r)
                        self.state = 66
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 67
                        self.functionDefine()
                        pass

                    elif la_ == 3:
                        localctx = naiveCParser.RContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_r)
                        self.state = 68
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 69
                        self.functionDeclare()
                        pass

             
                self.state = 74
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class RealTypeIDContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TypeChar(self):
            return self.getToken(naiveCParser.TypeChar, 0)

        def TypeInt(self):
            return self.getToken(naiveCParser.TypeInt, 0)

        def TypeLL(self):
            return self.getToken(naiveCParser.TypeLL, 0)

        def TypeDouble(self):
            return self.getToken(naiveCParser.TypeDouble, 0)

        def getRuleIndex(self):
            return naiveCParser.RULE_realTypeID

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRealTypeID" ):
                listener.enterRealTypeID(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRealTypeID" ):
                listener.exitRealTypeID(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRealTypeID" ):
                return visitor.visitRealTypeID(self)
            else:
                return visitor.visitChildren(self)




    def realTypeID(self):

        localctx = naiveCParser.RealTypeIDContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_realTypeID)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << naiveCParser.TypeInt) | (1 << naiveCParser.TypeChar) | (1 << naiveCParser.TypeLL) | (1 << naiveCParser.TypeDouble))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RealTypeIDPointerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def realTypeID(self):
            return self.getTypedRuleContext(naiveCParser.RealTypeIDContext,0)


        def MUL(self):
            return self.getToken(naiveCParser.MUL, 0)

        def getRuleIndex(self):
            return naiveCParser.RULE_realTypeIDPointer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRealTypeIDPointer" ):
                listener.enterRealTypeIDPointer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRealTypeIDPointer" ):
                listener.exitRealTypeIDPointer(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRealTypeIDPointer" ):
                return visitor.visitRealTypeIDPointer(self)
            else:
                return visitor.visitChildren(self)




    def realTypeIDPointer(self):

        localctx = naiveCParser.RealTypeIDPointerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_realTypeIDPointer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.realTypeID()
            self.state = 78
            self.match(naiveCParser.MUL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeIdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TypeInt(self):
            return self.getToken(naiveCParser.TypeInt, 0)

        def TypeVoid(self):
            return self.getToken(naiveCParser.TypeVoid, 0)

        def TypeChar(self):
            return self.getToken(naiveCParser.TypeChar, 0)

        def TypeLL(self):
            return self.getToken(naiveCParser.TypeLL, 0)

        def TypeDouble(self):
            return self.getToken(naiveCParser.TypeDouble, 0)

        def getRuleIndex(self):
            return naiveCParser.RULE_typeIdentifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeIdentifier" ):
                listener.enterTypeIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeIdentifier" ):
                listener.exitTypeIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeIdentifier" ):
                return visitor.visitTypeIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def typeIdentifier(self):

        localctx = naiveCParser.TypeIdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_typeIdentifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << naiveCParser.TypeInt) | (1 << naiveCParser.TypeVoid) | (1 << naiveCParser.TypeChar) | (1 << naiveCParser.TypeLL) | (1 << naiveCParser.TypeDouble))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeIdentifierPointerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeIdentifier(self):
            return self.getTypedRuleContext(naiveCParser.TypeIdentifierContext,0)


        def MUL(self):
            return self.getToken(naiveCParser.MUL, 0)

        def getRuleIndex(self):
            return naiveCParser.RULE_typeIdentifierPointer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeIdentifierPointer" ):
                listener.enterTypeIdentifierPointer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeIdentifierPointer" ):
                listener.exitTypeIdentifierPointer(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeIdentifierPointer" ):
                return visitor.visitTypeIdentifierPointer(self)
            else:
                return visitor.visitChildren(self)




    def typeIdentifierPointer(self):

        localctx = naiveCParser.TypeIdentifierPointerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_typeIdentifierPointer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.typeIdentifier()
            self.state = 83
            self.match(naiveCParser.MUL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoolExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(naiveCParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(naiveCParser.FALSE, 0)

        def getRuleIndex(self):
            return naiveCParser.RULE_boolExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolExpr" ):
                listener.enterBoolExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolExpr" ):
                listener.exitBoolExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolExpr" ):
                return visitor.visitBoolExpr(self)
            else:
                return visitor.visitChildren(self)




    def boolExpr(self):

        localctx = naiveCParser.BoolExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_boolExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            _la = self._input.LA(1)
            if not(_la==naiveCParser.TRUE or _la==naiveCParser.FALSE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(naiveCParser.ID, 0)

        def idList(self):
            return self.getTypedRuleContext(naiveCParser.IdListContext,0)


        def getRuleIndex(self):
            return naiveCParser.RULE_idList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdList" ):
                listener.enterIdList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdList" ):
                listener.exitIdList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdList" ):
                return visitor.visitIdList(self)
            else:
                return visitor.visitChildren(self)




    def idList(self):

        localctx = naiveCParser.IdListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_idList)
        try:
            self.state = 91
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 87
                self.match(naiveCParser.ID)
                self.state = 88
                self.match(naiveCParser.T__0)
                self.state = 89
                self.idList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 90
                self.match(naiveCParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return naiveCParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class PositiveINTContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a naiveCParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PositiveINT(self):
            return self.getToken(naiveCParser.PositiveINT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPositiveINT" ):
                listener.enterPositiveINT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPositiveINT" ):
                listener.exitPositiveINT(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPositiveINT" ):
                return visitor.visitPositiveINT(self)
            else:
                return visitor.visitChildren(self)


    class TrueFalseContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a naiveCParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def boolExpr(self):
            return self.getTypedRuleContext(naiveCParser.BoolExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrueFalse" ):
                listener.enterTrueFalse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrueFalse" ):
                listener.exitTrueFalse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrueFalse" ):
                return visitor.visitTrueFalse(self)
            else:
                return visitor.visitChildren(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a naiveCParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(naiveCParser.ExprContext)
            else:
                return self.getTypedRuleContext(naiveCParser.ExprContext,i)

        def MUL(self):
            return self.getToken(naiveCParser.MUL, 0)
        def DIV(self):
            return self.getToken(naiveCParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a naiveCParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(naiveCParser.ExprContext)
            else:
                return self.getTypedRuleContext(naiveCParser.ExprContext,i)

        def ADD(self):
            return self.getToken(naiveCParser.ADD, 0)
        def SUB(self):
            return self.getToken(naiveCParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSub" ):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a naiveCParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LeftParentheses(self):
            return self.getToken(naiveCParser.LeftParentheses, 0)
        def expr(self):
            return self.getTypedRuleContext(naiveCParser.ExprContext,0)

        def RightParentheses(self):
            return self.getToken(naiveCParser.RightParentheses, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a naiveCParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(naiveCParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)


    class NegativeContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a naiveCParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SUB(self):
            return self.getToken(naiveCParser.SUB, 0)
        def expr(self):
            return self.getTypedRuleContext(naiveCParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegative" ):
                listener.enterNegative(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegative" ):
                listener.exitNegative(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegative" ):
                return visitor.visitNegative(self)
            else:
                return visitor.visitChildren(self)


    class CharContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a naiveCParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Char(self):
            return self.getToken(naiveCParser.Char, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChar" ):
                listener.enterChar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChar" ):
                listener.exitChar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitChar" ):
                return visitor.visitChar(self)
            else:
                return visitor.visitChildren(self)


    class SizeOfContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a naiveCParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SIZEOF(self):
            return self.getToken(naiveCParser.SIZEOF, 0)
        def LeftParentheses(self):
            return self.getToken(naiveCParser.LeftParentheses, 0)
        def typeIdentifier(self):
            return self.getTypedRuleContext(naiveCParser.TypeIdentifierContext,0)

        def RightParentheses(self):
            return self.getToken(naiveCParser.RightParentheses, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSizeOf" ):
                listener.enterSizeOf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSizeOf" ):
                listener.exitSizeOf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSizeOf" ):
                return visitor.visitSizeOf(self)
            else:
                return visitor.visitChildren(self)


    class TypeCastContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a naiveCParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LeftParentheses(self):
            return self.getToken(naiveCParser.LeftParentheses, 0)
        def RightParentheses(self):
            return self.getToken(naiveCParser.RightParentheses, 0)
        def expr(self):
            return self.getTypedRuleContext(naiveCParser.ExprContext,0)

        def realTypeIDPointer(self):
            return self.getTypedRuleContext(naiveCParser.RealTypeIDPointerContext,0)

        def realTypeID(self):
            return self.getTypedRuleContext(naiveCParser.RealTypeIDContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeCast" ):
                listener.enterTypeCast(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeCast" ):
                listener.exitTypeCast(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeCast" ):
                return visitor.visitTypeCast(self)
            else:
                return visitor.visitChildren(self)


    class GetPContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a naiveCParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ArithmeticAnd(self):
            return self.getToken(naiveCParser.ArithmeticAnd, 0)
        def ID(self):
            return self.getToken(naiveCParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGetP" ):
                listener.enterGetP(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGetP" ):
                listener.exitGetP(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGetP" ):
                return visitor.visitGetP(self)
            else:
                return visitor.visitChildren(self)


    class IdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a naiveCParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(naiveCParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)


    class ArrayVisitContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a naiveCParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(naiveCParser.ID, 0)
        def LeftBracket(self):
            return self.getToken(naiveCParser.LeftBracket, 0)
        def expr(self):
            return self.getTypedRuleContext(naiveCParser.ExprContext,0)

        def RightBracket(self):
            return self.getToken(naiveCParser.RightBracket, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayVisit" ):
                listener.enterArrayVisit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayVisit" ):
                listener.exitArrayVisit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayVisit" ):
                return visitor.visitArrayVisit(self)
            else:
                return visitor.visitChildren(self)


    class MakPContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a naiveCParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MUL(self):
            return self.getToken(naiveCParser.MUL, 0)
        def expr(self):
            return self.getTypedRuleContext(naiveCParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMakP" ):
                listener.enterMakP(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMakP" ):
                listener.exitMakP(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMakP" ):
                return visitor.visitMakP(self)
            else:
                return visitor.visitChildren(self)


    class FCallContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a naiveCParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def functionCall(self):
            return self.getTypedRuleContext(naiveCParser.FunctionCallContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFCall" ):
                listener.enterFCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFCall" ):
                listener.exitFCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFCall" ):
                return visitor.visitFCall(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = naiveCParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                localctx = naiveCParser.TypeCastContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 94
                self.match(naiveCParser.LeftParentheses)
                self.state = 97
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 95
                    self.realTypeIDPointer()
                    pass

                elif la_ == 2:
                    self.state = 96
                    self.realTypeID()
                    pass


                self.state = 99
                self.match(naiveCParser.RightParentheses)
                self.state = 100
                self.expr(15)
                pass

            elif la_ == 2:
                localctx = naiveCParser.NegativeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 102
                self.match(naiveCParser.SUB)
                self.state = 103
                self.expr(14)
                pass

            elif la_ == 3:
                localctx = naiveCParser.MakPContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 104
                self.match(naiveCParser.MUL)
                self.state = 105
                self.expr(13)
                pass

            elif la_ == 4:
                localctx = naiveCParser.GetPContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 106
                self.match(naiveCParser.ArithmeticAnd)
                self.state = 107
                self.match(naiveCParser.ID)
                pass

            elif la_ == 5:
                localctx = naiveCParser.PositiveINTContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 108
                self.match(naiveCParser.PositiveINT)
                pass

            elif la_ == 6:
                localctx = naiveCParser.CharContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 109
                self.match(naiveCParser.Char)
                pass

            elif la_ == 7:
                localctx = naiveCParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 110
                self.match(naiveCParser.INT)
                pass

            elif la_ == 8:
                localctx = naiveCParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 111
                self.match(naiveCParser.ID)
                pass

            elif la_ == 9:
                localctx = naiveCParser.FCallContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 112
                self.functionCall()
                pass

            elif la_ == 10:
                localctx = naiveCParser.SizeOfContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 113
                self.match(naiveCParser.SIZEOF)
                self.state = 114
                self.match(naiveCParser.LeftParentheses)
                self.state = 115
                self.typeIdentifier()
                self.state = 116
                self.match(naiveCParser.RightParentheses)
                pass

            elif la_ == 11:
                localctx = naiveCParser.TrueFalseContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 118
                self.boolExpr()
                pass

            elif la_ == 12:
                localctx = naiveCParser.ArrayVisitContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 119
                self.match(naiveCParser.ID)
                self.state = 120
                self.match(naiveCParser.LeftBracket)
                self.state = 121
                self.expr(0)
                self.state = 122
                self.match(naiveCParser.RightBracket)
                pass

            elif la_ == 13:
                localctx = naiveCParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 124
                self.match(naiveCParser.LeftParentheses)
                self.state = 125
                self.expr(0)
                self.state = 126
                self.match(naiveCParser.RightParentheses)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 138
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 136
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = naiveCParser.MulDivContext(self, naiveCParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 130
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 131
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==naiveCParser.MUL or _la==naiveCParser.DIV):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 132
                        self.expr(3)
                        pass

                    elif la_ == 2:
                        localctx = naiveCParser.AddSubContext(self, naiveCParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 133
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 134
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==naiveCParser.ADD or _la==naiveCParser.SUB):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 135
                        self.expr(2)
                        pass

             
                self.state = 140
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ConditionOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Greater(self):
            return self.getToken(naiveCParser.Greater, 0)

        def GreaterEqual(self):
            return self.getToken(naiveCParser.GreaterEqual, 0)

        def Less(self):
            return self.getToken(naiveCParser.Less, 0)

        def LessEqual(self):
            return self.getToken(naiveCParser.LessEqual, 0)

        def Equal(self):
            return self.getToken(naiveCParser.Equal, 0)

        def NotEqual(self):
            return self.getToken(naiveCParser.NotEqual, 0)

        def getRuleIndex(self):
            return naiveCParser.RULE_conditionOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionOperator" ):
                listener.enterConditionOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionOperator" ):
                listener.exitConditionOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditionOperator" ):
                return visitor.visitConditionOperator(self)
            else:
                return visitor.visitChildren(self)




    def conditionOperator(self):

        localctx = naiveCParser.ConditionOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_conditionOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << naiveCParser.Greater) | (1 << naiveCParser.Less) | (1 << naiveCParser.GreaterEqual) | (1 << naiveCParser.LessEqual) | (1 << naiveCParser.Equal) | (1 << naiveCParser.NotEqual))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return naiveCParser.RULE_conditionExpr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class NegContext(ConditionExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a naiveCParser.ConditionExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Not(self):
            return self.getToken(naiveCParser.Not, 0)
        def conditionExpr(self):
            return self.getTypedRuleContext(naiveCParser.ConditionExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNeg" ):
                listener.enterNeg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNeg" ):
                listener.exitNeg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNeg" ):
                return visitor.visitNeg(self)
            else:
                return visitor.visitChildren(self)


    class CondExpContext(ConditionExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a naiveCParser.ConditionExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(naiveCParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondExp" ):
                listener.enterCondExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondExp" ):
                listener.exitCondExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondExp" ):
                return visitor.visitCondExp(self)
            else:
                return visitor.visitChildren(self)


    class OrContext(ConditionExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a naiveCParser.ConditionExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def conditionExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(naiveCParser.ConditionExprContext)
            else:
                return self.getTypedRuleContext(naiveCParser.ConditionExprContext,i)

        def LogicOR(self):
            return self.getToken(naiveCParser.LogicOR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOr" ):
                listener.enterOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOr" ):
                listener.exitOr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOr" ):
                return visitor.visitOr(self)
            else:
                return visitor.visitChildren(self)


    class AndContext(ConditionExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a naiveCParser.ConditionExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def conditionExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(naiveCParser.ConditionExprContext)
            else:
                return self.getTypedRuleContext(naiveCParser.ConditionExprContext,i)

        def LogicAnd(self):
            return self.getToken(naiveCParser.LogicAnd, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnd" ):
                listener.enterAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnd" ):
                listener.exitAnd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnd" ):
                return visitor.visitAnd(self)
            else:
                return visitor.visitChildren(self)


    class CondOpContext(ConditionExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a naiveCParser.ConditionExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(naiveCParser.ExprContext)
            else:
                return self.getTypedRuleContext(naiveCParser.ExprContext,i)

        def conditionOperator(self):
            return self.getTypedRuleContext(naiveCParser.ConditionOperatorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondOp" ):
                listener.enterCondOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondOp" ):
                listener.exitCondOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondOp" ):
                return visitor.visitCondOp(self)
            else:
                return visitor.visitChildren(self)


    class CondParenContext(ConditionExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a naiveCParser.ConditionExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LeftParentheses(self):
            return self.getToken(naiveCParser.LeftParentheses, 0)
        def conditionExpr(self):
            return self.getTypedRuleContext(naiveCParser.ConditionExprContext,0)

        def RightParentheses(self):
            return self.getToken(naiveCParser.RightParentheses, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondParen" ):
                listener.enterCondParen(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondParen" ):
                listener.exitCondParen(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondParen" ):
                return visitor.visitCondParen(self)
            else:
                return visitor.visitChildren(self)



    def conditionExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = naiveCParser.ConditionExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_conditionExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                localctx = naiveCParser.NegContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 144
                self.match(naiveCParser.Not)
                self.state = 145
                self.conditionExpr(6)
                pass

            elif la_ == 2:
                localctx = naiveCParser.CondParenContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 146
                self.match(naiveCParser.LeftParentheses)
                self.state = 147
                self.conditionExpr(0)
                self.state = 148
                self.match(naiveCParser.RightParentheses)
                pass

            elif la_ == 3:
                localctx = naiveCParser.CondOpContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 150
                self.expr(0)
                self.state = 151
                self.conditionOperator()
                self.state = 152
                self.expr(0)
                pass

            elif la_ == 4:
                localctx = naiveCParser.CondExpContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 154
                self.expr(0)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 165
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 163
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                    if la_ == 1:
                        localctx = naiveCParser.AndContext(self, naiveCParser.ConditionExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_conditionExpr)
                        self.state = 157
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 158
                        self.match(naiveCParser.LogicAnd)
                        self.state = 159
                        self.conditionExpr(6)
                        pass

                    elif la_ == 2:
                        localctx = naiveCParser.OrContext(self, naiveCParser.ConditionExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_conditionExpr)
                        self.state = 160
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 161
                        self.match(naiveCParser.LogicOR)
                        self.state = 162
                        self.conditionExpr(5)
                        pass

             
                self.state = 167
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return naiveCParser.RULE_assignment

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ArrayAssignContext(AssignmentContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a naiveCParser.AssignmentContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(naiveCParser.ID, 0)
        def LeftBracket(self):
            return self.getToken(naiveCParser.LeftBracket, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(naiveCParser.ExprContext)
            else:
                return self.getTypedRuleContext(naiveCParser.ExprContext,i)

        def RightBracket(self):
            return self.getToken(naiveCParser.RightBracket, 0)
        def AssignOperator(self):
            return self.getToken(naiveCParser.AssignOperator, 0)
        def Semicolon(self):
            return self.getToken(naiveCParser.Semicolon, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayAssign" ):
                listener.enterArrayAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayAssign" ):
                listener.exitArrayAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayAssign" ):
                return visitor.visitArrayAssign(self)
            else:
                return visitor.visitChildren(self)


    class MemoryAssignContext(AssignmentContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a naiveCParser.AssignmentContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MUL(self):
            return self.getToken(naiveCParser.MUL, 0)
        def ID(self):
            return self.getToken(naiveCParser.ID, 0)
        def AssignOperator(self):
            return self.getToken(naiveCParser.AssignOperator, 0)
        def expr(self):
            return self.getTypedRuleContext(naiveCParser.ExprContext,0)

        def Semicolon(self):
            return self.getToken(naiveCParser.Semicolon, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMemoryAssign" ):
                listener.enterMemoryAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMemoryAssign" ):
                listener.exitMemoryAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMemoryAssign" ):
                return visitor.visitMemoryAssign(self)
            else:
                return visitor.visitChildren(self)


    class CommonAssignContext(AssignmentContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a naiveCParser.AssignmentContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(naiveCParser.ID, 0)
        def AssignOperator(self):
            return self.getToken(naiveCParser.AssignOperator, 0)
        def expr(self):
            return self.getTypedRuleContext(naiveCParser.ExprContext,0)

        def Semicolon(self):
            return self.getToken(naiveCParser.Semicolon, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommonAssign" ):
                listener.enterCommonAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommonAssign" ):
                listener.exitCommonAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommonAssign" ):
                return visitor.visitCommonAssign(self)
            else:
                return visitor.visitChildren(self)



    def assignment(self):

        localctx = naiveCParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_assignment)
        try:
            self.state = 187
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                localctx = naiveCParser.CommonAssignContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 168
                self.match(naiveCParser.ID)
                self.state = 169
                self.match(naiveCParser.AssignOperator)
                self.state = 170
                self.expr(0)
                self.state = 171
                self.match(naiveCParser.Semicolon)
                pass

            elif la_ == 2:
                localctx = naiveCParser.MemoryAssignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 173
                self.match(naiveCParser.MUL)
                self.state = 174
                self.match(naiveCParser.ID)
                self.state = 175
                self.match(naiveCParser.AssignOperator)
                self.state = 176
                self.expr(0)
                self.state = 177
                self.match(naiveCParser.Semicolon)
                pass

            elif la_ == 3:
                localctx = naiveCParser.ArrayAssignContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 179
                self.match(naiveCParser.ID)
                self.state = 180
                self.match(naiveCParser.LeftBracket)
                self.state = 181
                self.expr(0)
                self.state = 182
                self.match(naiveCParser.RightBracket)
                self.state = 183
                self.match(naiveCParser.AssignOperator)
                self.state = 184
                self.expr(0)
                self.state = 185
                self.match(naiveCParser.Semicolon)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(naiveCParser.ID, 0)

        def Semicolon(self):
            return self.getToken(naiveCParser.Semicolon, 0)

        def realTypeID(self):
            return self.getTypedRuleContext(naiveCParser.RealTypeIDContext,0)


        def realTypeIDPointer(self):
            return self.getTypedRuleContext(naiveCParser.RealTypeIDPointerContext,0)


        def AssignOperator(self):
            return self.getToken(naiveCParser.AssignOperator, 0)

        def expr(self):
            return self.getTypedRuleContext(naiveCParser.ExprContext,0)


        def LeftBracket(self):
            return self.getToken(naiveCParser.LeftBracket, 0)

        def PositiveINT(self):
            return self.getToken(naiveCParser.PositiveINT, 0)

        def RightBracket(self):
            return self.getToken(naiveCParser.RightBracket, 0)

        def getRuleIndex(self):
            return naiveCParser.RULE_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefinition" ):
                listener.enterDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefinition" ):
                listener.exitDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefinition" ):
                return visitor.visitDefinition(self)
            else:
                return visitor.visitChildren(self)




    def definition(self):

        localctx = naiveCParser.DefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_definition)
        self._la = 0 # Token type
        try:
            self.state = 210
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 191
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                if la_ == 1:
                    self.state = 189
                    self.realTypeID()
                    pass

                elif la_ == 2:
                    self.state = 190
                    self.realTypeIDPointer()
                    pass


                self.state = 193
                self.match(naiveCParser.ID)
                self.state = 196
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==naiveCParser.AssignOperator:
                    self.state = 194
                    self.match(naiveCParser.AssignOperator)
                    self.state = 195
                    self.expr(0)


                self.state = 198
                self.match(naiveCParser.Semicolon)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 202
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                if la_ == 1:
                    self.state = 200
                    self.realTypeID()
                    pass

                elif la_ == 2:
                    self.state = 201
                    self.realTypeIDPointer()
                    pass


                self.state = 204
                self.match(naiveCParser.ID)
                self.state = 205
                self.match(naiveCParser.LeftBracket)
                self.state = 206
                self.match(naiveCParser.PositiveINT)
                self.state = 207
                self.match(naiveCParser.RightBracket)
                self.state = 208
                self.match(naiveCParser.Semicolon)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallProcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionCall(self):
            return self.getTypedRuleContext(naiveCParser.FunctionCallContext,0)


        def Semicolon(self):
            return self.getToken(naiveCParser.Semicolon, 0)

        def getRuleIndex(self):
            return naiveCParser.RULE_callProc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCallProc" ):
                listener.enterCallProc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCallProc" ):
                listener.exitCallProc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallProc" ):
                return visitor.visitCallProc(self)
            else:
                return visitor.visitChildren(self)




    def callProc(self):

        localctx = naiveCParser.CallProcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_callProc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.functionCall()
            self.state = 213
            self.match(naiveCParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnLineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Return(self):
            return self.getToken(naiveCParser.Return, 0)

        def Semicolon(self):
            return self.getToken(naiveCParser.Semicolon, 0)

        def expr(self):
            return self.getTypedRuleContext(naiveCParser.ExprContext,0)


        def getRuleIndex(self):
            return naiveCParser.RULE_returnLine

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnLine" ):
                listener.enterReturnLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnLine" ):
                listener.exitReturnLine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnLine" ):
                return visitor.visitReturnLine(self)
            else:
                return visitor.visitChildren(self)




    def returnLine(self):

        localctx = naiveCParser.ReturnLineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_returnLine)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.match(naiveCParser.Return)
            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << naiveCParser.SUB) | (1 << naiveCParser.MUL) | (1 << naiveCParser.ArithmeticAnd) | (1 << naiveCParser.LeftParentheses) | (1 << naiveCParser.TRUE) | (1 << naiveCParser.FALSE) | (1 << naiveCParser.SIZEOF) | (1 << naiveCParser.PositiveINT) | (1 << naiveCParser.Char) | (1 << naiveCParser.INT) | (1 << naiveCParser.ID))) != 0):
                self.state = 216
                self.expr(0)


            self.state = 219
            self.match(naiveCParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return naiveCParser.RULE_param

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ParamExprContext(ParamContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a naiveCParser.ParamContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(naiveCParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamExpr" ):
                listener.enterParamExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamExpr" ):
                listener.exitParamExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamExpr" ):
                return visitor.visitParamExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParamFuncContext(ParamContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a naiveCParser.ParamContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def functionCall(self):
            return self.getTypedRuleContext(naiveCParser.FunctionCallContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamFunc" ):
                listener.enterParamFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamFunc" ):
                listener.exitParamFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamFunc" ):
                return visitor.visitParamFunc(self)
            else:
                return visitor.visitChildren(self)


    class ParamStringContext(ParamContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a naiveCParser.ParamContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def String(self):
            return self.getToken(naiveCParser.String, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamString" ):
                listener.enterParamString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamString" ):
                listener.exitParamString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamString" ):
                return visitor.visitParamString(self)
            else:
                return visitor.visitChildren(self)



    def param(self):

        localctx = naiveCParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_param)
        try:
            self.state = 224
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                localctx = naiveCParser.ParamExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self.expr(0)
                pass

            elif la_ == 2:
                localctx = naiveCParser.ParamFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 222
                self.functionCall()
                pass

            elif la_ == 3:
                localctx = naiveCParser.ParamStringContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 223
                self.match(naiveCParser.String)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(naiveCParser.ParamContext,0)


        def paramList(self):
            return self.getTypedRuleContext(naiveCParser.ParamListContext,0)


        def getRuleIndex(self):
            return naiveCParser.RULE_paramList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamList" ):
                listener.enterParamList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamList" ):
                listener.exitParamList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamList" ):
                return visitor.visitParamList(self)
            else:
                return visitor.visitChildren(self)



    def paramList(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = naiveCParser.ParamListContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_paramList, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 227
                self.param()


            self._ctx.stop = self._input.LT(-1)
            self.state = 235
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = naiveCParser.ParamListContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_paramList)
                    self.state = 230
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 231
                    self.match(naiveCParser.T__0)
                    self.state = 232
                    self.param() 
                self.state = 237
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class DefineParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(naiveCParser.ID, 0)

        def typeIdentifier(self):
            return self.getTypedRuleContext(naiveCParser.TypeIdentifierContext,0)


        def typeIdentifierPointer(self):
            return self.getTypedRuleContext(naiveCParser.TypeIdentifierPointerContext,0)


        def getRuleIndex(self):
            return naiveCParser.RULE_defineParam

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefineParam" ):
                listener.enterDefineParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefineParam" ):
                listener.exitDefineParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefineParam" ):
                return visitor.visitDefineParam(self)
            else:
                return visitor.visitChildren(self)




    def defineParam(self):

        localctx = naiveCParser.DefineParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_defineParam)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 238
                self.typeIdentifier()
                pass

            elif la_ == 2:
                self.state = 239
                self.typeIdentifierPointer()
                pass


            self.state = 242
            self.match(naiveCParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefineParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def defineParam(self):
            return self.getTypedRuleContext(naiveCParser.DefineParamContext,0)


        def defineParamList(self):
            return self.getTypedRuleContext(naiveCParser.DefineParamListContext,0)


        def getRuleIndex(self):
            return naiveCParser.RULE_defineParamList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefineParamList" ):
                listener.enterDefineParamList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefineParamList" ):
                listener.exitDefineParamList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefineParamList" ):
                return visitor.visitDefineParamList(self)
            else:
                return visitor.visitChildren(self)



    def defineParamList(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = naiveCParser.DefineParamListContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_defineParamList, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 245
                self.defineParam()


            self._ctx.stop = self._input.LT(-1)
            self.state = 253
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = naiveCParser.DefineParamListContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_defineParamList)
                    self.state = 248
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 249
                    self.match(naiveCParser.T__0)
                    self.state = 250
                    self.defineParam() 
                self.state = 255
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LeftBrace(self):
            return self.getToken(naiveCParser.LeftBrace, 0)

        def statements(self):
            return self.getTypedRuleContext(naiveCParser.StatementsContext,0)


        def RightBrace(self):
            return self.getToken(naiveCParser.RightBrace, 0)

        def getRuleIndex(self):
            return naiveCParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = naiveCParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.match(naiveCParser.LeftBrace)
            self.state = 257
            self.statements()
            self.state = 258
            self.match(naiveCParser.RightBrace)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakLineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Break(self):
            return self.getToken(naiveCParser.Break, 0)

        def Semicolon(self):
            return self.getToken(naiveCParser.Semicolon, 0)

        def getRuleIndex(self):
            return naiveCParser.RULE_breakLine

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreakLine" ):
                listener.enterBreakLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreakLine" ):
                listener.exitBreakLine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakLine" ):
                return visitor.visitBreakLine(self)
            else:
                return visitor.visitChildren(self)




    def breakLine(self):

        localctx = naiveCParser.BreakLineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_breakLine)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.match(naiveCParser.Break)
            self.state = 261
            self.match(naiveCParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueLineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Continue(self):
            return self.getToken(naiveCParser.Continue, 0)

        def Semicolon(self):
            return self.getToken(naiveCParser.Semicolon, 0)

        def getRuleIndex(self):
            return naiveCParser.RULE_continueLine

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinueLine" ):
                listener.enterContinueLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinueLine" ):
                listener.exitContinueLine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinueLine" ):
                return visitor.visitContinueLine(self)
            else:
                return visitor.visitChildren(self)




    def continueLine(self):

        localctx = naiveCParser.ContinueLineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_continueLine)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.match(naiveCParser.Continue)
            self.state = 264
            self.match(naiveCParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(naiveCParser.AssignmentContext)
            else:
                return self.getTypedRuleContext(naiveCParser.AssignmentContext,i)


        def definition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(naiveCParser.DefinitionContext)
            else:
                return self.getTypedRuleContext(naiveCParser.DefinitionContext,i)


        def callProc(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(naiveCParser.CallProcContext)
            else:
                return self.getTypedRuleContext(naiveCParser.CallProcContext,i)


        def whileBlock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(naiveCParser.WhileBlockContext)
            else:
                return self.getTypedRuleContext(naiveCParser.WhileBlockContext,i)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(naiveCParser.BlockContext)
            else:
                return self.getTypedRuleContext(naiveCParser.BlockContext,i)


        def ifBlock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(naiveCParser.IfBlockContext)
            else:
                return self.getTypedRuleContext(naiveCParser.IfBlockContext,i)


        def returnLine(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(naiveCParser.ReturnLineContext)
            else:
                return self.getTypedRuleContext(naiveCParser.ReturnLineContext,i)


        def breakLine(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(naiveCParser.BreakLineContext)
            else:
                return self.getTypedRuleContext(naiveCParser.BreakLineContext,i)


        def continueLine(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(naiveCParser.ContinueLineContext)
            else:
                return self.getTypedRuleContext(naiveCParser.ContinueLineContext,i)


        def getRuleIndex(self):
            return naiveCParser.RULE_statements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatements" ):
                listener.enterStatements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatements" ):
                listener.exitStatements(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatements" ):
                return visitor.visitStatements(self)
            else:
                return visitor.visitChildren(self)




    def statements(self):

        localctx = naiveCParser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_statements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << naiveCParser.TypeInt) | (1 << naiveCParser.TypeChar) | (1 << naiveCParser.TypeLL) | (1 << naiveCParser.TypeDouble) | (1 << naiveCParser.Break) | (1 << naiveCParser.Continue) | (1 << naiveCParser.If) | (1 << naiveCParser.Return) | (1 << naiveCParser.While) | (1 << naiveCParser.MUL) | (1 << naiveCParser.LeftBrace) | (1 << naiveCParser.ID))) != 0):
                self.state = 275
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                if la_ == 1:
                    self.state = 266
                    self.assignment()
                    pass

                elif la_ == 2:
                    self.state = 267
                    self.definition()
                    pass

                elif la_ == 3:
                    self.state = 268
                    self.callProc()
                    pass

                elif la_ == 4:
                    self.state = 269
                    self.whileBlock()
                    pass

                elif la_ == 5:
                    self.state = 270
                    self.block()
                    pass

                elif la_ == 6:
                    self.state = 271
                    self.ifBlock()
                    pass

                elif la_ == 7:
                    self.state = 272
                    self.returnLine()
                    pass

                elif la_ == 8:
                    self.state = 273
                    self.breakLine()
                    pass

                elif la_ == 9:
                    self.state = 274
                    self.continueLine()
                    pass


                self.state = 279
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def While(self):
            return self.getToken(naiveCParser.While, 0)

        def LeftParentheses(self):
            return self.getToken(naiveCParser.LeftParentheses, 0)

        def conditionExpr(self):
            return self.getTypedRuleContext(naiveCParser.ConditionExprContext,0)


        def RightParentheses(self):
            return self.getToken(naiveCParser.RightParentheses, 0)

        def block(self):
            return self.getTypedRuleContext(naiveCParser.BlockContext,0)


        def getRuleIndex(self):
            return naiveCParser.RULE_whileBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileBlock" ):
                listener.enterWhileBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileBlock" ):
                listener.exitWhileBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileBlock" ):
                return visitor.visitWhileBlock(self)
            else:
                return visitor.visitChildren(self)




    def whileBlock(self):

        localctx = naiveCParser.WhileBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_whileBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.match(naiveCParser.While)
            self.state = 281
            self.match(naiveCParser.LeftParentheses)
            self.state = 282
            self.conditionExpr(0)
            self.state = 283
            self.match(naiveCParser.RightParentheses)
            self.state = 284
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.elif_cond = None # ConditionExprContext
            self.else_block = None # BlockContext

        def If(self, i:int=None):
            if i is None:
                return self.getTokens(naiveCParser.If)
            else:
                return self.getToken(naiveCParser.If, i)

        def LeftParentheses(self, i:int=None):
            if i is None:
                return self.getTokens(naiveCParser.LeftParentheses)
            else:
                return self.getToken(naiveCParser.LeftParentheses, i)

        def conditionExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(naiveCParser.ConditionExprContext)
            else:
                return self.getTypedRuleContext(naiveCParser.ConditionExprContext,i)


        def RightParentheses(self, i:int=None):
            if i is None:
                return self.getTokens(naiveCParser.RightParentheses)
            else:
                return self.getToken(naiveCParser.RightParentheses, i)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(naiveCParser.BlockContext)
            else:
                return self.getTypedRuleContext(naiveCParser.BlockContext,i)


        def Else(self, i:int=None):
            if i is None:
                return self.getTokens(naiveCParser.Else)
            else:
                return self.getToken(naiveCParser.Else, i)

        def getRuleIndex(self):
            return naiveCParser.RULE_ifBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfBlock" ):
                listener.enterIfBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfBlock" ):
                listener.exitIfBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfBlock" ):
                return visitor.visitIfBlock(self)
            else:
                return visitor.visitChildren(self)




    def ifBlock(self):

        localctx = naiveCParser.IfBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_ifBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.match(naiveCParser.If)
            self.state = 287
            self.match(naiveCParser.LeftParentheses)
            self.state = 288
            self.conditionExpr(0)
            self.state = 289
            self.match(naiveCParser.RightParentheses)
            self.state = 290
            self.block()
            self.state = 300
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 291
                    self.match(naiveCParser.Else)
                    self.state = 292
                    self.match(naiveCParser.If)
                    self.state = 293
                    self.match(naiveCParser.LeftParentheses)
                    self.state = 294
                    localctx.elif_cond = self.conditionExpr(0)
                    self.state = 295
                    self.match(naiveCParser.RightParentheses)
                    self.state = 296
                    self.block() 
                self.state = 302
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

            self.state = 305
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==naiveCParser.Else:
                self.state = 303
                self.match(naiveCParser.Else)
                self.state = 304
                localctx.else_block = self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(naiveCParser.ID, 0)

        def LeftParentheses(self):
            return self.getToken(naiveCParser.LeftParentheses, 0)

        def paramList(self):
            return self.getTypedRuleContext(naiveCParser.ParamListContext,0)


        def RightParentheses(self):
            return self.getToken(naiveCParser.RightParentheses, 0)

        def getRuleIndex(self):
            return naiveCParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = naiveCParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_functionCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.match(naiveCParser.ID)
            self.state = 308
            self.match(naiveCParser.LeftParentheses)
            self.state = 309
            self.paramList(0)
            self.state = 310
            self.match(naiveCParser.RightParentheses)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(naiveCParser.ID, 0)

        def LeftParentheses(self):
            return self.getToken(naiveCParser.LeftParentheses, 0)

        def defineParamList(self):
            return self.getTypedRuleContext(naiveCParser.DefineParamListContext,0)


        def RightParentheses(self):
            return self.getToken(naiveCParser.RightParentheses, 0)

        def Semicolon(self):
            return self.getToken(naiveCParser.Semicolon, 0)

        def typeIdentifier(self):
            return self.getTypedRuleContext(naiveCParser.TypeIdentifierContext,0)


        def typeIdentifierPointer(self):
            return self.getTypedRuleContext(naiveCParser.TypeIdentifierPointerContext,0)


        def getRuleIndex(self):
            return naiveCParser.RULE_functionDeclare

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDeclare" ):
                listener.enterFunctionDeclare(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDeclare" ):
                listener.exitFunctionDeclare(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDeclare" ):
                return visitor.visitFunctionDeclare(self)
            else:
                return visitor.visitChildren(self)




    def functionDeclare(self):

        localctx = naiveCParser.FunctionDeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_functionDeclare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 312
                self.typeIdentifier()
                pass

            elif la_ == 2:
                self.state = 313
                self.typeIdentifierPointer()
                pass


            self.state = 316
            self.match(naiveCParser.ID)
            self.state = 317
            self.match(naiveCParser.LeftParentheses)
            self.state = 318
            self.defineParamList(0)
            self.state = 319
            self.match(naiveCParser.RightParentheses)
            self.state = 320
            self.match(naiveCParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDefineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(naiveCParser.ID, 0)

        def LeftParentheses(self):
            return self.getToken(naiveCParser.LeftParentheses, 0)

        def defineParamList(self):
            return self.getTypedRuleContext(naiveCParser.DefineParamListContext,0)


        def RightParentheses(self):
            return self.getToken(naiveCParser.RightParentheses, 0)

        def block(self):
            return self.getTypedRuleContext(naiveCParser.BlockContext,0)


        def typeIdentifier(self):
            return self.getTypedRuleContext(naiveCParser.TypeIdentifierContext,0)


        def typeIdentifierPointer(self):
            return self.getTypedRuleContext(naiveCParser.TypeIdentifierPointerContext,0)


        def getRuleIndex(self):
            return naiveCParser.RULE_functionDefine

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDefine" ):
                listener.enterFunctionDefine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDefine" ):
                listener.exitFunctionDefine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDefine" ):
                return visitor.visitFunctionDefine(self)
            else:
                return visitor.visitChildren(self)




    def functionDefine(self):

        localctx = naiveCParser.FunctionDefineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_functionDefine)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 322
                self.typeIdentifier()
                pass

            elif la_ == 2:
                self.state = 323
                self.typeIdentifierPointer()
                pass


            self.state = 326
            self.match(naiveCParser.ID)
            self.state = 327
            self.match(naiveCParser.LeftParentheses)
            self.state = 328
            self.defineParamList(0)
            self.state = 329
            self.match(naiveCParser.RightParentheses)
            self.state = 330
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.r_sempred
        self._predicates[8] = self.expr_sempred
        self._predicates[10] = self.conditionExpr_sempred
        self._predicates[16] = self.paramList_sempred
        self._predicates[18] = self.defineParamList_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def r_sempred(self, localctx:RContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 1)
         

    def conditionExpr_sempred(self, localctx:ConditionExprContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 4)
         

    def paramList_sempred(self, localctx:ParamListContext, predIndex:int):
            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         

    def defineParamList_sempred(self, localctx:DefineParamListContext, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 2)
         




