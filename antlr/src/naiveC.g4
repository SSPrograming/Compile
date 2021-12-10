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

realTypeID: TypeChar  # RealTypeChar
          | TypeInt  # RealTypeInt
          ;

realTypeIDPointer: realTypeID '*' ;

typeIdentifier: TypeInt   # TypeInt
               | TypeVoid # TypeVoid
               | TypeChar # TypeChar
               ;

typeIdentifierPointer: typeIdentifier '*';

TypeInt: 'int'
    ;


TypeVoid: 'void'
    ;

TypeChar: 'char'
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

sizeof: 'sizeof'
    ;

boolExpr: TRUE | FALSE
        ;

idList: ID ',' idList
      | ID
      ;

PositiveINT: [1-9][0-9]*;
INT: [-]?[1-9][0-9]* | '0';
ID : [a-zA-Z_][a-z0-9A-Z_]* ;             // match lower-case identifiers
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

arithmeticOperator:   ADD
                    | SUB
                    | MUL
                    | DIV
                    | MOD
                    | ArithmeticAnd
                    | ArithmeticOR
                    ;

expr: expr op=(MUL|DIV) expr    # MulDiv
    | expr op=(ADD|SUB) expr    # AddSub
    | '&' ID                    # GetP
    | '*' expr                  # MakP
    | PositiveINT               # PositiveINT
    | INT                       # Int
    | ID                        # Id
    | functionCall              # FCall
    | boolExpr                  # TrueFalse
    | expr '[' expr ']'         # ArrayVisit
    | '(' expr ')'              # Parens
    ;

conditionOperator: Greater
                 | GreaterEqual
                 | Less
                 | LessEqual
                 | Equal
                 ;

conditionExpr: conditionExpr '&&' conditionExpr  # And
             | conditionExpr '||'  conditionExpr # Or
             | '(' conditionExpr ')' # CondParen
             | expr conditionOperator expr # CondOp
             | expr # CondExp
             ;

assignment: (ID|ID '[' index=expr ']') AssignOperator value=expr ';';

definition: (realTypeID|realTypeID) ID ('=' expr)? ';'
          | (realTypeID|realTypeIDPointer) ID '[' PositiveINT ']' ';'
          ;

callProc: functionCall ';';

returnLine: 'return' expr ';';

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

loopBlock: '{' (assignment|definition|callProc|whileBlock|loopBlock|ifLoopBlock|breakLine|continueLine)* '}';

breakLine: 'break' ';' ;

continueLine: 'continue' ';' ;

statements: (assignment|definition|callProc|whileBlock|block|ifBlock)*;

returnStatemts: (assignment|definition|callProc|whileBlock|block|ifBlock|returnLine)*;

whileBlock: 'while' '(' conditionExpr ')' loopBlock;

ifBlock: 'if' '(' conditionExpr ')' block
        ('else' 'if' '(' elif_cond=conditionExpr ')' block)*
        ('else' else_block=block)?
        ;

ifLoopBlock: 'if' '(' conditionExpr ')'
            loopBlock('else' 'if' '(' conditionExpr ')' loopBlock)*
            ('else' loopBlock)?
            ;

BlockComment: '/*' .*? '*/' ->skip;
LineComment: '//' ~[\r\n]* ->skip;
String: '"' .*? '"';
functionCall : ID '(' paramList ')'
             | sizeof '(' typeIdentifier ')'
             ;
functionDeclare: (typeIdentifier|typeIdentifierPointer) ID '(' defineParamList ')' ';';
functionDefine: (typeIdentifier|typeIdentifierPointer) ID '(' defineParamList ')' '{' returnStatemts '}';
