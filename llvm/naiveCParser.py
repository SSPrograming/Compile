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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\60")
        buf.write("\u0161\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \3\2\3\2\3\3\3\3\3\3\3\3\5\3G\n\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\7\3O\n\3\f\3\16\3R\13\3\3\4\3\4\3")
        buf.write("\4\5\4W\n\4\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3")
        buf.write("\b\5\bd\n\b\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\5\nu\n\n\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\7\n\u0082\n\n\f\n\16\n\u0085\13\n\3")
        buf.write("\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u0093")
        buf.write("\n\f\3\f\3\f\3\f\3\f\3\f\3\f\7\f\u009b\n\f\f\f\16\f\u009e")
        buf.write("\13\f\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00a6\n\r\3\r\3\r\3")
        buf.write("\r\3\r\3\16\3\16\5\16\u00ae\n\16\3\16\3\16\3\16\5\16\u00b3")
        buf.write("\n\16\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\5\21\u00c1\n\21\3\22\3\22\5\22\u00c5\n\22\3")
        buf.write("\22\3\22\3\22\7\22\u00ca\n\22\f\22\16\22\u00cd\13\22\3")
        buf.write("\23\3\23\5\23\u00d1\n\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\24\5\24\u00da\n\24\5\24\u00dc\n\24\3\25\3\25\3\25\3")
        buf.write("\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\7\26")
        buf.write("\u00eb\n\26\f\26\16\26\u00ee\13\26\3\26\3\26\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\7\31")
        buf.write("\u00fe\n\31\f\31\16\31\u0101\13\31\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\7\32\u010a\n\32\f\32\16\32\u010d\13\32")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\7\34\u0121\n\34\f")
        buf.write("\34\16\34\u0124\13\34\3\34\3\34\5\34\u0128\n\34\3\35\3")
        buf.write("\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\7\35\u0136\n\35\f\35\16\35\u0139\13\35\3\35\3\35\5\35")
        buf.write("\u013d\n\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3")
        buf.write("\36\3\36\5\36\u0149\n\36\3\37\3\37\5\37\u014d\n\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3 \3 \5 \u0157\n \3 \3 \3 \3")
        buf.write(" \3 \3 \3 \3 \3 \2\6\4\22\26\"!\2\4\6\b\n\f\16\20\22\24")
        buf.write("\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>\2\7\3\2)*\5\2")
        buf.write("\17\17\22\25\36\37\3\2\23\24\4\2\17\17\22\22\3\2\26\32")
        buf.write("\2\u017c\2@\3\2\2\2\4F\3\2\2\2\6V\3\2\2\2\bX\3\2\2\2\n")
        buf.write("[\3\2\2\2\f]\3\2\2\2\16c\3\2\2\2\20e\3\2\2\2\22t\3\2\2")
        buf.write("\2\24\u0086\3\2\2\2\26\u0092\3\2\2\2\30\u00a5\3\2\2\2")
        buf.write("\32\u00ad\3\2\2\2\34\u00b6\3\2\2\2\36\u00b9\3\2\2\2 \u00c0")
        buf.write("\3\2\2\2\"\u00c2\3\2\2\2$\u00d0\3\2\2\2&\u00db\3\2\2\2")
        buf.write("(\u00dd\3\2\2\2*\u00e1\3\2\2\2,\u00f1\3\2\2\2.\u00f4\3")
        buf.write("\2\2\2\60\u00ff\3\2\2\2\62\u010b\3\2\2\2\64\u010e\3\2")
        buf.write("\2\2\66\u0114\3\2\2\28\u0129\3\2\2\2:\u0148\3\2\2\2<\u014c")
        buf.write("\3\2\2\2>\u0156\3\2\2\2@A\5\4\3\2A\3\3\2\2\2BC\b\3\1\2")
        buf.write("CG\5:\36\2DG\5<\37\2EG\5> \2FB\3\2\2\2FD\3\2\2\2FE\3\2")
        buf.write("\2\2GP\3\2\2\2HI\f\5\2\2IO\5:\36\2JK\f\4\2\2KO\5> \2L")
        buf.write("M\f\3\2\2MO\5<\37\2NH\3\2\2\2NJ\3\2\2\2NL\3\2\2\2OR\3")
        buf.write("\2\2\2PN\3\2\2\2PQ\3\2\2\2Q\5\3\2\2\2RP\3\2\2\2SW\7\6")
        buf.write("\2\2TW\7\7\2\2UW\7\b\2\2VS\3\2\2\2VT\3\2\2\2VU\3\2\2\2")
        buf.write("W\7\3\2\2\2XY\5\6\4\2YZ\7\23\2\2Z\t\3\2\2\2[\\\7\3\2\2")
        buf.write("\\\13\3\2\2\2]^\t\2\2\2^\r\3\2\2\2_`\7,\2\2`a\7\4\2\2")
        buf.write("ad\5\16\b\2bd\7,\2\2c_\3\2\2\2cb\3\2\2\2d\17\3\2\2\2e")
        buf.write("f\t\3\2\2f\21\3\2\2\2gh\b\n\1\2hi\7\36\2\2iu\7,\2\2jk")
        buf.write("\7\23\2\2ku\5\22\n\tlu\7+\2\2mu\7,\2\2nu\5:\36\2ou\5\f")
        buf.write("\7\2pq\7#\2\2qr\5\22\n\2rs\7$\2\2su\3\2\2\2tg\3\2\2\2")
        buf.write("tj\3\2\2\2tl\3\2\2\2tm\3\2\2\2tn\3\2\2\2to\3\2\2\2tp\3")
        buf.write("\2\2\2u\u0083\3\2\2\2vw\f\f\2\2wx\t\4\2\2x\u0082\5\22")
        buf.write("\n\ryz\f\13\2\2z{\t\5\2\2{\u0082\5\22\n\f|}\f\4\2\2}~")
        buf.write("\7%\2\2~\177\5\22\n\2\177\u0080\7&\2\2\u0080\u0082\3\2")
        buf.write("\2\2\u0081v\3\2\2\2\u0081y\3\2\2\2\u0081|\3\2\2\2\u0082")
        buf.write("\u0085\3\2\2\2\u0083\u0081\3\2\2\2\u0083\u0084\3\2\2\2")
        buf.write("\u0084\23\3\2\2\2\u0085\u0083\3\2\2\2\u0086\u0087\t\6")
        buf.write("\2\2\u0087\25\3\2\2\2\u0088\u0089\b\f\1\2\u0089\u008a")
        buf.write("\7#\2\2\u008a\u008b\5\26\f\2\u008b\u008c\7$\2\2\u008c")
        buf.write("\u0093\3\2\2\2\u008d\u008e\5\22\n\2\u008e\u008f\5\24\13")
        buf.write("\2\u008f\u0090\5\22\n\2\u0090\u0093\3\2\2\2\u0091\u0093")
        buf.write("\5\22\n\2\u0092\u0088\3\2\2\2\u0092\u008d\3\2\2\2\u0092")
        buf.write("\u0091\3\2\2\2\u0093\u009c\3\2\2\2\u0094\u0095\f\7\2\2")
        buf.write("\u0095\u0096\7 \2\2\u0096\u009b\5\26\f\b\u0097\u0098\f")
        buf.write("\6\2\2\u0098\u0099\7!\2\2\u0099\u009b\5\26\f\7\u009a\u0094")
        buf.write("\3\2\2\2\u009a\u0097\3\2\2\2\u009b\u009e\3\2\2\2\u009c")
        buf.write("\u009a\3\2\2\2\u009c\u009d\3\2\2\2\u009d\27\3\2\2\2\u009e")
        buf.write("\u009c\3\2\2\2\u009f\u00a6\7,\2\2\u00a0\u00a1\7,\2\2\u00a1")
        buf.write("\u00a2\7%\2\2\u00a2\u00a3\5\22\n\2\u00a3\u00a4\7&\2\2")
        buf.write("\u00a4\u00a6\3\2\2\2\u00a5\u009f\3\2\2\2\u00a5\u00a0\3")
        buf.write("\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\u00a8\7\35\2\2\u00a8")
        buf.write("\u00a9\5\22\n\2\u00a9\u00aa\7\"\2\2\u00aa\31\3\2\2\2\u00ab")
        buf.write("\u00ae\5\6\4\2\u00ac\u00ae\5\b\5\2\u00ad\u00ab\3\2\2\2")
        buf.write("\u00ad\u00ac\3\2\2\2\u00ae\u00af\3\2\2\2\u00af\u00b2\7")
        buf.write(",\2\2\u00b0\u00b1\7\35\2\2\u00b1\u00b3\5\22\n\2\u00b2")
        buf.write("\u00b0\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3\u00b4\3\2\2\2")
        buf.write("\u00b4\u00b5\7\"\2\2\u00b5\33\3\2\2\2\u00b6\u00b7\5:\36")
        buf.write("\2\u00b7\u00b8\7\"\2\2\u00b8\35\3\2\2\2\u00b9\u00ba\7")
        buf.write("\r\2\2\u00ba\u00bb\5\22\n\2\u00bb\u00bc\7\"\2\2\u00bc")
        buf.write("\37\3\2\2\2\u00bd\u00c1\5\22\n\2\u00be\u00c1\5:\36\2\u00bf")
        buf.write("\u00c1\7\60\2\2\u00c0\u00bd\3\2\2\2\u00c0\u00be\3\2\2")
        buf.write("\2\u00c0\u00bf\3\2\2\2\u00c1!\3\2\2\2\u00c2\u00c4\b\22")
        buf.write("\1\2\u00c3\u00c5\5 \21\2\u00c4\u00c3\3\2\2\2\u00c4\u00c5")
        buf.write("\3\2\2\2\u00c5\u00cb\3\2\2\2\u00c6\u00c7\f\4\2\2\u00c7")
        buf.write("\u00c8\7\4\2\2\u00c8\u00ca\5 \21\2\u00c9\u00c6\3\2\2\2")
        buf.write("\u00ca\u00cd\3\2\2\2\u00cb\u00c9\3\2\2\2\u00cb\u00cc\3")
        buf.write("\2\2\2\u00cc#\3\2\2\2\u00cd\u00cb\3\2\2\2\u00ce\u00d1")
        buf.write("\5\6\4\2\u00cf\u00d1\5\b\5\2\u00d0\u00ce\3\2\2\2\u00d0")
        buf.write("\u00cf\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2\u00d3\7,\2\2")
        buf.write("\u00d3%\3\2\2\2\u00d4\u00d5\5$\23\2\u00d5\u00d6\7\4\2")
        buf.write("\2\u00d6\u00d7\5&\24\2\u00d7\u00dc\3\2\2\2\u00d8\u00da")
        buf.write("\5$\23\2\u00d9\u00d8\3\2\2\2\u00d9\u00da\3\2\2\2\u00da")
        buf.write("\u00dc\3\2\2\2\u00db\u00d4\3\2\2\2\u00db\u00d9\3\2\2\2")
        buf.write("\u00dc\'\3\2\2\2\u00dd\u00de\7\'\2\2\u00de\u00df\5\60")
        buf.write("\31\2\u00df\u00e0\7(\2\2\u00e0)\3\2\2\2\u00e1\u00ec\7")
        buf.write("\'\2\2\u00e2\u00eb\5\30\r\2\u00e3\u00eb\5\32\16\2\u00e4")
        buf.write("\u00eb\5\34\17\2\u00e5\u00eb\5\64\33\2\u00e6\u00eb\5*")
        buf.write("\26\2\u00e7\u00eb\58\35\2\u00e8\u00eb\5,\27\2\u00e9\u00eb")
        buf.write("\5.\30\2\u00ea\u00e2\3\2\2\2\u00ea\u00e3\3\2\2\2\u00ea")
        buf.write("\u00e4\3\2\2\2\u00ea\u00e5\3\2\2\2\u00ea\u00e6\3\2\2\2")
        buf.write("\u00ea\u00e7\3\2\2\2\u00ea\u00e8\3\2\2\2\u00ea\u00e9\3")
        buf.write("\2\2\2\u00eb\u00ee\3\2\2\2\u00ec\u00ea\3\2\2\2\u00ec\u00ed")
        buf.write("\3\2\2\2\u00ed\u00ef\3\2\2\2\u00ee\u00ec\3\2\2\2\u00ef")
        buf.write("\u00f0\7(\2\2\u00f0+\3\2\2\2\u00f1\u00f2\7\t\2\2\u00f2")
        buf.write("\u00f3\7\"\2\2\u00f3-\3\2\2\2\u00f4\u00f5\7\n\2\2\u00f5")
        buf.write("\u00f6\7\"\2\2\u00f6/\3\2\2\2\u00f7\u00fe\5\30\r\2\u00f8")
        buf.write("\u00fe\5\32\16\2\u00f9\u00fe\5\34\17\2\u00fa\u00fe\5\64")
        buf.write("\33\2\u00fb\u00fe\5(\25\2\u00fc\u00fe\5\66\34\2\u00fd")
        buf.write("\u00f7\3\2\2\2\u00fd\u00f8\3\2\2\2\u00fd\u00f9\3\2\2\2")
        buf.write("\u00fd\u00fa\3\2\2\2\u00fd\u00fb\3\2\2\2\u00fd\u00fc\3")
        buf.write("\2\2\2\u00fe\u0101\3\2\2\2\u00ff\u00fd\3\2\2\2\u00ff\u0100")
        buf.write("\3\2\2\2\u0100\61\3\2\2\2\u0101\u00ff\3\2\2\2\u0102\u010a")
        buf.write("\5\30\r\2\u0103\u010a\5\32\16\2\u0104\u010a\5\34\17\2")
        buf.write("\u0105\u010a\5\64\33\2\u0106\u010a\5(\25\2\u0107\u010a")
        buf.write("\5\66\34\2\u0108\u010a\5\36\20\2\u0109\u0102\3\2\2\2\u0109")
        buf.write("\u0103\3\2\2\2\u0109\u0104\3\2\2\2\u0109\u0105\3\2\2\2")
        buf.write("\u0109\u0106\3\2\2\2\u0109\u0107\3\2\2\2\u0109\u0108\3")
        buf.write("\2\2\2\u010a\u010d\3\2\2\2\u010b\u0109\3\2\2\2\u010b\u010c")
        buf.write("\3\2\2\2\u010c\63\3\2\2\2\u010d\u010b\3\2\2\2\u010e\u010f")
        buf.write("\7\16\2\2\u010f\u0110\7#\2\2\u0110\u0111\5\26\f\2\u0111")
        buf.write("\u0112\7$\2\2\u0112\u0113\5*\26\2\u0113\65\3\2\2\2\u0114")
        buf.write("\u0115\7\13\2\2\u0115\u0116\7#\2\2\u0116\u0117\5\26\f")
        buf.write("\2\u0117\u0118\7$\2\2\u0118\u0122\5(\25\2\u0119\u011a")
        buf.write("\7\f\2\2\u011a\u011b\7\13\2\2\u011b\u011c\7#\2\2\u011c")
        buf.write("\u011d\5\26\f\2\u011d\u011e\7$\2\2\u011e\u011f\5(\25\2")
        buf.write("\u011f\u0121\3\2\2\2\u0120\u0119\3\2\2\2\u0121\u0124\3")
        buf.write("\2\2\2\u0122\u0120\3\2\2\2\u0122\u0123\3\2\2\2\u0123\u0127")
        buf.write("\3\2\2\2\u0124\u0122\3\2\2\2\u0125\u0126\7\f\2\2\u0126")
        buf.write("\u0128\5(\25\2\u0127\u0125\3\2\2\2\u0127\u0128\3\2\2\2")
        buf.write("\u0128\67\3\2\2\2\u0129\u012a\7\13\2\2\u012a\u012b\7#")
        buf.write("\2\2\u012b\u012c\5\26\f\2\u012c\u012d\7$\2\2\u012d\u0137")
        buf.write("\5*\26\2\u012e\u012f\7\f\2\2\u012f\u0130\7\13\2\2\u0130")
        buf.write("\u0131\7#\2\2\u0131\u0132\5\26\f\2\u0132\u0133\7$\2\2")
        buf.write("\u0133\u0134\5*\26\2\u0134\u0136\3\2\2\2\u0135\u012e\3")
        buf.write("\2\2\2\u0136\u0139\3\2\2\2\u0137\u0135\3\2\2\2\u0137\u0138")
        buf.write("\3\2\2\2\u0138\u013c\3\2\2\2\u0139\u0137\3\2\2\2\u013a")
        buf.write("\u013b\7\f\2\2\u013b\u013d\5*\26\2\u013c\u013a\3\2\2\2")
        buf.write("\u013c\u013d\3\2\2\2\u013d9\3\2\2\2\u013e\u013f\7,\2\2")
        buf.write("\u013f\u0140\7#\2\2\u0140\u0141\5\"\22\2\u0141\u0142\7")
        buf.write("$\2\2\u0142\u0149\3\2\2\2\u0143\u0144\5\n\6\2\u0144\u0145")
        buf.write("\7#\2\2\u0145\u0146\5\6\4\2\u0146\u0147\7$\2\2\u0147\u0149")
        buf.write("\3\2\2\2\u0148\u013e\3\2\2\2\u0148\u0143\3\2\2\2\u0149")
        buf.write(";\3\2\2\2\u014a\u014d\5\6\4\2\u014b\u014d\5\b\5\2\u014c")
        buf.write("\u014a\3\2\2\2\u014c\u014b\3\2\2\2\u014d\u014e\3\2\2\2")
        buf.write("\u014e\u014f\7,\2\2\u014f\u0150\7#\2\2\u0150\u0151\5&")
        buf.write("\24\2\u0151\u0152\7$\2\2\u0152\u0153\7\"\2\2\u0153=\3")
        buf.write("\2\2\2\u0154\u0157\5\6\4\2\u0155\u0157\5\b\5\2\u0156\u0154")
        buf.write("\3\2\2\2\u0156\u0155\3\2\2\2\u0157\u0158\3\2\2\2\u0158")
        buf.write("\u0159\7,\2\2\u0159\u015a\7#\2\2\u015a\u015b\5&\24\2\u015b")
        buf.write("\u015c\7$\2\2\u015c\u015d\7\'\2\2\u015d\u015e\5\62\32")
        buf.write("\2\u015e\u015f\7(\2\2\u015f?\3\2\2\2#FNPVct\u0081\u0083")
        buf.write("\u0092\u009a\u009c\u00a5\u00ad\u00b2\u00c0\u00c4\u00cb")
        buf.write("\u00d0\u00d9\u00db\u00ea\u00ec\u00fd\u00ff\u0109\u010b")
        buf.write("\u0122\u0127\u0137\u013c\u0148\u014c\u0156")
        return buf.getvalue()


class naiveCParser ( Parser ):

    grammarFileName = "naiveC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'sizeof'", "','", "<INVALID>", "'int'", 
                     "'void'", "'char'", "'break'", "'continue'", "'if'", 
                     "'else'", "'return'", "'while'", "'+'", "'++'", "'--'", 
                     "'-'", "'*'", "'/'", "'%'", "'>'", "'<'", "'>='", "'<='", 
                     "'=='", "'!='", "'!'", "'='", "'&'", "'|'", "'&&'", 
                     "'||'", "';'", "'('", "')'", "'['", "']'", "'{'", "'}'", 
                     "'true'", "'false'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "Include", 
                      "TypeInt", "TypeVoid", "TypeChar", "Break", "Continue", 
                      "If", "Else", "Return", "While", "ADD", "ADDADD", 
                      "SUBSUB", "SUB", "MUL", "DIV", "MOD", "Greater", "Less", 
                      "GreaterEqual", "LessEqual", "Equal", "NotEqual", 
                      "Not", "AssignOperator", "ArithmeticAnd", "ArithmeticOR", 
                      "LogicAnd", "LogicOR", "Semicolon", "LeftParentheses", 
                      "RightParentheses", "LeftBracket", "RightBracket", 
                      "LeftBrace", "RightBrace", "TRUE", "FALSE", "INT", 
                      "ID", "WS", "BlockComment", "LineComment", "String" ]

    RULE_prog = 0
    RULE_r = 1
    RULE_typeIdentifier = 2
    RULE_typeIdentifierPointer = 3
    RULE_sizeof = 4
    RULE_boolExpr = 5
    RULE_idList = 6
    RULE_arithmeticOperator = 7
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
    RULE_loopBlock = 20
    RULE_breakLine = 21
    RULE_continueLine = 22
    RULE_statements = 23
    RULE_returnStatemts = 24
    RULE_whileBlock = 25
    RULE_ifBlock = 26
    RULE_ifLoopBlock = 27
    RULE_functionCall = 28
    RULE_functionDeclare = 29
    RULE_functionDefine = 30

    ruleNames =  [ "prog", "r", "typeIdentifier", "typeIdentifierPointer", 
                   "sizeof", "boolExpr", "idList", "arithmeticOperator", 
                   "expr", "conditionOperator", "conditionExpr", "assignment", 
                   "definition", "callProc", "returnLine", "param", "paramList", 
                   "defineParam", "defineParamList", "block", "loopBlock", 
                   "breakLine", "continueLine", "statements", "returnStatemts", 
                   "whileBlock", "ifBlock", "ifLoopBlock", "functionCall", 
                   "functionDeclare", "functionDefine" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    Include=3
    TypeInt=4
    TypeVoid=5
    TypeChar=6
    Break=7
    Continue=8
    If=9
    Else=10
    Return=11
    While=12
    ADD=13
    ADDADD=14
    SUBSUB=15
    SUB=16
    MUL=17
    DIV=18
    MOD=19
    Greater=20
    Less=21
    GreaterEqual=22
    LessEqual=23
    Equal=24
    NotEqual=25
    Not=26
    AssignOperator=27
    ArithmeticAnd=28
    ArithmeticOR=29
    LogicAnd=30
    LogicOR=31
    Semicolon=32
    LeftParentheses=33
    RightParentheses=34
    LeftBracket=35
    RightBracket=36
    LeftBrace=37
    RightBrace=38
    TRUE=39
    FALSE=40
    INT=41
    ID=42
    WS=43
    BlockComment=44
    LineComment=45
    String=46

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
            self.state = 62
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
            self.state = 68
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 65
                self.functionCall()
                pass

            elif la_ == 2:
                self.state = 66
                self.functionDeclare()
                pass

            elif la_ == 3:
                self.state = 67
                self.functionDefine()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 78
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 76
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = naiveCParser.RContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_r)
                        self.state = 70
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 71
                        self.functionCall()
                        pass

                    elif la_ == 2:
                        localctx = naiveCParser.RContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_r)
                        self.state = 72
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 73
                        self.functionDefine()
                        pass

                    elif la_ == 3:
                        localctx = naiveCParser.RContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_r)
                        self.state = 74
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 75
                        self.functionDeclare()
                        pass

             
                self.state = 80
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TypeIdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return naiveCParser.RULE_typeIdentifier

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TypeCharContext(TypeIdentifierContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a naiveCParser.TypeIdentifierContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TypeChar(self):
            return self.getToken(naiveCParser.TypeChar, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeChar" ):
                listener.enterTypeChar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeChar" ):
                listener.exitTypeChar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeChar" ):
                return visitor.visitTypeChar(self)
            else:
                return visitor.visitChildren(self)


    class TypeVoidContext(TypeIdentifierContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a naiveCParser.TypeIdentifierContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TypeVoid(self):
            return self.getToken(naiveCParser.TypeVoid, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeVoid" ):
                listener.enterTypeVoid(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeVoid" ):
                listener.exitTypeVoid(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeVoid" ):
                return visitor.visitTypeVoid(self)
            else:
                return visitor.visitChildren(self)


    class TypeIntContext(TypeIdentifierContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a naiveCParser.TypeIdentifierContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TypeInt(self):
            return self.getToken(naiveCParser.TypeInt, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeInt" ):
                listener.enterTypeInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeInt" ):
                listener.exitTypeInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeInt" ):
                return visitor.visitTypeInt(self)
            else:
                return visitor.visitChildren(self)



    def typeIdentifier(self):

        localctx = naiveCParser.TypeIdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_typeIdentifier)
        try:
            self.state = 84
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [naiveCParser.TypeInt]:
                localctx = naiveCParser.TypeIntContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 81
                self.match(naiveCParser.TypeInt)
                pass
            elif token in [naiveCParser.TypeVoid]:
                localctx = naiveCParser.TypeVoidContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 82
                self.match(naiveCParser.TypeVoid)
                pass
            elif token in [naiveCParser.TypeChar]:
                localctx = naiveCParser.TypeCharContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 83
                self.match(naiveCParser.TypeChar)
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
        self.enterRule(localctx, 6, self.RULE_typeIdentifierPointer)
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
        self.enterRule(localctx, 8, self.RULE_sizeof)
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
        self.enterRule(localctx, 10, self.RULE_boolExpr)
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
        self.enterRule(localctx, 12, self.RULE_idList)
        try:
            self.state = 97
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
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
        self.enterRule(localctx, 14, self.RULE_arithmeticOperator)
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

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(naiveCParser.ExprContext)
            else:
                return self.getTypedRuleContext(naiveCParser.ExprContext,i)

        def LeftBracket(self):
            return self.getToken(naiveCParser.LeftBracket, 0)
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


    class FcallContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a naiveCParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def functionCall(self):
            return self.getTypedRuleContext(naiveCParser.FunctionCallContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFcall" ):
                listener.enterFcall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFcall" ):
                listener.exitFcall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFcall" ):
                return visitor.visitFcall(self)
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
            self.state = 114
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
                self.expr(7)
                pass

            elif la_ == 3:
                localctx = naiveCParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 106
                self.match(naiveCParser.INT)
                pass

            elif la_ == 4:
                localctx = naiveCParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 107
                self.match(naiveCParser.ID)
                pass

            elif la_ == 5:
                localctx = naiveCParser.FcallContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 108
                self.functionCall()
                pass

            elif la_ == 6:
                localctx = naiveCParser.TrueFalseContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 109
                self.boolExpr()
                pass

            elif la_ == 7:
                localctx = naiveCParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 110
                self.match(naiveCParser.LeftParentheses)
                self.state = 111
                self.expr(0)
                self.state = 112
                self.match(naiveCParser.RightParentheses)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 129
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 127
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = naiveCParser.MulDivContext(self, naiveCParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 116
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 117
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==naiveCParser.MUL or _la==naiveCParser.DIV):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 118
                        self.expr(11)
                        pass

                    elif la_ == 2:
                        localctx = naiveCParser.AddSubContext(self, naiveCParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 119
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 120
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==naiveCParser.ADD or _la==naiveCParser.SUB):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 121
                        self.expr(10)
                        pass

                    elif la_ == 3:
                        localctx = naiveCParser.ArrayVisitContext(self, naiveCParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 122
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 123
                        self.match(naiveCParser.LeftBracket)
                        self.state = 124
                        self.expr(0)
                        self.state = 125
                        self.match(naiveCParser.RightBracket)
                        pass

             
                self.state = 131
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
        self.enterRule(localctx, 18, self.RULE_conditionOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
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

        def LeftParentheses(self):
            return self.getToken(naiveCParser.LeftParentheses, 0)

        def conditionExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(naiveCParser.ConditionExprContext)
            else:
                return self.getTypedRuleContext(naiveCParser.ConditionExprContext,i)


        def RightParentheses(self):
            return self.getToken(naiveCParser.RightParentheses, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(naiveCParser.ExprContext)
            else:
                return self.getTypedRuleContext(naiveCParser.ExprContext,i)


        def conditionOperator(self):
            return self.getTypedRuleContext(naiveCParser.ConditionOperatorContext,0)


        def LogicAnd(self):
            return self.getToken(naiveCParser.LogicAnd, 0)

        def LogicOR(self):
            return self.getToken(naiveCParser.LogicOR, 0)

        def getRuleIndex(self):
            return naiveCParser.RULE_conditionExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionExpr" ):
                listener.enterConditionExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionExpr" ):
                listener.exitConditionExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditionExpr" ):
                return visitor.visitConditionExpr(self)
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
            self.state = 144
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 135
                self.match(naiveCParser.LeftParentheses)
                self.state = 136
                self.conditionExpr(0)
                self.state = 137
                self.match(naiveCParser.RightParentheses)
                pass

            elif la_ == 2:
                self.state = 139
                self.expr(0)
                self.state = 140
                self.conditionOperator()
                self.state = 141
                self.expr(0)
                pass

            elif la_ == 3:
                self.state = 143
                self.expr(0)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 154
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 152
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                    if la_ == 1:
                        localctx = naiveCParser.ConditionExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_conditionExpr)
                        self.state = 146
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 147
                        self.match(naiveCParser.LogicAnd)
                        self.state = 148
                        self.conditionExpr(6)
                        pass

                    elif la_ == 2:
                        localctx = naiveCParser.ConditionExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_conditionExpr)
                        self.state = 149
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 150
                        self.match(naiveCParser.LogicOR)
                        self.state = 151
                        self.conditionExpr(5)
                        pass

             
                self.state = 156
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
            self.index = None # ExprContext
            self.value = None # ExprContext

        def AssignOperator(self):
            return self.getToken(naiveCParser.AssignOperator, 0)

        def Semicolon(self):
            return self.getToken(naiveCParser.Semicolon, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(naiveCParser.ExprContext)
            else:
                return self.getTypedRuleContext(naiveCParser.ExprContext,i)


        def ID(self):
            return self.getToken(naiveCParser.ID, 0)

        def LeftBracket(self):
            return self.getToken(naiveCParser.LeftBracket, 0)

        def RightBracket(self):
            return self.getToken(naiveCParser.RightBracket, 0)

        def getRuleIndex(self):
            return naiveCParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = naiveCParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 157
                self.match(naiveCParser.ID)
                pass

            elif la_ == 2:
                self.state = 158
                self.match(naiveCParser.ID)
                self.state = 159
                self.match(naiveCParser.LeftBracket)
                self.state = 160
                localctx.index = self.expr(0)
                self.state = 161
                self.match(naiveCParser.RightBracket)
                pass


            self.state = 165
            self.match(naiveCParser.AssignOperator)
            self.state = 166
            localctx.value = self.expr(0)
            self.state = 167
            self.match(naiveCParser.Semicolon)
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

        def typeIdentifier(self):
            return self.getTypedRuleContext(naiveCParser.TypeIdentifierContext,0)


        def typeIdentifierPointer(self):
            return self.getTypedRuleContext(naiveCParser.TypeIdentifierPointerContext,0)


        def AssignOperator(self):
            return self.getToken(naiveCParser.AssignOperator, 0)

        def expr(self):
            return self.getTypedRuleContext(naiveCParser.ExprContext,0)


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
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 169
                self.typeIdentifier()
                pass

            elif la_ == 2:
                self.state = 170
                self.typeIdentifierPointer()
                pass


            self.state = 173
            self.match(naiveCParser.ID)
            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==naiveCParser.AssignOperator:
                self.state = 174
                self.match(naiveCParser.AssignOperator)
                self.state = 175
                self.expr(0)


            self.state = 178
            self.match(naiveCParser.Semicolon)
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
            self.state = 180
            self.functionCall()
            self.state = 181
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

        def expr(self):
            return self.getTypedRuleContext(naiveCParser.ExprContext,0)


        def Semicolon(self):
            return self.getToken(naiveCParser.Semicolon, 0)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.match(naiveCParser.Return)
            self.state = 184
            self.expr(0)
            self.state = 185
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
            self.state = 190
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                localctx = naiveCParser.ParamExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 187
                self.expr(0)
                pass

            elif la_ == 2:
                localctx = naiveCParser.ParamFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 188
                self.functionCall()
                pass

            elif la_ == 3:
                localctx = naiveCParser.ParamStringContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 189
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
            self.state = 194
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 193
                self.param()


            self._ctx.stop = self._input.LT(-1)
            self.state = 201
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = naiveCParser.ParamListContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_paramList)
                    self.state = 196
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 197
                    self.match(naiveCParser.T__1)
                    self.state = 198
                    self.param() 
                self.state = 203
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

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
            self.state = 206
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 204
                self.typeIdentifier()
                pass

            elif la_ == 2:
                self.state = 205
                self.typeIdentifierPointer()
                pass


            self.state = 208
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




    def defineParamList(self):

        localctx = naiveCParser.DefineParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_defineParamList)
        self._la = 0 # Token type
        try:
            self.state = 217
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 210
                self.defineParam()
                self.state = 211
                self.match(naiveCParser.T__1)
                self.state = 212
                self.defineParamList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 215
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << naiveCParser.TypeInt) | (1 << naiveCParser.TypeVoid) | (1 << naiveCParser.TypeChar))) != 0):
                    self.state = 214
                    self.defineParam()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
            self.state = 219
            self.match(naiveCParser.LeftBrace)
            self.state = 220
            self.statements()
            self.state = 221
            self.match(naiveCParser.RightBrace)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LeftBrace(self):
            return self.getToken(naiveCParser.LeftBrace, 0)

        def RightBrace(self):
            return self.getToken(naiveCParser.RightBrace, 0)

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


        def loopBlock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(naiveCParser.LoopBlockContext)
            else:
                return self.getTypedRuleContext(naiveCParser.LoopBlockContext,i)


        def ifLoopBlock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(naiveCParser.IfLoopBlockContext)
            else:
                return self.getTypedRuleContext(naiveCParser.IfLoopBlockContext,i)


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
            return naiveCParser.RULE_loopBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoopBlock" ):
                listener.enterLoopBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoopBlock" ):
                listener.exitLoopBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoopBlock" ):
                return visitor.visitLoopBlock(self)
            else:
                return visitor.visitChildren(self)




    def loopBlock(self):

        localctx = naiveCParser.LoopBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_loopBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.match(naiveCParser.LeftBrace)
            self.state = 234
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << naiveCParser.T__0) | (1 << naiveCParser.TypeInt) | (1 << naiveCParser.TypeVoid) | (1 << naiveCParser.TypeChar) | (1 << naiveCParser.Break) | (1 << naiveCParser.Continue) | (1 << naiveCParser.If) | (1 << naiveCParser.While) | (1 << naiveCParser.LeftBrace) | (1 << naiveCParser.ID))) != 0):
                self.state = 232
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                if la_ == 1:
                    self.state = 224
                    self.assignment()
                    pass

                elif la_ == 2:
                    self.state = 225
                    self.definition()
                    pass

                elif la_ == 3:
                    self.state = 226
                    self.callProc()
                    pass

                elif la_ == 4:
                    self.state = 227
                    self.whileBlock()
                    pass

                elif la_ == 5:
                    self.state = 228
                    self.loopBlock()
                    pass

                elif la_ == 6:
                    self.state = 229
                    self.ifLoopBlock()
                    pass

                elif la_ == 7:
                    self.state = 230
                    self.breakLine()
                    pass

                elif la_ == 8:
                    self.state = 231
                    self.continueLine()
                    pass


                self.state = 236
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 237
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
        self.enterRule(localctx, 42, self.RULE_breakLine)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(naiveCParser.Break)
            self.state = 240
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
        self.enterRule(localctx, 44, self.RULE_continueLine)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.match(naiveCParser.Continue)
            self.state = 243
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
        self.enterRule(localctx, 46, self.RULE_statements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << naiveCParser.T__0) | (1 << naiveCParser.TypeInt) | (1 << naiveCParser.TypeVoid) | (1 << naiveCParser.TypeChar) | (1 << naiveCParser.If) | (1 << naiveCParser.While) | (1 << naiveCParser.LeftBrace) | (1 << naiveCParser.ID))) != 0):
                self.state = 251
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                if la_ == 1:
                    self.state = 245
                    self.assignment()
                    pass

                elif la_ == 2:
                    self.state = 246
                    self.definition()
                    pass

                elif la_ == 3:
                    self.state = 247
                    self.callProc()
                    pass

                elif la_ == 4:
                    self.state = 248
                    self.whileBlock()
                    pass

                elif la_ == 5:
                    self.state = 249
                    self.block()
                    pass

                elif la_ == 6:
                    self.state = 250
                    self.ifBlock()
                    pass


                self.state = 255
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatemtsContext(ParserRuleContext):
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


        def getRuleIndex(self):
            return naiveCParser.RULE_returnStatemts

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatemts" ):
                listener.enterReturnStatemts(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatemts" ):
                listener.exitReturnStatemts(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatemts" ):
                return visitor.visitReturnStatemts(self)
            else:
                return visitor.visitChildren(self)




    def returnStatemts(self):

        localctx = naiveCParser.ReturnStatemtsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_returnStatemts)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << naiveCParser.T__0) | (1 << naiveCParser.TypeInt) | (1 << naiveCParser.TypeVoid) | (1 << naiveCParser.TypeChar) | (1 << naiveCParser.If) | (1 << naiveCParser.Return) | (1 << naiveCParser.While) | (1 << naiveCParser.LeftBrace) | (1 << naiveCParser.ID))) != 0):
                self.state = 263
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                if la_ == 1:
                    self.state = 256
                    self.assignment()
                    pass

                elif la_ == 2:
                    self.state = 257
                    self.definition()
                    pass

                elif la_ == 3:
                    self.state = 258
                    self.callProc()
                    pass

                elif la_ == 4:
                    self.state = 259
                    self.whileBlock()
                    pass

                elif la_ == 5:
                    self.state = 260
                    self.block()
                    pass

                elif la_ == 6:
                    self.state = 261
                    self.ifBlock()
                    pass

                elif la_ == 7:
                    self.state = 262
                    self.returnLine()
                    pass


                self.state = 267
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

        def loopBlock(self):
            return self.getTypedRuleContext(naiveCParser.LoopBlockContext,0)


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
            self.state = 268
            self.match(naiveCParser.While)
            self.state = 269
            self.match(naiveCParser.LeftParentheses)
            self.state = 270
            self.conditionExpr(0)
            self.state = 271
            self.match(naiveCParser.RightParentheses)
            self.state = 272
            self.loopBlock()
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
            self.state = 274
            self.match(naiveCParser.If)
            self.state = 275
            self.match(naiveCParser.LeftParentheses)
            self.state = 276
            self.conditionExpr(0)
            self.state = 277
            self.match(naiveCParser.RightParentheses)
            self.state = 278
            self.block()
            self.state = 288
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 279
                    self.match(naiveCParser.Else)
                    self.state = 280
                    self.match(naiveCParser.If)
                    self.state = 281
                    self.match(naiveCParser.LeftParentheses)
                    self.state = 282
                    self.conditionExpr(0)
                    self.state = 283
                    self.match(naiveCParser.RightParentheses)
                    self.state = 284
                    self.block() 
                self.state = 290
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

            self.state = 293
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==naiveCParser.Else:
                self.state = 291
                self.match(naiveCParser.Else)
                self.state = 292
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfLoopBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

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

        def loopBlock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(naiveCParser.LoopBlockContext)
            else:
                return self.getTypedRuleContext(naiveCParser.LoopBlockContext,i)


        def Else(self, i:int=None):
            if i is None:
                return self.getTokens(naiveCParser.Else)
            else:
                return self.getToken(naiveCParser.Else, i)

        def getRuleIndex(self):
            return naiveCParser.RULE_ifLoopBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfLoopBlock" ):
                listener.enterIfLoopBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfLoopBlock" ):
                listener.exitIfLoopBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfLoopBlock" ):
                return visitor.visitIfLoopBlock(self)
            else:
                return visitor.visitChildren(self)




    def ifLoopBlock(self):

        localctx = naiveCParser.IfLoopBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_ifLoopBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.match(naiveCParser.If)
            self.state = 296
            self.match(naiveCParser.LeftParentheses)
            self.state = 297
            self.conditionExpr(0)
            self.state = 298
            self.match(naiveCParser.RightParentheses)
            self.state = 299
            self.loopBlock()
            self.state = 309
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 300
                    self.match(naiveCParser.Else)
                    self.state = 301
                    self.match(naiveCParser.If)
                    self.state = 302
                    self.match(naiveCParser.LeftParentheses)
                    self.state = 303
                    self.conditionExpr(0)
                    self.state = 304
                    self.match(naiveCParser.RightParentheses)
                    self.state = 305
                    self.loopBlock() 
                self.state = 311
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

            self.state = 314
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==naiveCParser.Else:
                self.state = 312
                self.match(naiveCParser.Else)
                self.state = 313
                self.loopBlock()


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
        self.enterRule(localctx, 56, self.RULE_functionCall)
        try:
            self.state = 326
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [naiveCParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 316
                self.match(naiveCParser.ID)
                self.state = 317
                self.match(naiveCParser.LeftParentheses)
                self.state = 318
                self.paramList(0)
                self.state = 319
                self.match(naiveCParser.RightParentheses)
                pass
            elif token in [naiveCParser.T__0]:
                self.enterOuterAlt(localctx, 2)
                self.state = 321
                self.sizeof()
                self.state = 322
                self.match(naiveCParser.LeftParentheses)
                self.state = 323
                self.typeIdentifier()
                self.state = 324
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
        self.enterRule(localctx, 58, self.RULE_functionDeclare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 328
                self.typeIdentifier()
                pass

            elif la_ == 2:
                self.state = 329
                self.typeIdentifierPointer()
                pass


            self.state = 332
            self.match(naiveCParser.ID)
            self.state = 333
            self.match(naiveCParser.LeftParentheses)
            self.state = 334
            self.defineParamList()
            self.state = 335
            self.match(naiveCParser.RightParentheses)
            self.state = 336
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

        def LeftBrace(self):
            return self.getToken(naiveCParser.LeftBrace, 0)

        def returnStatemts(self):
            return self.getTypedRuleContext(naiveCParser.ReturnStatemtsContext,0)


        def RightBrace(self):
            return self.getToken(naiveCParser.RightBrace, 0)

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
        self.enterRule(localctx, 60, self.RULE_functionDefine)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 338
                self.typeIdentifier()
                pass

            elif la_ == 2:
                self.state = 339
                self.typeIdentifierPointer()
                pass


            self.state = 342
            self.match(naiveCParser.ID)
            self.state = 343
            self.match(naiveCParser.LeftParentheses)
            self.state = 344
            self.defineParamList()
            self.state = 345
            self.match(naiveCParser.RightParentheses)
            self.state = 346
            self.match(naiveCParser.LeftBrace)
            self.state = 347
            self.returnStatemts()
            self.state = 348
            self.match(naiveCParser.RightBrace)
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
                return self.precpred(self._ctx, 10)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

    def conditionExpr_sempred(self, localctx:ConditionExprContext, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 4)
         

    def paramList_sempred(self, localctx:ParamListContext, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 2)
         




