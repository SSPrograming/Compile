// Define a grammar called Hello
grammar naiveC;
prog: r
    ;

r  :  functionCall
    | functionDeclare
    | functionDefine
    | r functionCall
    | r functionDefine
    | r functionDeclare
;         // match keyword hello followed by an identifier

Include: '#include'  ~[\r\n]* -> skip;


realTypeID: TypeChar
          | TypeInt
          | TypeLL
          | TypeDouble
          ;

realTypeIDPointer: realTypeID '*' ;


typeIdentifier: TypeInt
               | TypeVoid
               | TypeChar
               | TypeLL
               | TypeDouble
               ;

typeIdentifierPointer: typeIdentifier '*';

TypeInt: 'int'
    ;


TypeVoid: 'void'
    ;

TypeChar: 'char'
    ;

TypeLL: 'long long'
      ;

TypeDouble: 'double'
    ;

Break: 'break'
    ;

Continue: 'continue'
    ;

If: 'if'
    ;

Else: 'else'
    ;

Return: 'return'
    ;

While: 'while'
    ;

ADD: '+'
    ;

ADDADD: '++'
    ;

SUBSUB: '--'
    ;

SUB: '-'
    ;

MUL: '*'
    ;

DIV: '/'
    ;

MOD: '%'
    ;

Greater: '>'
    ;

Less:   '<'
    ;

GreaterEqual: '>='
    ;

LessEqual: '<='
    ;

Equal: '=='
    ;

NotEqual: '!='
    ;

Not: '!'
    ;

AssignOperator: '='
    ;

ArithmeticAnd: '&'
    ;

ArithmeticOR: '|'
    ;

LogicAnd: '&&'
    ;

LogicOR: '||'
    ;

Semicolon: ';'
    ;

LeftParentheses: '('
    ;

RightParentheses: ')'
    ;

LeftBracket: '['
    ;

RightBracket: ']'
    ;

LeftBrace: '{'
    ;

RightBrace: '}'
    ;

TRUE: 'true'
    ;

FALSE: 'false'
    ;

SIZEOF: 'sizeof'
    ;

boolExpr: TRUE | FALSE
        ;

idList: ID ',' idList
      | ID
      ;

PositiveINT: [1-9][0-9]*;
Char: '\'' ([\u0000-\u007f]|'\\0'|'\\t'|'\\n') '\'';
INT: [-]?[1-9][0-9]* | '0';
ID : [a-zA-Z_][a-z0-9A-Z_]*|[\p{Emoji}] ;             // match lower-case identifiers
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

expr: '(' (realTypeIDPointer | realTypeID) ')' expr # TypeCast
    | '-' expr                  # Negative
    | '*' expr                  # MakP
    | '&' ID                    # GetP
	| PositiveINT               # PositiveINT
	| Char                      # Char
    | INT                       # Int
    | ID                        # Id
    | functionCall              # FCall
    | SIZEOF '(' typeIdentifier ')' # SizeOf
    | boolExpr                  # TrueFalse
    | ID '[' expr ']'           # ArrayVisit
    | '(' expr ')'              # Parens
    | expr op=(MUL|DIV) expr    # MulDiv
    | expr op=(ADD|SUB) expr    # AddSub
    ;

conditionOperator: Greater
                 | GreaterEqual
                 | Less
                 | LessEqual
                 | Equal
                 | NotEqual
                 ;

conditionExpr: '!' conditionExpr # Neg
             | conditionExpr '&&' conditionExpr  # And
             | conditionExpr '||'  conditionExpr # Or
             | '(' conditionExpr ')' # CondParen
             | expr conditionOperator expr # CondOp
             | expr # CondExp
             ;

assignment: ID AssignOperator expr ';'              # CommonAssign
          | '*' ID AssignOperator expr ';'          # MemoryAssign
          | ID '[' expr ']' AssignOperator expr ';' # ArrayAssign
          ;

definition: (realTypeID|realTypeIDPointer) ID ('=' expr)? ';'
          | (realTypeID|realTypeIDPointer) ID '[' PositiveINT ']' ';'
          ;

callProc: functionCall ';';

returnLine: 'return' expr? ';';

param:
       expr             # ParamExpr
     | functionCall     # ParamFunc
     | String           # ParamString
     ;

paramList: paramList ',' param
         | param?
         ;

defineParam: (typeIdentifier|typeIdentifierPointer) ID;

defineParamList: defineParamList ',' defineParam
               | defineParam?
               ;

block:  '{' statements '}';

breakLine: 'break' ';' ;

continueLine: 'continue' ';' ;

statements: (assignment|definition|callProc|whileBlock|block|ifBlock|returnLine|breakLine|continueLine)*;

whileBlock: 'while' '(' conditionExpr ')' block;

ifBlock: 'if' '(' conditionExpr ')' block
        ('else' 'if' '(' elif_cond=conditionExpr ')' block)*
        ('else' else_block=block)?
        ;

BlockComment: '/*' .*? '*/' ->skip;
LineComment: '//' ~[\r\n]* ->skip;
String: '"' .*? '"';
functionCall : ID '(' paramList ')'
             ;
functionDeclare: (typeIdentifier|typeIdentifierPointer) ID '(' defineParamList ')' ';';
functionDefine: (typeIdentifier|typeIdentifierPointer) ID '(' defineParamList ')' block;
