// Generated from e:\Tsinghua\课程\大三上\汇编与编译原理\作业\编译\编译小组作业\src\LLVM\antlr\src\naiveC.g4 by ANTLR 4.8
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class naiveCParser extends Parser {
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
	public static final int
		RULE_prog = 0, RULE_r = 1, RULE_realTypeID = 2, RULE_realTypeIDPointer = 3, 
		RULE_typeIdentifier = 4, RULE_typeIdentifierPointer = 5, RULE_sizeof = 6, 
		RULE_boolExpr = 7, RULE_idList = 8, RULE_arithmeticOperator = 9, RULE_expr = 10, 
		RULE_conditionOperator = 11, RULE_conditionExpr = 12, RULE_assignment = 13, 
		RULE_definition = 14, RULE_callProc = 15, RULE_returnLine = 16, RULE_param = 17, 
		RULE_paramList = 18, RULE_defineParam = 19, RULE_defineParamList = 20, 
		RULE_block = 21, RULE_breakLine = 22, RULE_continueLine = 23, RULE_statements = 24, 
		RULE_whileBlock = 25, RULE_ifBlock = 26, RULE_functionCall = 27, RULE_functionDeclare = 28, 
		RULE_functionDefine = 29;
	private static String[] makeRuleNames() {
		return new String[] {
			"prog", "r", "realTypeID", "realTypeIDPointer", "typeIdentifier", "typeIdentifierPointer", 
			"sizeof", "boolExpr", "idList", "arithmeticOperator", "expr", "conditionOperator", 
			"conditionExpr", "assignment", "definition", "callProc", "returnLine", 
			"param", "paramList", "defineParam", "defineParamList", "block", "breakLine", 
			"continueLine", "statements", "whileBlock", "ifBlock", "functionCall", 
			"functionDeclare", "functionDefine"
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

	@Override
	public String getGrammarFileName() { return "naiveC.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public naiveCParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgContext extends ParserRuleContext {
		public RContext r() {
			return getRuleContext(RContext.class,0);
		}
		public ProgContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prog; }
	}

	public final ProgContext prog() throws RecognitionException {
		ProgContext _localctx = new ProgContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_prog);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(60);
			r(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class RContext extends ParserRuleContext {
		public FunctionCallContext functionCall() {
			return getRuleContext(FunctionCallContext.class,0);
		}
		public FunctionDeclareContext functionDeclare() {
			return getRuleContext(FunctionDeclareContext.class,0);
		}
		public FunctionDefineContext functionDefine() {
			return getRuleContext(FunctionDefineContext.class,0);
		}
		public RContext r() {
			return getRuleContext(RContext.class,0);
		}
		public RContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_r; }
	}

	public final RContext r() throws RecognitionException {
		return r(0);
	}

	private RContext r(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		RContext _localctx = new RContext(_ctx, _parentState);
		RContext _prevctx = _localctx;
		int _startState = 2;
		enterRecursionRule(_localctx, 2, RULE_r, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(66);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				{
				setState(63);
				functionCall();
				}
				break;
			case 2:
				{
				setState(64);
				functionDeclare();
				}
				break;
			case 3:
				{
				setState(65);
				functionDefine();
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(76);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(74);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
					case 1:
						{
						_localctx = new RContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_r);
						setState(68);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(69);
						functionCall();
						}
						break;
					case 2:
						{
						_localctx = new RContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_r);
						setState(70);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(71);
						functionDefine();
						}
						break;
					case 3:
						{
						_localctx = new RContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_r);
						setState(72);
						if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
						setState(73);
						functionDeclare();
						}
						break;
					}
					} 
				}
				setState(78);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class RealTypeIDContext extends ParserRuleContext {
		public RealTypeIDContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_realTypeID; }
	 
		public RealTypeIDContext() { }
		public void copyFrom(RealTypeIDContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class RealTypeIntContext extends RealTypeIDContext {
		public TerminalNode TypeInt() { return getToken(naiveCParser.TypeInt, 0); }
		public RealTypeIntContext(RealTypeIDContext ctx) { copyFrom(ctx); }
	}
	public static class RealTypeCharContext extends RealTypeIDContext {
		public TerminalNode TypeChar() { return getToken(naiveCParser.TypeChar, 0); }
		public RealTypeCharContext(RealTypeIDContext ctx) { copyFrom(ctx); }
	}

	public final RealTypeIDContext realTypeID() throws RecognitionException {
		RealTypeIDContext _localctx = new RealTypeIDContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_realTypeID);
		try {
			setState(81);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case TypeChar:
				_localctx = new RealTypeCharContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(79);
				match(TypeChar);
				}
				break;
			case TypeInt:
				_localctx = new RealTypeIntContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(80);
				match(TypeInt);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class RealTypeIDPointerContext extends ParserRuleContext {
		public RealTypeIDContext realTypeID() {
			return getRuleContext(RealTypeIDContext.class,0);
		}
		public TerminalNode MUL() { return getToken(naiveCParser.MUL, 0); }
		public RealTypeIDPointerContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_realTypeIDPointer; }
	}

	public final RealTypeIDPointerContext realTypeIDPointer() throws RecognitionException {
		RealTypeIDPointerContext _localctx = new RealTypeIDPointerContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_realTypeIDPointer);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(83);
			realTypeID();
			setState(84);
			match(MUL);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TypeIdentifierContext extends ParserRuleContext {
		public TypeIdentifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typeIdentifier; }
	 
		public TypeIdentifierContext() { }
		public void copyFrom(TypeIdentifierContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class TypeCharContext extends TypeIdentifierContext {
		public TerminalNode TypeChar() { return getToken(naiveCParser.TypeChar, 0); }
		public TypeCharContext(TypeIdentifierContext ctx) { copyFrom(ctx); }
	}
	public static class TypeVoidContext extends TypeIdentifierContext {
		public TerminalNode TypeVoid() { return getToken(naiveCParser.TypeVoid, 0); }
		public TypeVoidContext(TypeIdentifierContext ctx) { copyFrom(ctx); }
	}
	public static class TypeIntContext extends TypeIdentifierContext {
		public TerminalNode TypeInt() { return getToken(naiveCParser.TypeInt, 0); }
		public TypeIntContext(TypeIdentifierContext ctx) { copyFrom(ctx); }
	}

	public final TypeIdentifierContext typeIdentifier() throws RecognitionException {
		TypeIdentifierContext _localctx = new TypeIdentifierContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_typeIdentifier);
		try {
			setState(89);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case TypeInt:
				_localctx = new TypeIntContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(86);
				match(TypeInt);
				}
				break;
			case TypeVoid:
				_localctx = new TypeVoidContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(87);
				match(TypeVoid);
				}
				break;
			case TypeChar:
				_localctx = new TypeCharContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(88);
				match(TypeChar);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TypeIdentifierPointerContext extends ParserRuleContext {
		public TypeIdentifierContext typeIdentifier() {
			return getRuleContext(TypeIdentifierContext.class,0);
		}
		public TerminalNode MUL() { return getToken(naiveCParser.MUL, 0); }
		public TypeIdentifierPointerContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typeIdentifierPointer; }
	}

	public final TypeIdentifierPointerContext typeIdentifierPointer() throws RecognitionException {
		TypeIdentifierPointerContext _localctx = new TypeIdentifierPointerContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_typeIdentifierPointer);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(91);
			typeIdentifier();
			setState(92);
			match(MUL);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SizeofContext extends ParserRuleContext {
		public SizeofContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sizeof; }
	}

	public final SizeofContext sizeof() throws RecognitionException {
		SizeofContext _localctx = new SizeofContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_sizeof);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(94);
			match(T__0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BoolExprContext extends ParserRuleContext {
		public TerminalNode TRUE() { return getToken(naiveCParser.TRUE, 0); }
		public TerminalNode FALSE() { return getToken(naiveCParser.FALSE, 0); }
		public BoolExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_boolExpr; }
	}

	public final BoolExprContext boolExpr() throws RecognitionException {
		BoolExprContext _localctx = new BoolExprContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_boolExpr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(96);
			_la = _input.LA(1);
			if ( !(_la==TRUE || _la==FALSE) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IdListContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(naiveCParser.ID, 0); }
		public IdListContext idList() {
			return getRuleContext(IdListContext.class,0);
		}
		public IdListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_idList; }
	}

	public final IdListContext idList() throws RecognitionException {
		IdListContext _localctx = new IdListContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_idList);
		try {
			setState(102);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(98);
				match(ID);
				setState(99);
				match(T__1);
				setState(100);
				idList();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(101);
				match(ID);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ArithmeticOperatorContext extends ParserRuleContext {
		public TerminalNode ADD() { return getToken(naiveCParser.ADD, 0); }
		public TerminalNode SUB() { return getToken(naiveCParser.SUB, 0); }
		public TerminalNode MUL() { return getToken(naiveCParser.MUL, 0); }
		public TerminalNode DIV() { return getToken(naiveCParser.DIV, 0); }
		public TerminalNode MOD() { return getToken(naiveCParser.MOD, 0); }
		public TerminalNode ArithmeticAnd() { return getToken(naiveCParser.ArithmeticAnd, 0); }
		public TerminalNode ArithmeticOR() { return getToken(naiveCParser.ArithmeticOR, 0); }
		public ArithmeticOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arithmeticOperator; }
	}

	public final ArithmeticOperatorContext arithmeticOperator() throws RecognitionException {
		ArithmeticOperatorContext _localctx = new ArithmeticOperatorContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_arithmeticOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(104);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << ADD) | (1L << SUB) | (1L << MUL) | (1L << DIV) | (1L << MOD) | (1L << ArithmeticAnd) | (1L << ArithmeticOR))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExprContext extends ParserRuleContext {
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	 
		public ExprContext() { }
		public void copyFrom(ExprContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class PositiveINTContext extends ExprContext {
		public TerminalNode PositiveINT() { return getToken(naiveCParser.PositiveINT, 0); }
		public PositiveINTContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class TrueFalseContext extends ExprContext {
		public BoolExprContext boolExpr() {
			return getRuleContext(BoolExprContext.class,0);
		}
		public TrueFalseContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class MulDivContext extends ExprContext {
		public Token op;
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode MUL() { return getToken(naiveCParser.MUL, 0); }
		public TerminalNode DIV() { return getToken(naiveCParser.DIV, 0); }
		public MulDivContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class AddSubContext extends ExprContext {
		public Token op;
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode ADD() { return getToken(naiveCParser.ADD, 0); }
		public TerminalNode SUB() { return getToken(naiveCParser.SUB, 0); }
		public AddSubContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class ParensContext extends ExprContext {
		public TerminalNode LeftParentheses() { return getToken(naiveCParser.LeftParentheses, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode RightParentheses() { return getToken(naiveCParser.RightParentheses, 0); }
		public ParensContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class IntContext extends ExprContext {
		public TerminalNode INT() { return getToken(naiveCParser.INT, 0); }
		public IntContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class NegativeContext extends ExprContext {
		public TerminalNode SUB() { return getToken(naiveCParser.SUB, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public NegativeContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class CharContext extends ExprContext {
		public TerminalNode Char() { return getToken(naiveCParser.Char, 0); }
		public CharContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class GetPContext extends ExprContext {
		public TerminalNode ArithmeticAnd() { return getToken(naiveCParser.ArithmeticAnd, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public GetPContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class TypeCastContext extends ExprContext {
		public TerminalNode LeftParentheses() { return getToken(naiveCParser.LeftParentheses, 0); }
		public TerminalNode RightParentheses() { return getToken(naiveCParser.RightParentheses, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public RealTypeIDPointerContext realTypeIDPointer() {
			return getRuleContext(RealTypeIDPointerContext.class,0);
		}
		public RealTypeIDContext realTypeID() {
			return getRuleContext(RealTypeIDContext.class,0);
		}
		public TypeCastContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class IdContext extends ExprContext {
		public TerminalNode ID() { return getToken(naiveCParser.ID, 0); }
		public IdContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class ArrayVisitContext extends ExprContext {
		public TerminalNode ID() { return getToken(naiveCParser.ID, 0); }
		public TerminalNode LeftBracket() { return getToken(naiveCParser.LeftBracket, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode RightBracket() { return getToken(naiveCParser.RightBracket, 0); }
		public ArrayVisitContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class MakPContext extends ExprContext {
		public TerminalNode MUL() { return getToken(naiveCParser.MUL, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public MakPContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class FCallContext extends ExprContext {
		public FunctionCallContext functionCall() {
			return getRuleContext(FunctionCallContext.class,0);
		}
		public FCallContext(ExprContext ctx) { copyFrom(ctx); }
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 20;
		enterRecursionRule(_localctx, 20, RULE_expr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(136);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				{
				_localctx = new GetPContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(107);
				match(ArithmeticAnd);
				setState(108);
				expr(12);
				}
				break;
			case 2:
				{
				_localctx = new MakPContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(109);
				match(MUL);
				setState(110);
				expr(11);
				}
				break;
			case 3:
				{
				_localctx = new NegativeContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(111);
				match(SUB);
				setState(112);
				expr(10);
				}
				break;
			case 4:
				{
				_localctx = new TypeCastContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(113);
				match(LeftParentheses);
				setState(116);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
				case 1:
					{
					setState(114);
					realTypeIDPointer();
					}
					break;
				case 2:
					{
					setState(115);
					realTypeID();
					}
					break;
				}
				setState(118);
				match(RightParentheses);
				setState(119);
				expr(9);
				}
				break;
			case 5:
				{
				_localctx = new PositiveINTContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(121);
				match(PositiveINT);
				}
				break;
			case 6:
				{
				_localctx = new CharContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(122);
				match(Char);
				}
				break;
			case 7:
				{
				_localctx = new IntContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(123);
				match(INT);
				}
				break;
			case 8:
				{
				_localctx = new IdContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(124);
				match(ID);
				}
				break;
			case 9:
				{
				_localctx = new FCallContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(125);
				functionCall();
				}
				break;
			case 10:
				{
				_localctx = new TrueFalseContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(126);
				boolExpr();
				}
				break;
			case 11:
				{
				_localctx = new ArrayVisitContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(127);
				match(ID);
				setState(128);
				match(LeftBracket);
				setState(129);
				expr(0);
				setState(130);
				match(RightBracket);
				}
				break;
			case 12:
				{
				_localctx = new ParensContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(132);
				match(LeftParentheses);
				setState(133);
				expr(0);
				setState(134);
				match(RightParentheses);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(146);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,9,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(144);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
					case 1:
						{
						_localctx = new MulDivContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(138);
						if (!(precpred(_ctx, 14))) throw new FailedPredicateException(this, "precpred(_ctx, 14)");
						setState(139);
						((MulDivContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==MUL || _la==DIV) ) {
							((MulDivContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(140);
						expr(15);
						}
						break;
					case 2:
						{
						_localctx = new AddSubContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(141);
						if (!(precpred(_ctx, 13))) throw new FailedPredicateException(this, "precpred(_ctx, 13)");
						setState(142);
						((AddSubContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==ADD || _la==SUB) ) {
							((AddSubContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(143);
						expr(14);
						}
						break;
					}
					} 
				}
				setState(148);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,9,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class ConditionOperatorContext extends ParserRuleContext {
		public TerminalNode Greater() { return getToken(naiveCParser.Greater, 0); }
		public TerminalNode GreaterEqual() { return getToken(naiveCParser.GreaterEqual, 0); }
		public TerminalNode Less() { return getToken(naiveCParser.Less, 0); }
		public TerminalNode LessEqual() { return getToken(naiveCParser.LessEqual, 0); }
		public TerminalNode Equal() { return getToken(naiveCParser.Equal, 0); }
		public ConditionOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_conditionOperator; }
	}

	public final ConditionOperatorContext conditionOperator() throws RecognitionException {
		ConditionOperatorContext _localctx = new ConditionOperatorContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_conditionOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(149);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << Greater) | (1L << Less) | (1L << GreaterEqual) | (1L << LessEqual) | (1L << Equal))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ConditionExprContext extends ParserRuleContext {
		public ConditionExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_conditionExpr; }
	 
		public ConditionExprContext() { }
		public void copyFrom(ConditionExprContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class CondExpContext extends ConditionExprContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public CondExpContext(ConditionExprContext ctx) { copyFrom(ctx); }
	}
	public static class OrContext extends ConditionExprContext {
		public List<ConditionExprContext> conditionExpr() {
			return getRuleContexts(ConditionExprContext.class);
		}
		public ConditionExprContext conditionExpr(int i) {
			return getRuleContext(ConditionExprContext.class,i);
		}
		public TerminalNode LogicOR() { return getToken(naiveCParser.LogicOR, 0); }
		public OrContext(ConditionExprContext ctx) { copyFrom(ctx); }
	}
	public static class AndContext extends ConditionExprContext {
		public List<ConditionExprContext> conditionExpr() {
			return getRuleContexts(ConditionExprContext.class);
		}
		public ConditionExprContext conditionExpr(int i) {
			return getRuleContext(ConditionExprContext.class,i);
		}
		public TerminalNode LogicAnd() { return getToken(naiveCParser.LogicAnd, 0); }
		public AndContext(ConditionExprContext ctx) { copyFrom(ctx); }
	}
	public static class CondOpContext extends ConditionExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public ConditionOperatorContext conditionOperator() {
			return getRuleContext(ConditionOperatorContext.class,0);
		}
		public CondOpContext(ConditionExprContext ctx) { copyFrom(ctx); }
	}
	public static class CondParenContext extends ConditionExprContext {
		public TerminalNode LeftParentheses() { return getToken(naiveCParser.LeftParentheses, 0); }
		public ConditionExprContext conditionExpr() {
			return getRuleContext(ConditionExprContext.class,0);
		}
		public TerminalNode RightParentheses() { return getToken(naiveCParser.RightParentheses, 0); }
		public CondParenContext(ConditionExprContext ctx) { copyFrom(ctx); }
	}

	public final ConditionExprContext conditionExpr() throws RecognitionException {
		return conditionExpr(0);
	}

	private ConditionExprContext conditionExpr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ConditionExprContext _localctx = new ConditionExprContext(_ctx, _parentState);
		ConditionExprContext _prevctx = _localctx;
		int _startState = 24;
		enterRecursionRule(_localctx, 24, RULE_conditionExpr, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(161);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
			case 1:
				{
				_localctx = new CondParenContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(152);
				match(LeftParentheses);
				setState(153);
				conditionExpr(0);
				setState(154);
				match(RightParentheses);
				}
				break;
			case 2:
				{
				_localctx = new CondOpContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(156);
				expr(0);
				setState(157);
				conditionOperator();
				setState(158);
				expr(0);
				}
				break;
			case 3:
				{
				_localctx = new CondExpContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(160);
				expr(0);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(171);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(169);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
					case 1:
						{
						_localctx = new AndContext(new ConditionExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_conditionExpr);
						setState(163);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(164);
						match(LogicAnd);
						setState(165);
						conditionExpr(6);
						}
						break;
					case 2:
						{
						_localctx = new OrContext(new ConditionExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_conditionExpr);
						setState(166);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(167);
						match(LogicOR);
						setState(168);
						conditionExpr(5);
						}
						break;
					}
					} 
				}
				setState(173);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class AssignmentContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(naiveCParser.ID, 0); }
		public TerminalNode AssignOperator() { return getToken(naiveCParser.AssignOperator, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode Semicolon() { return getToken(naiveCParser.Semicolon, 0); }
		public TerminalNode MUL() { return getToken(naiveCParser.MUL, 0); }
		public TerminalNode LeftBracket() { return getToken(naiveCParser.LeftBracket, 0); }
		public TerminalNode RightBracket() { return getToken(naiveCParser.RightBracket, 0); }
		public AssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignment; }
	}

	public final AssignmentContext assignment() throws RecognitionException {
		AssignmentContext _localctx = new AssignmentContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_assignment);
		try {
			setState(193);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(174);
				match(ID);
				setState(175);
				match(AssignOperator);
				setState(176);
				expr(0);
				setState(177);
				match(Semicolon);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(179);
				match(MUL);
				setState(180);
				match(ID);
				setState(181);
				match(AssignOperator);
				setState(182);
				expr(0);
				setState(183);
				match(Semicolon);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(185);
				match(ID);
				setState(186);
				match(LeftBracket);
				setState(187);
				expr(0);
				setState(188);
				match(RightBracket);
				setState(189);
				match(AssignOperator);
				setState(190);
				expr(0);
				setState(191);
				match(Semicolon);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DefinitionContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(naiveCParser.ID, 0); }
		public TerminalNode Semicolon() { return getToken(naiveCParser.Semicolon, 0); }
		public RealTypeIDContext realTypeID() {
			return getRuleContext(RealTypeIDContext.class,0);
		}
		public RealTypeIDPointerContext realTypeIDPointer() {
			return getRuleContext(RealTypeIDPointerContext.class,0);
		}
		public TerminalNode AssignOperator() { return getToken(naiveCParser.AssignOperator, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode LeftBracket() { return getToken(naiveCParser.LeftBracket, 0); }
		public TerminalNode PositiveINT() { return getToken(naiveCParser.PositiveINT, 0); }
		public TerminalNode RightBracket() { return getToken(naiveCParser.RightBracket, 0); }
		public DefinitionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_definition; }
	}

	public final DefinitionContext definition() throws RecognitionException {
		DefinitionContext _localctx = new DefinitionContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_definition);
		int _la;
		try {
			setState(216);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,17,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(197);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
				case 1:
					{
					setState(195);
					realTypeID();
					}
					break;
				case 2:
					{
					setState(196);
					realTypeIDPointer();
					}
					break;
				}
				setState(199);
				match(ID);
				setState(202);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==AssignOperator) {
					{
					setState(200);
					match(AssignOperator);
					setState(201);
					expr(0);
					}
				}

				setState(204);
				match(Semicolon);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(208);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,16,_ctx) ) {
				case 1:
					{
					setState(206);
					realTypeID();
					}
					break;
				case 2:
					{
					setState(207);
					realTypeIDPointer();
					}
					break;
				}
				setState(210);
				match(ID);
				setState(211);
				match(LeftBracket);
				setState(212);
				match(PositiveINT);
				setState(213);
				match(RightBracket);
				setState(214);
				match(Semicolon);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CallProcContext extends ParserRuleContext {
		public FunctionCallContext functionCall() {
			return getRuleContext(FunctionCallContext.class,0);
		}
		public TerminalNode Semicolon() { return getToken(naiveCParser.Semicolon, 0); }
		public CallProcContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_callProc; }
	}

	public final CallProcContext callProc() throws RecognitionException {
		CallProcContext _localctx = new CallProcContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_callProc);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(218);
			functionCall();
			setState(219);
			match(Semicolon);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ReturnLineContext extends ParserRuleContext {
		public TerminalNode Return() { return getToken(naiveCParser.Return, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode Semicolon() { return getToken(naiveCParser.Semicolon, 0); }
		public ReturnLineContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_returnLine; }
	}

	public final ReturnLineContext returnLine() throws RecognitionException {
		ReturnLineContext _localctx = new ReturnLineContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_returnLine);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(221);
			match(Return);
			setState(222);
			expr(0);
			setState(223);
			match(Semicolon);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ParamContext extends ParserRuleContext {
		public ParamContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_param; }
	 
		public ParamContext() { }
		public void copyFrom(ParamContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class ParamExprContext extends ParamContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public ParamExprContext(ParamContext ctx) { copyFrom(ctx); }
	}
	public static class ParamFuncContext extends ParamContext {
		public FunctionCallContext functionCall() {
			return getRuleContext(FunctionCallContext.class,0);
		}
		public ParamFuncContext(ParamContext ctx) { copyFrom(ctx); }
	}
	public static class ParamStringContext extends ParamContext {
		public TerminalNode String() { return getToken(naiveCParser.String, 0); }
		public ParamStringContext(ParamContext ctx) { copyFrom(ctx); }
	}

	public final ParamContext param() throws RecognitionException {
		ParamContext _localctx = new ParamContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_param);
		try {
			setState(228);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,18,_ctx) ) {
			case 1:
				_localctx = new ParamExprContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(225);
				expr(0);
				}
				break;
			case 2:
				_localctx = new ParamFuncContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(226);
				functionCall();
				}
				break;
			case 3:
				_localctx = new ParamStringContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(227);
				match(String);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ParamListContext extends ParserRuleContext {
		public ParamContext param() {
			return getRuleContext(ParamContext.class,0);
		}
		public ParamListContext paramList() {
			return getRuleContext(ParamListContext.class,0);
		}
		public ParamListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_paramList; }
	}

	public final ParamListContext paramList() throws RecognitionException {
		return paramList(0);
	}

	private ParamListContext paramList(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ParamListContext _localctx = new ParamListContext(_ctx, _parentState);
		ParamListContext _prevctx = _localctx;
		int _startState = 36;
		enterRecursionRule(_localctx, 36, RULE_paramList, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(232);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,19,_ctx) ) {
			case 1:
				{
				setState(231);
				param();
				}
				break;
			}
			}
			_ctx.stop = _input.LT(-1);
			setState(239);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,20,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new ParamListContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_paramList);
					setState(234);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(235);
					match(T__1);
					setState(236);
					param();
					}
					} 
				}
				setState(241);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,20,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class DefineParamContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(naiveCParser.ID, 0); }
		public TypeIdentifierContext typeIdentifier() {
			return getRuleContext(TypeIdentifierContext.class,0);
		}
		public TypeIdentifierPointerContext typeIdentifierPointer() {
			return getRuleContext(TypeIdentifierPointerContext.class,0);
		}
		public DefineParamContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_defineParam; }
	}

	public final DefineParamContext defineParam() throws RecognitionException {
		DefineParamContext _localctx = new DefineParamContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_defineParam);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(244);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,21,_ctx) ) {
			case 1:
				{
				setState(242);
				typeIdentifier();
				}
				break;
			case 2:
				{
				setState(243);
				typeIdentifierPointer();
				}
				break;
			}
			setState(246);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DefineParamListContext extends ParserRuleContext {
		public DefineParamContext defineParam() {
			return getRuleContext(DefineParamContext.class,0);
		}
		public DefineParamListContext defineParamList() {
			return getRuleContext(DefineParamListContext.class,0);
		}
		public DefineParamListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_defineParamList; }
	}

	public final DefineParamListContext defineParamList() throws RecognitionException {
		return defineParamList(0);
	}

	private DefineParamListContext defineParamList(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		DefineParamListContext _localctx = new DefineParamListContext(_ctx, _parentState);
		DefineParamListContext _prevctx = _localctx;
		int _startState = 40;
		enterRecursionRule(_localctx, 40, RULE_defineParamList, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(250);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,22,_ctx) ) {
			case 1:
				{
				setState(249);
				defineParam();
				}
				break;
			}
			}
			_ctx.stop = _input.LT(-1);
			setState(257);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,23,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new DefineParamListContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_defineParamList);
					setState(252);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(253);
					match(T__1);
					setState(254);
					defineParam();
					}
					} 
				}
				setState(259);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,23,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class BlockContext extends ParserRuleContext {
		public TerminalNode LeftBrace() { return getToken(naiveCParser.LeftBrace, 0); }
		public StatementsContext statements() {
			return getRuleContext(StatementsContext.class,0);
		}
		public TerminalNode RightBrace() { return getToken(naiveCParser.RightBrace, 0); }
		public BlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block; }
	}

	public final BlockContext block() throws RecognitionException {
		BlockContext _localctx = new BlockContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_block);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(260);
			match(LeftBrace);
			setState(261);
			statements();
			setState(262);
			match(RightBrace);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BreakLineContext extends ParserRuleContext {
		public TerminalNode Break() { return getToken(naiveCParser.Break, 0); }
		public TerminalNode Semicolon() { return getToken(naiveCParser.Semicolon, 0); }
		public BreakLineContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_breakLine; }
	}

	public final BreakLineContext breakLine() throws RecognitionException {
		BreakLineContext _localctx = new BreakLineContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_breakLine);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(264);
			match(Break);
			setState(265);
			match(Semicolon);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ContinueLineContext extends ParserRuleContext {
		public TerminalNode Continue() { return getToken(naiveCParser.Continue, 0); }
		public TerminalNode Semicolon() { return getToken(naiveCParser.Semicolon, 0); }
		public ContinueLineContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_continueLine; }
	}

	public final ContinueLineContext continueLine() throws RecognitionException {
		ContinueLineContext _localctx = new ContinueLineContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_continueLine);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(267);
			match(Continue);
			setState(268);
			match(Semicolon);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatementsContext extends ParserRuleContext {
		public List<AssignmentContext> assignment() {
			return getRuleContexts(AssignmentContext.class);
		}
		public AssignmentContext assignment(int i) {
			return getRuleContext(AssignmentContext.class,i);
		}
		public List<DefinitionContext> definition() {
			return getRuleContexts(DefinitionContext.class);
		}
		public DefinitionContext definition(int i) {
			return getRuleContext(DefinitionContext.class,i);
		}
		public List<CallProcContext> callProc() {
			return getRuleContexts(CallProcContext.class);
		}
		public CallProcContext callProc(int i) {
			return getRuleContext(CallProcContext.class,i);
		}
		public List<WhileBlockContext> whileBlock() {
			return getRuleContexts(WhileBlockContext.class);
		}
		public WhileBlockContext whileBlock(int i) {
			return getRuleContext(WhileBlockContext.class,i);
		}
		public List<BlockContext> block() {
			return getRuleContexts(BlockContext.class);
		}
		public BlockContext block(int i) {
			return getRuleContext(BlockContext.class,i);
		}
		public List<IfBlockContext> ifBlock() {
			return getRuleContexts(IfBlockContext.class);
		}
		public IfBlockContext ifBlock(int i) {
			return getRuleContext(IfBlockContext.class,i);
		}
		public List<ReturnLineContext> returnLine() {
			return getRuleContexts(ReturnLineContext.class);
		}
		public ReturnLineContext returnLine(int i) {
			return getRuleContext(ReturnLineContext.class,i);
		}
		public List<BreakLineContext> breakLine() {
			return getRuleContexts(BreakLineContext.class);
		}
		public BreakLineContext breakLine(int i) {
			return getRuleContext(BreakLineContext.class,i);
		}
		public List<ContinueLineContext> continueLine() {
			return getRuleContexts(ContinueLineContext.class);
		}
		public ContinueLineContext continueLine(int i) {
			return getRuleContext(ContinueLineContext.class,i);
		}
		public StatementsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statements; }
	}

	public final StatementsContext statements() throws RecognitionException {
		StatementsContext _localctx = new StatementsContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_statements);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(281);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__0) | (1L << TypeInt) | (1L << TypeChar) | (1L << Break) | (1L << Continue) | (1L << If) | (1L << Return) | (1L << While) | (1L << MUL) | (1L << LeftBrace) | (1L << ID))) != 0)) {
				{
				setState(279);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,24,_ctx) ) {
				case 1:
					{
					setState(270);
					assignment();
					}
					break;
				case 2:
					{
					setState(271);
					definition();
					}
					break;
				case 3:
					{
					setState(272);
					callProc();
					}
					break;
				case 4:
					{
					setState(273);
					whileBlock();
					}
					break;
				case 5:
					{
					setState(274);
					block();
					}
					break;
				case 6:
					{
					setState(275);
					ifBlock();
					}
					break;
				case 7:
					{
					setState(276);
					returnLine();
					}
					break;
				case 8:
					{
					setState(277);
					breakLine();
					}
					break;
				case 9:
					{
					setState(278);
					continueLine();
					}
					break;
				}
				}
				setState(283);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class WhileBlockContext extends ParserRuleContext {
		public TerminalNode While() { return getToken(naiveCParser.While, 0); }
		public TerminalNode LeftParentheses() { return getToken(naiveCParser.LeftParentheses, 0); }
		public ConditionExprContext conditionExpr() {
			return getRuleContext(ConditionExprContext.class,0);
		}
		public TerminalNode RightParentheses() { return getToken(naiveCParser.RightParentheses, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public WhileBlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whileBlock; }
	}

	public final WhileBlockContext whileBlock() throws RecognitionException {
		WhileBlockContext _localctx = new WhileBlockContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_whileBlock);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(284);
			match(While);
			setState(285);
			match(LeftParentheses);
			setState(286);
			conditionExpr(0);
			setState(287);
			match(RightParentheses);
			setState(288);
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IfBlockContext extends ParserRuleContext {
		public ConditionExprContext elif_cond;
		public BlockContext else_block;
		public List<TerminalNode> If() { return getTokens(naiveCParser.If); }
		public TerminalNode If(int i) {
			return getToken(naiveCParser.If, i);
		}
		public List<TerminalNode> LeftParentheses() { return getTokens(naiveCParser.LeftParentheses); }
		public TerminalNode LeftParentheses(int i) {
			return getToken(naiveCParser.LeftParentheses, i);
		}
		public List<ConditionExprContext> conditionExpr() {
			return getRuleContexts(ConditionExprContext.class);
		}
		public ConditionExprContext conditionExpr(int i) {
			return getRuleContext(ConditionExprContext.class,i);
		}
		public List<TerminalNode> RightParentheses() { return getTokens(naiveCParser.RightParentheses); }
		public TerminalNode RightParentheses(int i) {
			return getToken(naiveCParser.RightParentheses, i);
		}
		public List<BlockContext> block() {
			return getRuleContexts(BlockContext.class);
		}
		public BlockContext block(int i) {
			return getRuleContext(BlockContext.class,i);
		}
		public List<TerminalNode> Else() { return getTokens(naiveCParser.Else); }
		public TerminalNode Else(int i) {
			return getToken(naiveCParser.Else, i);
		}
		public IfBlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifBlock; }
	}

	public final IfBlockContext ifBlock() throws RecognitionException {
		IfBlockContext _localctx = new IfBlockContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_ifBlock);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(290);
			match(If);
			setState(291);
			match(LeftParentheses);
			setState(292);
			conditionExpr(0);
			setState(293);
			match(RightParentheses);
			setState(294);
			block();
			setState(304);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,26,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(295);
					match(Else);
					setState(296);
					match(If);
					setState(297);
					match(LeftParentheses);
					setState(298);
					((IfBlockContext)_localctx).elif_cond = conditionExpr(0);
					setState(299);
					match(RightParentheses);
					setState(300);
					block();
					}
					} 
				}
				setState(306);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,26,_ctx);
			}
			setState(309);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==Else) {
				{
				setState(307);
				match(Else);
				setState(308);
				((IfBlockContext)_localctx).else_block = block();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FunctionCallContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(naiveCParser.ID, 0); }
		public TerminalNode LeftParentheses() { return getToken(naiveCParser.LeftParentheses, 0); }
		public ParamListContext paramList() {
			return getRuleContext(ParamListContext.class,0);
		}
		public TerminalNode RightParentheses() { return getToken(naiveCParser.RightParentheses, 0); }
		public SizeofContext sizeof() {
			return getRuleContext(SizeofContext.class,0);
		}
		public TypeIdentifierContext typeIdentifier() {
			return getRuleContext(TypeIdentifierContext.class,0);
		}
		public FunctionCallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionCall; }
	}

	public final FunctionCallContext functionCall() throws RecognitionException {
		FunctionCallContext _localctx = new FunctionCallContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_functionCall);
		try {
			setState(321);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(311);
				match(ID);
				setState(312);
				match(LeftParentheses);
				setState(313);
				paramList(0);
				setState(314);
				match(RightParentheses);
				}
				break;
			case T__0:
				enterOuterAlt(_localctx, 2);
				{
				setState(316);
				sizeof();
				setState(317);
				match(LeftParentheses);
				setState(318);
				typeIdentifier();
				setState(319);
				match(RightParentheses);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FunctionDeclareContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(naiveCParser.ID, 0); }
		public TerminalNode LeftParentheses() { return getToken(naiveCParser.LeftParentheses, 0); }
		public DefineParamListContext defineParamList() {
			return getRuleContext(DefineParamListContext.class,0);
		}
		public TerminalNode RightParentheses() { return getToken(naiveCParser.RightParentheses, 0); }
		public TerminalNode Semicolon() { return getToken(naiveCParser.Semicolon, 0); }
		public TypeIdentifierContext typeIdentifier() {
			return getRuleContext(TypeIdentifierContext.class,0);
		}
		public TypeIdentifierPointerContext typeIdentifierPointer() {
			return getRuleContext(TypeIdentifierPointerContext.class,0);
		}
		public FunctionDeclareContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionDeclare; }
	}

	public final FunctionDeclareContext functionDeclare() throws RecognitionException {
		FunctionDeclareContext _localctx = new FunctionDeclareContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_functionDeclare);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(325);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,29,_ctx) ) {
			case 1:
				{
				setState(323);
				typeIdentifier();
				}
				break;
			case 2:
				{
				setState(324);
				typeIdentifierPointer();
				}
				break;
			}
			setState(327);
			match(ID);
			setState(328);
			match(LeftParentheses);
			setState(329);
			defineParamList(0);
			setState(330);
			match(RightParentheses);
			setState(331);
			match(Semicolon);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FunctionDefineContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(naiveCParser.ID, 0); }
		public TerminalNode LeftParentheses() { return getToken(naiveCParser.LeftParentheses, 0); }
		public DefineParamListContext defineParamList() {
			return getRuleContext(DefineParamListContext.class,0);
		}
		public TerminalNode RightParentheses() { return getToken(naiveCParser.RightParentheses, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public TypeIdentifierContext typeIdentifier() {
			return getRuleContext(TypeIdentifierContext.class,0);
		}
		public TypeIdentifierPointerContext typeIdentifierPointer() {
			return getRuleContext(TypeIdentifierPointerContext.class,0);
		}
		public FunctionDefineContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionDefine; }
	}

	public final FunctionDefineContext functionDefine() throws RecognitionException {
		FunctionDefineContext _localctx = new FunctionDefineContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_functionDefine);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(335);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,30,_ctx) ) {
			case 1:
				{
				setState(333);
				typeIdentifier();
				}
				break;
			case 2:
				{
				setState(334);
				typeIdentifierPointer();
				}
				break;
			}
			setState(337);
			match(ID);
			setState(338);
			match(LeftParentheses);
			setState(339);
			defineParamList(0);
			setState(340);
			match(RightParentheses);
			setState(341);
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 1:
			return r_sempred((RContext)_localctx, predIndex);
		case 10:
			return expr_sempred((ExprContext)_localctx, predIndex);
		case 12:
			return conditionExpr_sempred((ConditionExprContext)_localctx, predIndex);
		case 18:
			return paramList_sempred((ParamListContext)_localctx, predIndex);
		case 20:
			return defineParamList_sempred((DefineParamListContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean r_sempred(RContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 3);
		case 1:
			return precpred(_ctx, 2);
		case 2:
			return precpred(_ctx, 1);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 3:
			return precpred(_ctx, 14);
		case 4:
			return precpred(_ctx, 13);
		}
		return true;
	}
	private boolean conditionExpr_sempred(ConditionExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 5:
			return precpred(_ctx, 5);
		case 6:
			return precpred(_ctx, 4);
		}
		return true;
	}
	private boolean paramList_sempred(ParamListContext _localctx, int predIndex) {
		switch (predIndex) {
		case 7:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean defineParamList_sempred(DefineParamListContext _localctx, int predIndex) {
		switch (predIndex) {
		case 8:
			return precpred(_ctx, 2);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\62\u015a\4\2\t\2"+
		"\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\3\2\3\2\3"+
		"\3\3\3\3\3\3\3\5\3E\n\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3M\n\3\f\3\16\3P\13"+
		"\3\3\4\3\4\5\4T\n\4\3\5\3\5\3\5\3\6\3\6\3\6\5\6\\\n\6\3\7\3\7\3\7\3\b"+
		"\3\b\3\t\3\t\3\n\3\n\3\n\3\n\5\ni\n\n\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3"+
		"\f\3\f\3\f\3\f\3\f\5\fw\n\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3"+
		"\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u008b\n\f\3\f\3\f\3\f\3\f\3\f\3\f\7"+
		"\f\u0093\n\f\f\f\16\f\u0096\13\f\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16"+
		"\3\16\3\16\3\16\3\16\5\16\u00a4\n\16\3\16\3\16\3\16\3\16\3\16\3\16\7\16"+
		"\u00ac\n\16\f\16\16\16\u00af\13\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17"+
		"\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u00c4"+
		"\n\17\3\20\3\20\5\20\u00c8\n\20\3\20\3\20\3\20\5\20\u00cd\n\20\3\20\3"+
		"\20\3\20\3\20\5\20\u00d3\n\20\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u00db"+
		"\n\20\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\23\3\23\3\23\5\23\u00e7\n\23"+
		"\3\24\3\24\5\24\u00eb\n\24\3\24\3\24\3\24\7\24\u00f0\n\24\f\24\16\24\u00f3"+
		"\13\24\3\25\3\25\5\25\u00f7\n\25\3\25\3\25\3\26\3\26\5\26\u00fd\n\26\3"+
		"\26\3\26\3\26\7\26\u0102\n\26\f\26\16\26\u0105\13\26\3\27\3\27\3\27\3"+
		"\27\3\30\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3"+
		"\32\3\32\7\32\u011a\n\32\f\32\16\32\u011d\13\32\3\33\3\33\3\33\3\33\3"+
		"\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\7"+
		"\34\u0131\n\34\f\34\16\34\u0134\13\34\3\34\3\34\5\34\u0138\n\34\3\35\3"+
		"\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\5\35\u0144\n\35\3\36\3\36"+
		"\5\36\u0148\n\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\5\37\u0152\n"+
		"\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\2\7\4\26\32&* \2\4\6\b\n\f\16\20"+
		"\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<\2\7\3\2)*\5\2\17\17\22\25"+
		"\36\37\3\2\23\24\4\2\17\17\22\22\3\2\26\32\2\u0171\2>\3\2\2\2\4D\3\2\2"+
		"\2\6S\3\2\2\2\bU\3\2\2\2\n[\3\2\2\2\f]\3\2\2\2\16`\3\2\2\2\20b\3\2\2\2"+
		"\22h\3\2\2\2\24j\3\2\2\2\26\u008a\3\2\2\2\30\u0097\3\2\2\2\32\u00a3\3"+
		"\2\2\2\34\u00c3\3\2\2\2\36\u00da\3\2\2\2 \u00dc\3\2\2\2\"\u00df\3\2\2"+
		"\2$\u00e6\3\2\2\2&\u00e8\3\2\2\2(\u00f6\3\2\2\2*\u00fa\3\2\2\2,\u0106"+
		"\3\2\2\2.\u010a\3\2\2\2\60\u010d\3\2\2\2\62\u011b\3\2\2\2\64\u011e\3\2"+
		"\2\2\66\u0124\3\2\2\28\u0143\3\2\2\2:\u0147\3\2\2\2<\u0151\3\2\2\2>?\5"+
		"\4\3\2?\3\3\2\2\2@A\b\3\1\2AE\58\35\2BE\5:\36\2CE\5<\37\2D@\3\2\2\2DB"+
		"\3\2\2\2DC\3\2\2\2EN\3\2\2\2FG\f\5\2\2GM\58\35\2HI\f\4\2\2IM\5<\37\2J"+
		"K\f\3\2\2KM\5:\36\2LF\3\2\2\2LH\3\2\2\2LJ\3\2\2\2MP\3\2\2\2NL\3\2\2\2"+
		"NO\3\2\2\2O\5\3\2\2\2PN\3\2\2\2QT\7\b\2\2RT\7\6\2\2SQ\3\2\2\2SR\3\2\2"+
		"\2T\7\3\2\2\2UV\5\6\4\2VW\7\23\2\2W\t\3\2\2\2X\\\7\6\2\2Y\\\7\7\2\2Z\\"+
		"\7\b\2\2[X\3\2\2\2[Y\3\2\2\2[Z\3\2\2\2\\\13\3\2\2\2]^\5\n\6\2^_\7\23\2"+
		"\2_\r\3\2\2\2`a\7\3\2\2a\17\3\2\2\2bc\t\2\2\2c\21\3\2\2\2de\7.\2\2ef\7"+
		"\4\2\2fi\5\22\n\2gi\7.\2\2hd\3\2\2\2hg\3\2\2\2i\23\3\2\2\2jk\t\3\2\2k"+
		"\25\3\2\2\2lm\b\f\1\2mn\7\36\2\2n\u008b\5\26\f\16op\7\23\2\2p\u008b\5"+
		"\26\f\rqr\7\22\2\2r\u008b\5\26\f\fsv\7#\2\2tw\5\b\5\2uw\5\6\4\2vt\3\2"+
		"\2\2vu\3\2\2\2wx\3\2\2\2xy\7$\2\2yz\5\26\f\13z\u008b\3\2\2\2{\u008b\7"+
		"+\2\2|\u008b\7,\2\2}\u008b\7-\2\2~\u008b\7.\2\2\177\u008b\58\35\2\u0080"+
		"\u008b\5\20\t\2\u0081\u0082\7.\2\2\u0082\u0083\7%\2\2\u0083\u0084\5\26"+
		"\f\2\u0084\u0085\7&\2\2\u0085\u008b\3\2\2\2\u0086\u0087\7#\2\2\u0087\u0088"+
		"\5\26\f\2\u0088\u0089\7$\2\2\u0089\u008b\3\2\2\2\u008al\3\2\2\2\u008a"+
		"o\3\2\2\2\u008aq\3\2\2\2\u008as\3\2\2\2\u008a{\3\2\2\2\u008a|\3\2\2\2"+
		"\u008a}\3\2\2\2\u008a~\3\2\2\2\u008a\177\3\2\2\2\u008a\u0080\3\2\2\2\u008a"+
		"\u0081\3\2\2\2\u008a\u0086\3\2\2\2\u008b\u0094\3\2\2\2\u008c\u008d\f\20"+
		"\2\2\u008d\u008e\t\4\2\2\u008e\u0093\5\26\f\21\u008f\u0090\f\17\2\2\u0090"+
		"\u0091\t\5\2\2\u0091\u0093\5\26\f\20\u0092\u008c\3\2\2\2\u0092\u008f\3"+
		"\2\2\2\u0093\u0096\3\2\2\2\u0094\u0092\3\2\2\2\u0094\u0095\3\2\2\2\u0095"+
		"\27\3\2\2\2\u0096\u0094\3\2\2\2\u0097\u0098\t\6\2\2\u0098\31\3\2\2\2\u0099"+
		"\u009a\b\16\1\2\u009a\u009b\7#\2\2\u009b\u009c\5\32\16\2\u009c\u009d\7"+
		"$\2\2\u009d\u00a4\3\2\2\2\u009e\u009f\5\26\f\2\u009f\u00a0\5\30\r\2\u00a0"+
		"\u00a1\5\26\f\2\u00a1\u00a4\3\2\2\2\u00a2\u00a4\5\26\f\2\u00a3\u0099\3"+
		"\2\2\2\u00a3\u009e\3\2\2\2\u00a3\u00a2\3\2\2\2\u00a4\u00ad\3\2\2\2\u00a5"+
		"\u00a6\f\7\2\2\u00a6\u00a7\7 \2\2\u00a7\u00ac\5\32\16\b\u00a8\u00a9\f"+
		"\6\2\2\u00a9\u00aa\7!\2\2\u00aa\u00ac\5\32\16\7\u00ab\u00a5\3\2\2\2\u00ab"+
		"\u00a8\3\2\2\2\u00ac\u00af\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ad\u00ae\3\2"+
		"\2\2\u00ae\33\3\2\2\2\u00af\u00ad\3\2\2\2\u00b0\u00b1\7.\2\2\u00b1\u00b2"+
		"\7\35\2\2\u00b2\u00b3\5\26\f\2\u00b3\u00b4\7\"\2\2\u00b4\u00c4\3\2\2\2"+
		"\u00b5\u00b6\7\23\2\2\u00b6\u00b7\7.\2\2\u00b7\u00b8\7\35\2\2\u00b8\u00b9"+
		"\5\26\f\2\u00b9\u00ba\7\"\2\2\u00ba\u00c4\3\2\2\2\u00bb\u00bc\7.\2\2\u00bc"+
		"\u00bd\7%\2\2\u00bd\u00be\5\26\f\2\u00be\u00bf\7&\2\2\u00bf\u00c0\7\35"+
		"\2\2\u00c0\u00c1\5\26\f\2\u00c1\u00c2\7\"\2\2\u00c2\u00c4\3\2\2\2\u00c3"+
		"\u00b0\3\2\2\2\u00c3\u00b5\3\2\2\2\u00c3\u00bb\3\2\2\2\u00c4\35\3\2\2"+
		"\2\u00c5\u00c8\5\6\4\2\u00c6\u00c8\5\b\5\2\u00c7\u00c5\3\2\2\2\u00c7\u00c6"+
		"\3\2\2\2\u00c8\u00c9\3\2\2\2\u00c9\u00cc\7.\2\2\u00ca\u00cb\7\35\2\2\u00cb"+
		"\u00cd\5\26\f\2\u00cc\u00ca\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd\u00ce\3"+
		"\2\2\2\u00ce\u00cf\7\"\2\2\u00cf\u00db\3\2\2\2\u00d0\u00d3\5\6\4\2\u00d1"+
		"\u00d3\5\b\5\2\u00d2\u00d0\3\2\2\2\u00d2\u00d1\3\2\2\2\u00d3\u00d4\3\2"+
		"\2\2\u00d4\u00d5\7.\2\2\u00d5\u00d6\7%\2\2\u00d6\u00d7\7+\2\2\u00d7\u00d8"+
		"\7&\2\2\u00d8\u00d9\7\"\2\2\u00d9\u00db\3\2\2\2\u00da\u00c7\3\2\2\2\u00da"+
		"\u00d2\3\2\2\2\u00db\37\3\2\2\2\u00dc\u00dd\58\35\2\u00dd\u00de\7\"\2"+
		"\2\u00de!\3\2\2\2\u00df\u00e0\7\r\2\2\u00e0\u00e1\5\26\f\2\u00e1\u00e2"+
		"\7\"\2\2\u00e2#\3\2\2\2\u00e3\u00e7\5\26\f\2\u00e4\u00e7\58\35\2\u00e5"+
		"\u00e7\7\62\2\2\u00e6\u00e3\3\2\2\2\u00e6\u00e4\3\2\2\2\u00e6\u00e5\3"+
		"\2\2\2\u00e7%\3\2\2\2\u00e8\u00ea\b\24\1\2\u00e9\u00eb\5$\23\2\u00ea\u00e9"+
		"\3\2\2\2\u00ea\u00eb\3\2\2\2\u00eb\u00f1\3\2\2\2\u00ec\u00ed\f\4\2\2\u00ed"+
		"\u00ee\7\4\2\2\u00ee\u00f0\5$\23\2\u00ef\u00ec\3\2\2\2\u00f0\u00f3\3\2"+
		"\2\2\u00f1\u00ef\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2\'\3\2\2\2\u00f3\u00f1"+
		"\3\2\2\2\u00f4\u00f7\5\n\6\2\u00f5\u00f7\5\f\7\2\u00f6\u00f4\3\2\2\2\u00f6"+
		"\u00f5\3\2\2\2\u00f7\u00f8\3\2\2\2\u00f8\u00f9\7.\2\2\u00f9)\3\2\2\2\u00fa"+
		"\u00fc\b\26\1\2\u00fb\u00fd\5(\25\2\u00fc\u00fb\3\2\2\2\u00fc\u00fd\3"+
		"\2\2\2\u00fd\u0103\3\2\2\2\u00fe\u00ff\f\4\2\2\u00ff\u0100\7\4\2\2\u0100"+
		"\u0102\5(\25\2\u0101\u00fe\3\2\2\2\u0102\u0105\3\2\2\2\u0103\u0101\3\2"+
		"\2\2\u0103\u0104\3\2\2\2\u0104+\3\2\2\2\u0105\u0103\3\2\2\2\u0106\u0107"+
		"\7\'\2\2\u0107\u0108\5\62\32\2\u0108\u0109\7(\2\2\u0109-\3\2\2\2\u010a"+
		"\u010b\7\t\2\2\u010b\u010c\7\"\2\2\u010c/\3\2\2\2\u010d\u010e\7\n\2\2"+
		"\u010e\u010f\7\"\2\2\u010f\61\3\2\2\2\u0110\u011a\5\34\17\2\u0111\u011a"+
		"\5\36\20\2\u0112\u011a\5 \21\2\u0113\u011a\5\64\33\2\u0114\u011a\5,\27"+
		"\2\u0115\u011a\5\66\34\2\u0116\u011a\5\"\22\2\u0117\u011a\5.\30\2\u0118"+
		"\u011a\5\60\31\2\u0119\u0110\3\2\2\2\u0119\u0111\3\2\2\2\u0119\u0112\3"+
		"\2\2\2\u0119\u0113\3\2\2\2\u0119\u0114\3\2\2\2\u0119\u0115\3\2\2\2\u0119"+
		"\u0116\3\2\2\2\u0119\u0117\3\2\2\2\u0119\u0118\3\2\2\2\u011a\u011d\3\2"+
		"\2\2\u011b\u0119\3\2\2\2\u011b\u011c\3\2\2\2\u011c\63\3\2\2\2\u011d\u011b"+
		"\3\2\2\2\u011e\u011f\7\16\2\2\u011f\u0120\7#\2\2\u0120\u0121\5\32\16\2"+
		"\u0121\u0122\7$\2\2\u0122\u0123\5,\27\2\u0123\65\3\2\2\2\u0124\u0125\7"+
		"\13\2\2\u0125\u0126\7#\2\2\u0126\u0127\5\32\16\2\u0127\u0128\7$\2\2\u0128"+
		"\u0132\5,\27\2\u0129\u012a\7\f\2\2\u012a\u012b\7\13\2\2\u012b\u012c\7"+
		"#\2\2\u012c\u012d\5\32\16\2\u012d\u012e\7$\2\2\u012e\u012f\5,\27\2\u012f"+
		"\u0131\3\2\2\2\u0130\u0129\3\2\2\2\u0131\u0134\3\2\2\2\u0132\u0130\3\2"+
		"\2\2\u0132\u0133\3\2\2\2\u0133\u0137\3\2\2\2\u0134\u0132\3\2\2\2\u0135"+
		"\u0136\7\f\2\2\u0136\u0138\5,\27\2\u0137\u0135\3\2\2\2\u0137\u0138\3\2"+
		"\2\2\u0138\67\3\2\2\2\u0139\u013a\7.\2\2\u013a\u013b\7#\2\2\u013b\u013c"+
		"\5&\24\2\u013c\u013d\7$\2\2\u013d\u0144\3\2\2\2\u013e\u013f\5\16\b\2\u013f"+
		"\u0140\7#\2\2\u0140\u0141\5\n\6\2\u0141\u0142\7$\2\2\u0142\u0144\3\2\2"+
		"\2\u0143\u0139\3\2\2\2\u0143\u013e\3\2\2\2\u01449\3\2\2\2\u0145\u0148"+
		"\5\n\6\2\u0146\u0148\5\f\7\2\u0147\u0145\3\2\2\2\u0147\u0146\3\2\2\2\u0148"+
		"\u0149\3\2\2\2\u0149\u014a\7.\2\2\u014a\u014b\7#\2\2\u014b\u014c\5*\26"+
		"\2\u014c\u014d\7$\2\2\u014d\u014e\7\"\2\2\u014e;\3\2\2\2\u014f\u0152\5"+
		"\n\6\2\u0150\u0152\5\f\7\2\u0151\u014f\3\2\2\2\u0151\u0150\3\2\2\2\u0152"+
		"\u0153\3\2\2\2\u0153\u0154\7.\2\2\u0154\u0155\7#\2\2\u0155\u0156\5*\26"+
		"\2\u0156\u0157\7$\2\2\u0157\u0158\5,\27\2\u0158=\3\2\2\2!DLNS[hv\u008a"+
		"\u0092\u0094\u00a3\u00ab\u00ad\u00c3\u00c7\u00cc\u00d2\u00da\u00e6\u00ea"+
		"\u00f1\u00f6\u00fc\u0103\u0119\u011b\u0132\u0137\u0143\u0147\u0151";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}