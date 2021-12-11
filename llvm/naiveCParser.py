# Generated from E:/Tsinghua/课程/大三上/汇编与编译原理/作业/编译/编译小组作业/src/LLVM/antlr/src\naiveC.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\63")
        buf.write("\u0157\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\3\2\3\2\3\3\3\3\3\3\3\3\5\3E\n\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\7\3M\n\3\f\3\16\3P\13\3\3\4\3\4\3\5\3\5")
        buf.write("\3\5\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3")
        buf.write("\n\5\nd\n\n\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\5\fr\n\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u0086\n\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\7\f\u008e\n\f\f\f\16\f\u0091\13\f")
        buf.write("\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\5\16\u009f\n\16\3\16\3\16\3\16\3\16\3\16\3\16\7")
        buf.write("\16\u00a7\n\16\f\16\16\16\u00aa\13\16\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\5\17\u00bf\n\17\3\20\3\20\5")
        buf.write("\20\u00c3\n\20\3\20\3\20\3\20\5\20\u00c8\n\20\3\20\3\20")
        buf.write("\3\20\3\20\5\20\u00ce\n\20\3\20\3\20\3\20\3\20\3\20\3")
        buf.write("\20\5\20\u00d6\n\20\3\21\3\21\3\21\3\22\3\22\5\22\u00dd")
        buf.write("\n\22\3\22\3\22\3\23\3\23\3\23\5\23\u00e4\n\23\3\24\3")
        buf.write("\24\5\24\u00e8\n\24\3\24\3\24\3\24\7\24\u00ed\n\24\f\24")
        buf.write("\16\24\u00f0\13\24\3\25\3\25\5\25\u00f4\n\25\3\25\3\25")
        buf.write("\3\26\3\26\5\26\u00fa\n\26\3\26\3\26\3\26\7\26\u00ff\n")
        buf.write("\26\f\26\16\26\u0102\13\26\3\27\3\27\3\27\3\27\3\30\3")
        buf.write("\30\3\30\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\7\32\u0117\n\32\f\32\16\32\u011a\13\32")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\7\34\u012e\n\34\f")
        buf.write("\34\16\34\u0131\13\34\3\34\3\34\5\34\u0135\n\34\3\35\3")
        buf.write("\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\5\35\u0141")
        buf.write("\n\35\3\36\3\36\5\36\u0145\n\36\3\36\3\36\3\36\3\36\3")
        buf.write("\36\3\36\3\37\3\37\5\37\u014f\n\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\2\7\4\26\32&* \2\4\6\b\n\f\16\20\22\24")
        buf.write("\26\30\32\34\36 \"$&(*,.\60\62\64\668:<\2\t\4\2\6\6\b")
        buf.write("\t\3\2\6\t\3\2*+\5\2\20\20\23\26\37 \3\2\24\25\4\2\20")
        buf.write("\20\23\23\3\2\27\33\2\u016c\2>\3\2\2\2\4D\3\2\2\2\6Q\3")
        buf.write("\2\2\2\bS\3\2\2\2\nV\3\2\2\2\fX\3\2\2\2\16[\3\2\2\2\20")
        buf.write("]\3\2\2\2\22c\3\2\2\2\24e\3\2\2\2\26\u0085\3\2\2\2\30")
        buf.write("\u0092\3\2\2\2\32\u009e\3\2\2\2\34\u00be\3\2\2\2\36\u00d5")
        buf.write("\3\2\2\2 \u00d7\3\2\2\2\"\u00da\3\2\2\2$\u00e3\3\2\2\2")
        buf.write("&\u00e5\3\2\2\2(\u00f3\3\2\2\2*\u00f7\3\2\2\2,\u0103\3")
        buf.write("\2\2\2.\u0107\3\2\2\2\60\u010a\3\2\2\2\62\u0118\3\2\2")
        buf.write("\2\64\u011b\3\2\2\2\66\u0121\3\2\2\28\u0140\3\2\2\2:\u0144")
        buf.write("\3\2\2\2<\u014e\3\2\2\2>?\5\4\3\2?\3\3\2\2\2@A\b\3\1\2")
        buf.write("AE\58\35\2BE\5:\36\2CE\5<\37\2D@\3\2\2\2DB\3\2\2\2DC\3")
        buf.write("\2\2\2EN\3\2\2\2FG\f\5\2\2GM\58\35\2HI\f\4\2\2IM\5<\37")
        buf.write("\2JK\f\3\2\2KM\5:\36\2LF\3\2\2\2LH\3\2\2\2LJ\3\2\2\2M")
        buf.write("P\3\2\2\2NL\3\2\2\2NO\3\2\2\2O\5\3\2\2\2PN\3\2\2\2QR\t")
        buf.write("\2\2\2R\7\3\2\2\2ST\5\6\4\2TU\7\24\2\2U\t\3\2\2\2VW\t")
        buf.write("\3\2\2W\13\3\2\2\2XY\5\n\6\2YZ\7\24\2\2Z\r\3\2\2\2[\\")
        buf.write("\7\3\2\2\\\17\3\2\2\2]^\t\4\2\2^\21\3\2\2\2_`\7/\2\2`")
        buf.write("a\7\4\2\2ad\5\22\n\2bd\7/\2\2c_\3\2\2\2cb\3\2\2\2d\23")
        buf.write("\3\2\2\2ef\t\5\2\2f\25\3\2\2\2gh\b\f\1\2hi\7\37\2\2i\u0086")
        buf.write("\7/\2\2jk\7\24\2\2k\u0086\5\26\f\rlm\7\23\2\2m\u0086\5")
        buf.write("\26\f\fnq\7$\2\2or\5\b\5\2pr\5\6\4\2qo\3\2\2\2qp\3\2\2")
        buf.write("\2rs\3\2\2\2st\7%\2\2tu\5\26\f\13u\u0086\3\2\2\2v\u0086")
        buf.write("\7,\2\2w\u0086\7-\2\2x\u0086\7.\2\2y\u0086\7/\2\2z\u0086")
        buf.write("\58\35\2{\u0086\5\20\t\2|}\7/\2\2}~\7&\2\2~\177\5\26\f")
        buf.write("\2\177\u0080\7\'\2\2\u0080\u0086\3\2\2\2\u0081\u0082\7")
        buf.write("$\2\2\u0082\u0083\5\26\f\2\u0083\u0084\7%\2\2\u0084\u0086")
        buf.write("\3\2\2\2\u0085g\3\2\2\2\u0085j\3\2\2\2\u0085l\3\2\2\2")
        buf.write("\u0085n\3\2\2\2\u0085v\3\2\2\2\u0085w\3\2\2\2\u0085x\3")
        buf.write("\2\2\2\u0085y\3\2\2\2\u0085z\3\2\2\2\u0085{\3\2\2\2\u0085")
        buf.write("|\3\2\2\2\u0085\u0081\3\2\2\2\u0086\u008f\3\2\2\2\u0087")
        buf.write("\u0088\f\20\2\2\u0088\u0089\t\6\2\2\u0089\u008e\5\26\f")
        buf.write("\21\u008a\u008b\f\17\2\2\u008b\u008c\t\7\2\2\u008c\u008e")
        buf.write("\5\26\f\20\u008d\u0087\3\2\2\2\u008d\u008a\3\2\2\2\u008e")
        buf.write("\u0091\3\2\2\2\u008f\u008d\3\2\2\2\u008f\u0090\3\2\2\2")
        buf.write("\u0090\27\3\2\2\2\u0091\u008f\3\2\2\2\u0092\u0093\t\b")
        buf.write("\2\2\u0093\31\3\2\2\2\u0094\u0095\b\16\1\2\u0095\u0096")
        buf.write("\7$\2\2\u0096\u0097\5\32\16\2\u0097\u0098\7%\2\2\u0098")
        buf.write("\u009f\3\2\2\2\u0099\u009a\5\26\f\2\u009a\u009b\5\30\r")
        buf.write("\2\u009b\u009c\5\26\f\2\u009c\u009f\3\2\2\2\u009d\u009f")
        buf.write("\5\26\f\2\u009e\u0094\3\2\2\2\u009e\u0099\3\2\2\2\u009e")
        buf.write("\u009d\3\2\2\2\u009f\u00a8\3\2\2\2\u00a0\u00a1\f\7\2\2")
        buf.write("\u00a1\u00a2\7!\2\2\u00a2\u00a7\5\32\16\b\u00a3\u00a4")
        buf.write("\f\6\2\2\u00a4\u00a5\7\"\2\2\u00a5\u00a7\5\32\16\7\u00a6")
        buf.write("\u00a0\3\2\2\2\u00a6\u00a3\3\2\2\2\u00a7\u00aa\3\2\2\2")
        buf.write("\u00a8\u00a6\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\33\3\2")
        buf.write("\2\2\u00aa\u00a8\3\2\2\2\u00ab\u00ac\7/\2\2\u00ac\u00ad")
        buf.write("\7\36\2\2\u00ad\u00ae\5\26\f\2\u00ae\u00af\7#\2\2\u00af")
        buf.write("\u00bf\3\2\2\2\u00b0\u00b1\7\24\2\2\u00b1\u00b2\7/\2\2")
        buf.write("\u00b2\u00b3\7\36\2\2\u00b3\u00b4\5\26\f\2\u00b4\u00b5")
        buf.write("\7#\2\2\u00b5\u00bf\3\2\2\2\u00b6\u00b7\7/\2\2\u00b7\u00b8")
        buf.write("\7&\2\2\u00b8\u00b9\5\26\f\2\u00b9\u00ba\7\'\2\2\u00ba")
        buf.write("\u00bb\7\36\2\2\u00bb\u00bc\5\26\f\2\u00bc\u00bd\7#\2")
        buf.write("\2\u00bd\u00bf\3\2\2\2\u00be\u00ab\3\2\2\2\u00be\u00b0")
        buf.write("\3\2\2\2\u00be\u00b6\3\2\2\2\u00bf\35\3\2\2\2\u00c0\u00c3")
        buf.write("\5\6\4\2\u00c1\u00c3\5\b\5\2\u00c2\u00c0\3\2\2\2\u00c2")
        buf.write("\u00c1\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4\u00c7\7/\2\2")
        buf.write("\u00c5\u00c6\7\36\2\2\u00c6\u00c8\5\26\f\2\u00c7\u00c5")
        buf.write("\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8\u00c9\3\2\2\2\u00c9")
        buf.write("\u00ca\7#\2\2\u00ca\u00d6\3\2\2\2\u00cb\u00ce\5\6\4\2")
        buf.write("\u00cc\u00ce\5\b\5\2\u00cd\u00cb\3\2\2\2\u00cd\u00cc\3")
        buf.write("\2\2\2\u00ce\u00cf\3\2\2\2\u00cf\u00d0\7/\2\2\u00d0\u00d1")
        buf.write("\7&\2\2\u00d1\u00d2\7,\2\2\u00d2\u00d3\7\'\2\2\u00d3\u00d4")
        buf.write("\7#\2\2\u00d4\u00d6\3\2\2\2\u00d5\u00c2\3\2\2\2\u00d5")
        buf.write("\u00cd\3\2\2\2\u00d6\37\3\2\2\2\u00d7\u00d8\58\35\2\u00d8")
        buf.write("\u00d9\7#\2\2\u00d9!\3\2\2\2\u00da\u00dc\7\16\2\2\u00db")
        buf.write("\u00dd\5\26\f\2\u00dc\u00db\3\2\2\2\u00dc\u00dd\3\2\2")
        buf.write("\2\u00dd\u00de\3\2\2\2\u00de\u00df\7#\2\2\u00df#\3\2\2")
        buf.write("\2\u00e0\u00e4\5\26\f\2\u00e1\u00e4\58\35\2\u00e2\u00e4")
        buf.write("\7\63\2\2\u00e3\u00e0\3\2\2\2\u00e3\u00e1\3\2\2\2\u00e3")
        buf.write("\u00e2\3\2\2\2\u00e4%\3\2\2\2\u00e5\u00e7\b\24\1\2\u00e6")
        buf.write("\u00e8\5$\23\2\u00e7\u00e6\3\2\2\2\u00e7\u00e8\3\2\2\2")
        buf.write("\u00e8\u00ee\3\2\2\2\u00e9\u00ea\f\4\2\2\u00ea\u00eb\7")
        buf.write("\4\2\2\u00eb\u00ed\5$\23\2\u00ec\u00e9\3\2\2\2\u00ed\u00f0")
        buf.write("\3\2\2\2\u00ee\u00ec\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef")
        buf.write("\'\3\2\2\2\u00f0\u00ee\3\2\2\2\u00f1\u00f4\5\n\6\2\u00f2")
        buf.write("\u00f4\5\f\7\2\u00f3\u00f1\3\2\2\2\u00f3\u00f2\3\2\2\2")
        buf.write("\u00f4\u00f5\3\2\2\2\u00f5\u00f6\7/\2\2\u00f6)\3\2\2\2")
        buf.write("\u00f7\u00f9\b\26\1\2\u00f8\u00fa\5(\25\2\u00f9\u00f8")
        buf.write("\3\2\2\2\u00f9\u00fa\3\2\2\2\u00fa\u0100\3\2\2\2\u00fb")
        buf.write("\u00fc\f\4\2\2\u00fc\u00fd\7\4\2\2\u00fd\u00ff\5(\25\2")
        buf.write("\u00fe\u00fb\3\2\2\2\u00ff\u0102\3\2\2\2\u0100\u00fe\3")
        buf.write("\2\2\2\u0100\u0101\3\2\2\2\u0101+\3\2\2\2\u0102\u0100")
        buf.write("\3\2\2\2\u0103\u0104\7(\2\2\u0104\u0105\5\62\32\2\u0105")
        buf.write("\u0106\7)\2\2\u0106-\3\2\2\2\u0107\u0108\7\n\2\2\u0108")
        buf.write("\u0109\7#\2\2\u0109/\3\2\2\2\u010a\u010b\7\13\2\2\u010b")
        buf.write("\u010c\7#\2\2\u010c\61\3\2\2\2\u010d\u0117\5\34\17\2\u010e")
        buf.write("\u0117\5\36\20\2\u010f\u0117\5 \21\2\u0110\u0117\5\64")
        buf.write("\33\2\u0111\u0117\5,\27\2\u0112\u0117\5\66\34\2\u0113")
        buf.write("\u0117\5\"\22\2\u0114\u0117\5.\30\2\u0115\u0117\5\60\31")
        buf.write("\2\u0116\u010d\3\2\2\2\u0116\u010e\3\2\2\2\u0116\u010f")
        buf.write("\3\2\2\2\u0116\u0110\3\2\2\2\u0116\u0111\3\2\2\2\u0116")
        buf.write("\u0112\3\2\2\2\u0116\u0113\3\2\2\2\u0116\u0114\3\2\2\2")
        buf.write("\u0116\u0115\3\2\2\2\u0117\u011a\3\2\2\2\u0118\u0116\3")
        buf.write("\2\2\2\u0118\u0119\3\2\2\2\u0119\63\3\2\2\2\u011a\u0118")
        buf.write("\3\2\2\2\u011b\u011c\7\17\2\2\u011c\u011d\7$\2\2\u011d")
        buf.write("\u011e\5\32\16\2\u011e\u011f\7%\2\2\u011f\u0120\5,\27")
        buf.write("\2\u0120\65\3\2\2\2\u0121\u0122\7\f\2\2\u0122\u0123\7")
        buf.write("$\2\2\u0123\u0124\5\32\16\2\u0124\u0125\7%\2\2\u0125\u012f")
        buf.write("\5,\27\2\u0126\u0127\7\r\2\2\u0127\u0128\7\f\2\2\u0128")
        buf.write("\u0129\7$\2\2\u0129\u012a\5\32\16\2\u012a\u012b\7%\2\2")
        buf.write("\u012b\u012c\5,\27\2\u012c\u012e\3\2\2\2\u012d\u0126\3")
        buf.write("\2\2\2\u012e\u0131\3\2\2\2\u012f\u012d\3\2\2\2\u012f\u0130")
        buf.write("\3\2\2\2\u0130\u0134\3\2\2\2\u0131\u012f\3\2\2\2\u0132")
        buf.write("\u0133\7\r\2\2\u0133\u0135\5,\27\2\u0134\u0132\3\2\2\2")
        buf.write("\u0134\u0135\3\2\2\2\u0135\67\3\2\2\2\u0136\u0137\7/\2")
        buf.write("\2\u0137\u0138\7$\2\2\u0138\u0139\5&\24\2\u0139\u013a")
        buf.write("\7%\2\2\u013a\u0141\3\2\2\2\u013b\u013c\5\16\b\2\u013c")
        buf.write("\u013d\7$\2\2\u013d\u013e\5\n\6\2\u013e\u013f\7%\2\2\u013f")
        buf.write("\u0141\3\2\2\2\u0140\u0136\3\2\2\2\u0140\u013b\3\2\2\2")
        buf.write("\u01419\3\2\2\2\u0142\u0145\5\n\6\2\u0143\u0145\5\f\7")
        buf.write("\2\u0144\u0142\3\2\2\2\u0144\u0143\3\2\2\2\u0145\u0146")
        buf.write("\3\2\2\2\u0146\u0147\7/\2\2\u0147\u0148\7$\2\2\u0148\u0149")
        buf.write("\5*\26\2\u0149\u014a\7%\2\2\u014a\u014b\7#\2\2\u014b;")
        buf.write("\3\2\2\2\u014c\u014f\5\n\6\2\u014d\u014f\5\f\7\2\u014e")
        buf.write("\u014c\3\2\2\2\u014e\u014d\3\2\2\2\u014f\u0150\3\2\2\2")
        buf.write("\u0150\u0151\7/\2\2\u0151\u0152\7$\2\2\u0152\u0153\5*")
        buf.write("\26\2\u0153\u0154\7%\2\2\u0154\u0155\5,\27\2\u0155=\3")
        buf.write("\2\2\2 DLNcq\u0085\u008d\u008f\u009e\u00a6\u00a8\u00be")
        buf.write("\u00c2\u00c7\u00cd\u00d5\u00dc\u00e3\u00e7\u00ee\u00f3")
        buf.write("\u00f9\u0100\u0116\u0118\u012f\u0134\u0140\u0144\u014e")
        return buf.getvalue()


class naiveCParser ( Parser ):

    grammarFileName = "naiveC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'sizeof'", "','", "<INVALID>", "'int'", 
                     "'void'", "'char'", "'long long'", "'break'", "'continue'", 
                     "'if'", "'else'", "'return'", "'while'", "'+'", "'++'", 
                     "'--'", "'-'", "'*'", "'/'", "'%'", "'>'", "'<'", "'>='", 
                     "'<='", "'=='", "'!='", "'!'", "'='", "'&'", "'|'", 
                     "'&&'", "'||'", "';'", "'('", "')'", "'['", "']'", 
                     "'{'", "'}'", "'true'", "'false'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "Include", 
                      "TypeInt", "TypeVoid", "TypeChar", "TypeLL", "Break", 
                      "Continue", "If", "Else", "Return", "While", "ADD", 
                      "ADDADD", "SUBSUB", "SUB", "MUL", "DIV", "MOD", "Greater", 
                      "Less", "GreaterEqual", "LessEqual", "Equal", "NotEqual", 
                      "Not", "AssignOperator", "ArithmeticAnd", "ArithmeticOR", 
                      "LogicAnd", "LogicOR", "Semicolon", "LeftParentheses", 
                      "RightParentheses", "LeftBracket", "RightBracket", 
                      "LeftBrace", "RightBrace", "TRUE", "FALSE", "PositiveINT", 
                      "Char", "INT", "ID", "WS", "BlockComment", "LineComment", 
                      "String" ]

    RULE_prog = 0
    RULE_r = 1
    RULE_realTypeID = 2
    RULE_realTypeIDPointer = 3
    RULE_typeIdentifier = 4
    RULE_typeIdentifierPointer = 5
    RULE_sizeof = 6
    RULE_boolExpr = 7
    RULE_idList = 8
    RULE_arithmeticOperator = 9
    RULE_expr = 10
    RULE_conditionOperator = 11
    RULE_conditionExpr = 12
    RULE_assignment = 13
    RULE_definition = 14
    RULE_callProc = 15
    RULE_returnLine = 16
    RULE_param = 17
    RULE_paramList = 18
    RULE_defineParam = 19
    RULE_defineParamList = 20
    RULE_block = 21
    RULE_breakLine = 22
    RULE_continueLine = 23
    RULE_statements = 24
    RULE_whileBlock = 25
    RULE_ifBlock = 26
    RULE_functionCall = 27
    RULE_functionDeclare = 28
    RULE_functionDefine = 29

    ruleNames =  [ "prog", "r", "realTypeID", "realTypeIDPointer", "typeIdentifier", 
                   "typeIdentifierPointer", "sizeof", "boolExpr", "idList", 
                   "arithmeticOperator", "expr", "conditionOperator", "conditionExpr", 
                   "assignment", "definition", "callProc", "returnLine", 
                   "param", "paramList", "defineParam", "defineParamList", 
                   "block", "breakLine", "continueLine", "statements", "whileBlock", 
                   "ifBlock", "functionCall", "functionDeclare", "functionDefine" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    Include=3
    TypeInt=4
    TypeVoid=5
    TypeChar=6
    TypeLL=7
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
    PositiveINT=42
    Char=43
    INT=44
    ID=45
    WS=46
    BlockComment=47
    LineComment=48
    String=49

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
            self.state = 60
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
            self.state = 66
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 63
                self.functionCall()
                pass

            elif la_ == 2:
                self.state = 64
                self.functionDeclare()
                pass

            elif la_ == 3:
                self.state = 65
                self.functionDefine()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 76
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 74
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = naiveCParser.RContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_r)
                        self.state = 68
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 69
                        self.functionCall()
                        pass

                    elif la_ == 2:
                        localctx = naiveCParser.RContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_r)
                        self.state = 70
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 71
                        self.functionDefine()
                        pass

                    elif la_ == 3:
                        localctx = naiveCParser.RContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_r)
                        self.state = 72
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 73
                        self.functionDeclare()
                        pass

             
                self.state = 78
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
            self.state = 79
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << naiveCParser.TypeInt) | (1 << naiveCParser.TypeChar) | (1 << naiveCParser.TypeLL))) != 0)):
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
            self.state = 81
            self.realTypeID()
            self.state = 82
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
            self.state = 84
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << naiveCParser.TypeInt) | (1 << naiveCParser.TypeVoid) | (1 << naiveCParser.TypeChar) | (1 << naiveCParser.TypeLL))) != 0)):
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
            self.state = 86
            self.typeIdentifier()
            self.state = 87
            self.match(naiveCParser.MUL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SizeofContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return naiveCParser.RULE_sizeof

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSizeof" ):
                listener.enterSizeof(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSizeof" ):
                listener.exitSizeof(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSizeof" ):
                return visitor.visitSizeof(self)
            else:
                return visitor.visitChildren(self)




    def sizeof(self):

        localctx = naiveCParser.SizeofContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_sizeof)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(naiveCParser.T__0)
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
        self.enterRule(localctx, 14, self.RULE_boolExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
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
        self.enterRule(localctx, 16, self.RULE_idList)
        try:
            self.state = 97
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 93
                self.match(naiveCParser.ID)
                self.state = 94
                self.match(naiveCParser.T__1)
                self.state = 95
                self.idList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 96
                self.match(naiveCParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArithmeticOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(naiveCParser.ADD, 0)

        def SUB(self):
            return self.getToken(naiveCParser.SUB, 0)

        def MUL(self):
            return self.getToken(naiveCParser.MUL, 0)

        def DIV(self):
            return self.getToken(naiveCParser.DIV, 0)

        def MOD(self):
            return self.getToken(naiveCParser.MOD, 0)

        def ArithmeticAnd(self):
            return self.getToken(naiveCParser.ArithmeticAnd, 0)

        def ArithmeticOR(self):
            return self.getToken(naiveCParser.ArithmeticOR, 0)

        def getRuleIndex(self):
            return naiveCParser.RULE_arithmeticOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmeticOperator" ):
                listener.enterArithmeticOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmeticOperator" ):
                listener.exitArithmeticOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmeticOperator" ):
                return visitor.visitArithmeticOperator(self)
            else:
                return visitor.visitChildren(self)




    def arithmeticOperator(self):

        localctx = naiveCParser.ArithmeticOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_arithmeticOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << naiveCParser.ADD) | (1 << naiveCParser.SUB) | (1 << naiveCParser.MUL) | (1 << naiveCParser.DIV) | (1 << naiveCParser.MOD) | (1 << naiveCParser.ArithmeticAnd) | (1 << naiveCParser.ArithmeticOR))) != 0)):
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
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                localctx = naiveCParser.GetPContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 102
                self.match(naiveCParser.ArithmeticAnd)
                self.state = 103
                self.match(naiveCParser.ID)
                pass

            elif la_ == 2:
                localctx = naiveCParser.MakPContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 104
                self.match(naiveCParser.MUL)
                self.state = 105
                self.expr(11)
                pass

            elif la_ == 3:
                localctx = naiveCParser.NegativeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 106
                self.match(naiveCParser.SUB)
                self.state = 107
                self.expr(10)
                pass

            elif la_ == 4:
                localctx = naiveCParser.TypeCastContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 108
                self.match(naiveCParser.LeftParentheses)
                self.state = 111
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 109
                    self.realTypeIDPointer()
                    pass

                elif la_ == 2:
                    self.state = 110
                    self.realTypeID()
                    pass


                self.state = 113
                self.match(naiveCParser.RightParentheses)
                self.state = 114
                self.expr(9)
                pass

            elif la_ == 5:
                localctx = naiveCParser.PositiveINTContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 116
                self.match(naiveCParser.PositiveINT)
                pass

            elif la_ == 6:
                localctx = naiveCParser.CharContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 117
                self.match(naiveCParser.Char)
                pass

            elif la_ == 7:
                localctx = naiveCParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 118
                self.match(naiveCParser.INT)
                pass

            elif la_ == 8:
                localctx = naiveCParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 119
                self.match(naiveCParser.ID)
                pass

            elif la_ == 9:
                localctx = naiveCParser.FCallContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 120
                self.functionCall()
                pass

            elif la_ == 10:
                localctx = naiveCParser.TrueFalseContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 121
                self.boolExpr()
                pass

            elif la_ == 11:
                localctx = naiveCParser.ArrayVisitContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 122
                self.match(naiveCParser.ID)
                self.state = 123
                self.match(naiveCParser.LeftBracket)
                self.state = 124
                self.expr(0)
                self.state = 125
                self.match(naiveCParser.RightBracket)
                pass

            elif la_ == 12:
                localctx = naiveCParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 127
                self.match(naiveCParser.LeftParentheses)
                self.state = 128
                self.expr(0)
                self.state = 129
                self.match(naiveCParser.RightParentheses)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 141
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 139
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = naiveCParser.MulDivContext(self, naiveCParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 133
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 134
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==naiveCParser.MUL or _la==naiveCParser.DIV):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 135
                        self.expr(15)
                        pass

                    elif la_ == 2:
                        localctx = naiveCParser.AddSubContext(self, naiveCParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 136
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 137
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==naiveCParser.ADD or _la==naiveCParser.SUB):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 138
                        self.expr(14)
                        pass

             
                self.state = 143
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
        self.enterRule(localctx, 22, self.RULE_conditionOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << naiveCParser.Greater) | (1 << naiveCParser.Less) | (1 << naiveCParser.GreaterEqual) | (1 << naiveCParser.LessEqual) | (1 << naiveCParser.Equal))) != 0)):
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
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_conditionExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                localctx = naiveCParser.CondParenContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 147
                self.match(naiveCParser.LeftParentheses)
                self.state = 148
                self.conditionExpr(0)
                self.state = 149
                self.match(naiveCParser.RightParentheses)
                pass

            elif la_ == 2:
                localctx = naiveCParser.CondOpContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 151
                self.expr(0)
                self.state = 152
                self.conditionOperator()
                self.state = 153
                self.expr(0)
                pass

            elif la_ == 3:
                localctx = naiveCParser.CondExpContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 155
                self.expr(0)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 166
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 164
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                    if la_ == 1:
                        localctx = naiveCParser.AndContext(self, naiveCParser.ConditionExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_conditionExpr)
                        self.state = 158
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 159
                        self.match(naiveCParser.LogicAnd)
                        self.state = 160
                        self.conditionExpr(6)
                        pass

                    elif la_ == 2:
                        localctx = naiveCParser.OrContext(self, naiveCParser.ConditionExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_conditionExpr)
                        self.state = 161
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 162
                        self.match(naiveCParser.LogicOR)
                        self.state = 163
                        self.conditionExpr(5)
                        pass

             
                self.state = 168
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
        self.enterRule(localctx, 26, self.RULE_assignment)
        try:
            self.state = 188
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                localctx = naiveCParser.CommonAssignContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 169
                self.match(naiveCParser.ID)
                self.state = 170
                self.match(naiveCParser.AssignOperator)
                self.state = 171
                self.expr(0)
                self.state = 172
                self.match(naiveCParser.Semicolon)
                pass

            elif la_ == 2:
                localctx = naiveCParser.MemoryAssignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 174
                self.match(naiveCParser.MUL)
                self.state = 175
                self.match(naiveCParser.ID)
                self.state = 176
                self.match(naiveCParser.AssignOperator)
                self.state = 177
                self.expr(0)
                self.state = 178
                self.match(naiveCParser.Semicolon)
                pass

            elif la_ == 3:
                localctx = naiveCParser.ArrayAssignContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 180
                self.match(naiveCParser.ID)
                self.state = 181
                self.match(naiveCParser.LeftBracket)
                self.state = 182
                self.expr(0)
                self.state = 183
                self.match(naiveCParser.RightBracket)
                self.state = 184
                self.match(naiveCParser.AssignOperator)
                self.state = 185
                self.expr(0)
                self.state = 186
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
        self.enterRule(localctx, 28, self.RULE_definition)
        self._la = 0 # Token type
        try:
            self.state = 211
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 192
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                if la_ == 1:
                    self.state = 190
                    self.realTypeID()
                    pass

                elif la_ == 2:
                    self.state = 191
                    self.realTypeIDPointer()
                    pass


                self.state = 194
                self.match(naiveCParser.ID)
                self.state = 197
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==naiveCParser.AssignOperator:
                    self.state = 195
                    self.match(naiveCParser.AssignOperator)
                    self.state = 196
                    self.expr(0)


                self.state = 199
                self.match(naiveCParser.Semicolon)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 203
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                if la_ == 1:
                    self.state = 201
                    self.realTypeID()
                    pass

                elif la_ == 2:
                    self.state = 202
                    self.realTypeIDPointer()
                    pass


                self.state = 205
                self.match(naiveCParser.ID)
                self.state = 206
                self.match(naiveCParser.LeftBracket)
                self.state = 207
                self.match(naiveCParser.PositiveINT)
                self.state = 208
                self.match(naiveCParser.RightBracket)
                self.state = 209
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
        self.enterRule(localctx, 30, self.RULE_callProc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.functionCall()
            self.state = 214
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
        self.enterRule(localctx, 32, self.RULE_returnLine)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.match(naiveCParser.Return)
            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << naiveCParser.T__0) | (1 << naiveCParser.SUB) | (1 << naiveCParser.MUL) | (1 << naiveCParser.ArithmeticAnd) | (1 << naiveCParser.LeftParentheses) | (1 << naiveCParser.TRUE) | (1 << naiveCParser.FALSE) | (1 << naiveCParser.PositiveINT) | (1 << naiveCParser.Char) | (1 << naiveCParser.INT) | (1 << naiveCParser.ID))) != 0):
                self.state = 217
                self.expr(0)


            self.state = 220
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
        self.enterRule(localctx, 34, self.RULE_param)
        try:
            self.state = 225
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                localctx = naiveCParser.ParamExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 222
                self.expr(0)
                pass

            elif la_ == 2:
                localctx = naiveCParser.ParamFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 223
                self.functionCall()
                pass

            elif la_ == 3:
                localctx = naiveCParser.ParamStringContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 224
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
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_paramList, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 228
                self.param()


            self._ctx.stop = self._input.LT(-1)
            self.state = 236
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = naiveCParser.ParamListContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_paramList)
                    self.state = 231
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 232
                    self.match(naiveCParser.T__1)
                    self.state = 233
                    self.param() 
                self.state = 238
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
        self.enterRule(localctx, 38, self.RULE_defineParam)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 239
                self.typeIdentifier()
                pass

            elif la_ == 2:
                self.state = 240
                self.typeIdentifierPointer()
                pass


            self.state = 243
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
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_defineParamList, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 246
                self.defineParam()


            self._ctx.stop = self._input.LT(-1)
            self.state = 254
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = naiveCParser.DefineParamListContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_defineParamList)
                    self.state = 249
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 250
                    self.match(naiveCParser.T__1)
                    self.state = 251
                    self.defineParam() 
                self.state = 256
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
        self.enterRule(localctx, 42, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.match(naiveCParser.LeftBrace)
            self.state = 258
            self.statements()
            self.state = 259
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
        self.enterRule(localctx, 44, self.RULE_breakLine)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.match(naiveCParser.Break)
            self.state = 262
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
        self.enterRule(localctx, 46, self.RULE_continueLine)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.match(naiveCParser.Continue)
            self.state = 265
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
        self.enterRule(localctx, 48, self.RULE_statements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << naiveCParser.T__0) | (1 << naiveCParser.TypeInt) | (1 << naiveCParser.TypeChar) | (1 << naiveCParser.TypeLL) | (1 << naiveCParser.Break) | (1 << naiveCParser.Continue) | (1 << naiveCParser.If) | (1 << naiveCParser.Return) | (1 << naiveCParser.While) | (1 << naiveCParser.MUL) | (1 << naiveCParser.LeftBrace) | (1 << naiveCParser.ID))) != 0):
                self.state = 276
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                if la_ == 1:
                    self.state = 267
                    self.assignment()
                    pass

                elif la_ == 2:
                    self.state = 268
                    self.definition()
                    pass

                elif la_ == 3:
                    self.state = 269
                    self.callProc()
                    pass

                elif la_ == 4:
                    self.state = 270
                    self.whileBlock()
                    pass

                elif la_ == 5:
                    self.state = 271
                    self.block()
                    pass

                elif la_ == 6:
                    self.state = 272
                    self.ifBlock()
                    pass

                elif la_ == 7:
                    self.state = 273
                    self.returnLine()
                    pass

                elif la_ == 8:
                    self.state = 274
                    self.breakLine()
                    pass

                elif la_ == 9:
                    self.state = 275
                    self.continueLine()
                    pass


                self.state = 280
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
        self.enterRule(localctx, 50, self.RULE_whileBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.match(naiveCParser.While)
            self.state = 282
            self.match(naiveCParser.LeftParentheses)
            self.state = 283
            self.conditionExpr(0)
            self.state = 284
            self.match(naiveCParser.RightParentheses)
            self.state = 285
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
        self.enterRule(localctx, 52, self.RULE_ifBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.match(naiveCParser.If)
            self.state = 288
            self.match(naiveCParser.LeftParentheses)
            self.state = 289
            self.conditionExpr(0)
            self.state = 290
            self.match(naiveCParser.RightParentheses)
            self.state = 291
            self.block()
            self.state = 301
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 292
                    self.match(naiveCParser.Else)
                    self.state = 293
                    self.match(naiveCParser.If)
                    self.state = 294
                    self.match(naiveCParser.LeftParentheses)
                    self.state = 295
                    localctx.elif_cond = self.conditionExpr(0)
                    self.state = 296
                    self.match(naiveCParser.RightParentheses)
                    self.state = 297
                    self.block() 
                self.state = 303
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

            self.state = 306
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==naiveCParser.Else:
                self.state = 304
                self.match(naiveCParser.Else)
                self.state = 305
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

        def sizeof(self):
            return self.getTypedRuleContext(naiveCParser.SizeofContext,0)


        def typeIdentifier(self):
            return self.getTypedRuleContext(naiveCParser.TypeIdentifierContext,0)


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
        self.enterRule(localctx, 54, self.RULE_functionCall)
        try:
            self.state = 318
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [naiveCParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 308
                self.match(naiveCParser.ID)
                self.state = 309
                self.match(naiveCParser.LeftParentheses)
                self.state = 310
                self.paramList(0)
                self.state = 311
                self.match(naiveCParser.RightParentheses)
                pass
            elif token in [naiveCParser.T__0]:
                self.enterOuterAlt(localctx, 2)
                self.state = 313
                self.sizeof()
                self.state = 314
                self.match(naiveCParser.LeftParentheses)
                self.state = 315
                self.typeIdentifier()
                self.state = 316
                self.match(naiveCParser.RightParentheses)
                pass
            else:
                raise NoViableAltException(self)

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
        self.enterRule(localctx, 56, self.RULE_functionDeclare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 320
                self.typeIdentifier()
                pass

            elif la_ == 2:
                self.state = 321
                self.typeIdentifierPointer()
                pass


            self.state = 324
            self.match(naiveCParser.ID)
            self.state = 325
            self.match(naiveCParser.LeftParentheses)
            self.state = 326
            self.defineParamList(0)
            self.state = 327
            self.match(naiveCParser.RightParentheses)
            self.state = 328
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
        self.enterRule(localctx, 58, self.RULE_functionDefine)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 332
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 330
                self.typeIdentifier()
                pass

            elif la_ == 2:
                self.state = 331
                self.typeIdentifierPointer()
                pass


            self.state = 334
            self.match(naiveCParser.ID)
            self.state = 335
            self.match(naiveCParser.LeftParentheses)
            self.state = 336
            self.defineParamList(0)
            self.state = 337
            self.match(naiveCParser.RightParentheses)
            self.state = 338
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
        self._predicates[10] = self.expr_sempred
        self._predicates[12] = self.conditionExpr_sempred
        self._predicates[18] = self.paramList_sempred
        self._predicates[20] = self.defineParamList_sempred
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
                return self.precpred(self._ctx, 14)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 13)
         

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
         




