// Generated from e:\Tsinghua\课程\大三上\汇编与编译原理\作业\编译\编译小组作业\src\LLVM\antlr\src\naiveC.g4 by ANTLR 4.8
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class naiveCLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, Include=3, TypeInt=4, TypeVoid=5, TypeChar=6, Break=7, 
		Continue=8, If=9, Else=10, Return=11, While=12, ADD=13, ADDADD=14, SUBSUB=15, 
		SUB=16, MUL=17, DIV=18, MOD=19, Greater=20, Less=21, GreaterEqual=22, 
		LessEqual=23, Equal=24, NotEqual=25, Not=26, AssignOperator=27, ArithmeticAnd=28, 
		ArithmeticOR=29, LogicAnd=30, LogicOR=31, Semicolon=32, LeftParentheses=33, 
		RightParentheses=34, LeftBracket=35, RightBracket=36, LeftBrace=37, RightBrace=38, 
		TRUE=39, FALSE=40, PositiveINT=41, Char=42, INT=43, ID=44, WS=45, BlockComment=46, 
		LineComment=47, String=48;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "Include", "TypeInt", "TypeVoid", "TypeChar", "Break", 
			"Continue", "If", "Else", "Return", "While", "ADD", "ADDADD", "SUBSUB", 
			"SUB", "MUL", "DIV", "MOD", "Greater", "Less", "GreaterEqual", "LessEqual", 
			"Equal", "NotEqual", "Not", "AssignOperator", "ArithmeticAnd", "ArithmeticOR", 
			"LogicAnd", "LogicOR", "Semicolon", "LeftParentheses", "RightParentheses", 
			"LeftBracket", "RightBracket", "LeftBrace", "RightBrace", "TRUE", "FALSE", 
			"PositiveINT", "Char", "INT", "ID", "WS", "BlockComment", "LineComment", 
			"String"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'sizeof'", "','", null, "'int'", "'void'", "'char'", "'break'", 
			"'continue'", "'if'", "'else'", "'return'", "'while'", "'+'", "'++'", 
			"'--'", "'-'", "'*'", "'/'", "'%'", "'>'", "'<'", "'>='", "'<='", "'=='", 
			"'!='", "'!'", "'='", "'&'", "'|'", "'&&'", "'||'", "';'", "'('", "')'", 
			"'['", "']'", "'{'", "'}'", "'true'", "'false'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, "Include", "TypeInt", "TypeVoid", "TypeChar", "Break", 
			"Continue", "If", "Else", "Return", "While", "ADD", "ADDADD", "SUBSUB", 
			"SUB", "MUL", "DIV", "MOD", "Greater", "Less", "GreaterEqual", "LessEqual", 
			"Equal", "NotEqual", "Not", "AssignOperator", "ArithmeticAnd", "ArithmeticOR", 
			"LogicAnd", "LogicOR", "Semicolon", "LeftParentheses", "RightParentheses", 
			"LeftBracket", "RightBracket", "LeftBrace", "RightBrace", "TRUE", "FALSE", 
			"PositiveINT", "Char", "INT", "ID", "WS", "BlockComment", "LineComment", 
			"String"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public naiveCLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "naiveC.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\62\u0142\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31"+
		"\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t"+
		" \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t"+
		"+\4,\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\3\2\3\2\3\2\3\2\3\2\3\2"+
		"\3\2\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4w\n\4\f\4\16\4"+
		"z\13\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7"+
		"\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3"+
		"\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3"+
		"\r\3\r\3\r\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\22\3\22"+
		"\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\30"+
		"\3\31\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36"+
		"\3\37\3\37\3\37\3 \3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'"+
		"\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3*\3*\7*\u00f9\n*\f*\16*\u00fc\13*\3"+
		"+\3+\3+\3+\5+\u0102\n+\3+\3+\3,\5,\u0107\n,\3,\3,\7,\u010b\n,\f,\16,\u010e"+
		"\13,\3,\5,\u0111\n,\3-\3-\7-\u0115\n-\f-\16-\u0118\13-\3.\6.\u011b\n."+
		"\r.\16.\u011c\3.\3.\3/\3/\3/\3/\7/\u0125\n/\f/\16/\u0128\13/\3/\3/\3/"+
		"\3/\3/\3\60\3\60\3\60\3\60\7\60\u0133\n\60\f\60\16\60\u0136\13\60\3\60"+
		"\3\60\3\61\3\61\7\61\u013c\n\61\f\61\16\61\u013f\13\61\3\61\3\61\4\u0126"+
		"\u013d\2\62\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33"+
		"\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67"+
		"\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62\3\2\n\4\2\f"+
		"\f\17\17\3\2\63;\3\2\62;\3\2\2\u0081\3\2//\5\2C\\aac|\6\2\62;C\\aac|\5"+
		"\2\13\f\17\17\"\"\2\u014c\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2"+
		"\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2"+
		"\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3"+
		"\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2"+
		"\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67"+
		"\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2"+
		"\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2"+
		"\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]"+
		"\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\3c\3\2\2\2\5j\3\2\2\2\7l\3\2\2\2\t}\3\2"+
		"\2\2\13\u0081\3\2\2\2\r\u0086\3\2\2\2\17\u008b\3\2\2\2\21\u0091\3\2\2"+
		"\2\23\u009a\3\2\2\2\25\u009d\3\2\2\2\27\u00a2\3\2\2\2\31\u00a9\3\2\2\2"+
		"\33\u00af\3\2\2\2\35\u00b1\3\2\2\2\37\u00b4\3\2\2\2!\u00b7\3\2\2\2#\u00b9"+
		"\3\2\2\2%\u00bb\3\2\2\2\'\u00bd\3\2\2\2)\u00bf\3\2\2\2+\u00c1\3\2\2\2"+
		"-\u00c3\3\2\2\2/\u00c6\3\2\2\2\61\u00c9\3\2\2\2\63\u00cc\3\2\2\2\65\u00cf"+
		"\3\2\2\2\67\u00d1\3\2\2\29\u00d3\3\2\2\2;\u00d5\3\2\2\2=\u00d7\3\2\2\2"+
		"?\u00da\3\2\2\2A\u00dd\3\2\2\2C\u00df\3\2\2\2E\u00e1\3\2\2\2G\u00e3\3"+
		"\2\2\2I\u00e5\3\2\2\2K\u00e7\3\2\2\2M\u00e9\3\2\2\2O\u00eb\3\2\2\2Q\u00f0"+
		"\3\2\2\2S\u00f6\3\2\2\2U\u00fd\3\2\2\2W\u0110\3\2\2\2Y\u0112\3\2\2\2["+
		"\u011a\3\2\2\2]\u0120\3\2\2\2_\u012e\3\2\2\2a\u0139\3\2\2\2cd\7u\2\2d"+
		"e\7k\2\2ef\7|\2\2fg\7g\2\2gh\7q\2\2hi\7h\2\2i\4\3\2\2\2jk\7.\2\2k\6\3"+
		"\2\2\2lm\7%\2\2mn\7k\2\2no\7p\2\2op\7e\2\2pq\7n\2\2qr\7w\2\2rs\7f\2\2"+
		"st\7g\2\2tx\3\2\2\2uw\n\2\2\2vu\3\2\2\2wz\3\2\2\2xv\3\2\2\2xy\3\2\2\2"+
		"y{\3\2\2\2zx\3\2\2\2{|\b\4\2\2|\b\3\2\2\2}~\7k\2\2~\177\7p\2\2\177\u0080"+
		"\7v\2\2\u0080\n\3\2\2\2\u0081\u0082\7x\2\2\u0082\u0083\7q\2\2\u0083\u0084"+
		"\7k\2\2\u0084\u0085\7f\2\2\u0085\f\3\2\2\2\u0086\u0087\7e\2\2\u0087\u0088"+
		"\7j\2\2\u0088\u0089\7c\2\2\u0089\u008a\7t\2\2\u008a\16\3\2\2\2\u008b\u008c"+
		"\7d\2\2\u008c\u008d\7t\2\2\u008d\u008e\7g\2\2\u008e\u008f\7c\2\2\u008f"+
		"\u0090\7m\2\2\u0090\20\3\2\2\2\u0091\u0092\7e\2\2\u0092\u0093\7q\2\2\u0093"+
		"\u0094\7p\2\2\u0094\u0095\7v\2\2\u0095\u0096\7k\2\2\u0096\u0097\7p\2\2"+
		"\u0097\u0098\7w\2\2\u0098\u0099\7g\2\2\u0099\22\3\2\2\2\u009a\u009b\7"+
		"k\2\2\u009b\u009c\7h\2\2\u009c\24\3\2\2\2\u009d\u009e\7g\2\2\u009e\u009f"+
		"\7n\2\2\u009f\u00a0\7u\2\2\u00a0\u00a1\7g\2\2\u00a1\26\3\2\2\2\u00a2\u00a3"+
		"\7t\2\2\u00a3\u00a4\7g\2\2\u00a4\u00a5\7v\2\2\u00a5\u00a6\7w\2\2\u00a6"+
		"\u00a7\7t\2\2\u00a7\u00a8\7p\2\2\u00a8\30\3\2\2\2\u00a9\u00aa\7y\2\2\u00aa"+
		"\u00ab\7j\2\2\u00ab\u00ac\7k\2\2\u00ac\u00ad\7n\2\2\u00ad\u00ae\7g\2\2"+
		"\u00ae\32\3\2\2\2\u00af\u00b0\7-\2\2\u00b0\34\3\2\2\2\u00b1\u00b2\7-\2"+
		"\2\u00b2\u00b3\7-\2\2\u00b3\36\3\2\2\2\u00b4\u00b5\7/\2\2\u00b5\u00b6"+
		"\7/\2\2\u00b6 \3\2\2\2\u00b7\u00b8\7/\2\2\u00b8\"\3\2\2\2\u00b9\u00ba"+
		"\7,\2\2\u00ba$\3\2\2\2\u00bb\u00bc\7\61\2\2\u00bc&\3\2\2\2\u00bd\u00be"+
		"\7\'\2\2\u00be(\3\2\2\2\u00bf\u00c0\7@\2\2\u00c0*\3\2\2\2\u00c1\u00c2"+
		"\7>\2\2\u00c2,\3\2\2\2\u00c3\u00c4\7@\2\2\u00c4\u00c5\7?\2\2\u00c5.\3"+
		"\2\2\2\u00c6\u00c7\7>\2\2\u00c7\u00c8\7?\2\2\u00c8\60\3\2\2\2\u00c9\u00ca"+
		"\7?\2\2\u00ca\u00cb\7?\2\2\u00cb\62\3\2\2\2\u00cc\u00cd\7#\2\2\u00cd\u00ce"+
		"\7?\2\2\u00ce\64\3\2\2\2\u00cf\u00d0\7#\2\2\u00d0\66\3\2\2\2\u00d1\u00d2"+
		"\7?\2\2\u00d28\3\2\2\2\u00d3\u00d4\7(\2\2\u00d4:\3\2\2\2\u00d5\u00d6\7"+
		"~\2\2\u00d6<\3\2\2\2\u00d7\u00d8\7(\2\2\u00d8\u00d9\7(\2\2\u00d9>\3\2"+
		"\2\2\u00da\u00db\7~\2\2\u00db\u00dc\7~\2\2\u00dc@\3\2\2\2\u00dd\u00de"+
		"\7=\2\2\u00deB\3\2\2\2\u00df\u00e0\7*\2\2\u00e0D\3\2\2\2\u00e1\u00e2\7"+
		"+\2\2\u00e2F\3\2\2\2\u00e3\u00e4\7]\2\2\u00e4H\3\2\2\2\u00e5\u00e6\7_"+
		"\2\2\u00e6J\3\2\2\2\u00e7\u00e8\7}\2\2\u00e8L\3\2\2\2\u00e9\u00ea\7\177"+
		"\2\2\u00eaN\3\2\2\2\u00eb\u00ec\7v\2\2\u00ec\u00ed\7t\2\2\u00ed\u00ee"+
		"\7w\2\2\u00ee\u00ef\7g\2\2\u00efP\3\2\2\2\u00f0\u00f1\7h\2\2\u00f1\u00f2"+
		"\7c\2\2\u00f2\u00f3\7n\2\2\u00f3\u00f4\7u\2\2\u00f4\u00f5\7g\2\2\u00f5"+
		"R\3\2\2\2\u00f6\u00fa\t\3\2\2\u00f7\u00f9\t\4\2\2\u00f8\u00f7\3\2\2\2"+
		"\u00f9\u00fc\3\2\2\2\u00fa\u00f8\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fbT\3"+
		"\2\2\2\u00fc\u00fa\3\2\2\2\u00fd\u0101\7)\2\2\u00fe\u0102\t\5\2\2\u00ff"+
		"\u0100\7^\2\2\u0100\u0102\7\62\2\2\u0101\u00fe\3\2\2\2\u0101\u00ff\3\2"+
		"\2\2\u0102\u0103\3\2\2\2\u0103\u0104\7)\2\2\u0104V\3\2\2\2\u0105\u0107"+
		"\t\6\2\2\u0106\u0105\3\2\2\2\u0106\u0107\3\2\2\2\u0107\u0108\3\2\2\2\u0108"+
		"\u010c\t\3\2\2\u0109\u010b\t\4\2\2\u010a\u0109\3\2\2\2\u010b\u010e\3\2"+
		"\2\2\u010c\u010a\3\2\2\2\u010c\u010d\3\2\2\2\u010d\u0111\3\2\2\2\u010e"+
		"\u010c\3\2\2\2\u010f\u0111\7\62\2\2\u0110\u0106\3\2\2\2\u0110\u010f\3"+
		"\2\2\2\u0111X\3\2\2\2\u0112\u0116\t\7\2\2\u0113\u0115\t\b\2\2\u0114\u0113"+
		"\3\2\2\2\u0115\u0118\3\2\2\2\u0116\u0114\3\2\2\2\u0116\u0117\3\2\2\2\u0117"+
		"Z\3\2\2\2\u0118\u0116\3\2\2\2\u0119\u011b\t\t\2\2\u011a\u0119\3\2\2\2"+
		"\u011b\u011c\3\2\2\2\u011c\u011a\3\2\2\2\u011c\u011d\3\2\2\2\u011d\u011e"+
		"\3\2\2\2\u011e\u011f\b.\2\2\u011f\\\3\2\2\2\u0120\u0121\7\61\2\2\u0121"+
		"\u0122\7,\2\2\u0122\u0126\3\2\2\2\u0123\u0125\13\2\2\2\u0124\u0123\3\2"+
		"\2\2\u0125\u0128\3\2\2\2\u0126\u0127\3\2\2\2\u0126\u0124\3\2\2\2\u0127"+
		"\u0129\3\2\2\2\u0128\u0126\3\2\2\2\u0129\u012a\7,\2\2\u012a\u012b\7\61"+
		"\2\2\u012b\u012c\3\2\2\2\u012c\u012d\b/\2\2\u012d^\3\2\2\2\u012e\u012f"+
		"\7\61\2\2\u012f\u0130\7\61\2\2\u0130\u0134\3\2\2\2\u0131\u0133\n\2\2\2"+
		"\u0132\u0131\3\2\2\2\u0133\u0136\3\2\2\2\u0134\u0132\3\2\2\2\u0134\u0135"+
		"\3\2\2\2\u0135\u0137\3\2\2\2\u0136\u0134\3\2\2\2\u0137\u0138\b\60\2\2"+
		"\u0138`\3\2\2\2\u0139\u013d\7$\2\2\u013a\u013c\13\2\2\2\u013b\u013a\3"+
		"\2\2\2\u013c\u013f\3\2\2\2\u013d\u013e\3\2\2\2\u013d\u013b\3\2\2\2\u013e"+
		"\u0140\3\2\2\2\u013f\u013d\3\2\2\2\u0140\u0141\7$\2\2\u0141b\3\2\2\2\16"+
		"\2x\u00fa\u0101\u0106\u010c\u0110\u0116\u011c\u0126\u0134\u013d\3\b\2"+
		"\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}