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

Include: '#include'  ~[\r\n]* ->skip;

realTypeID: TypeChar
          | TypeInt
          | TypeLL
          ;

realTypeIDPointer: realTypeID '*' ;

typeIdentifier: TypeInt
               | TypeVoid
               | TypeChar
               | TypeLL
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
Char: '\'' ([\u0000-\u007f]|'\\0') '\'';
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

expr: expr op=(MUL|DIV) expr
    | expr op=(ADD|SUB) expr
    | '&' expr
    | '*' expr
    | '-' expr
    | '(' (realTypeIDPointer|realTypeID) ')' expr
    | PositiveINT
    | Char
    | INT
    | ID
    | functionCall
    | boolExpr
    | expr '[' expr ']'
    | '(' expr ')'
    ;

conditionOperator: Greater
                 | GreaterEqual
                 | Less
                 | LessEqual
                 | Equal
                 ;

conditionExpr: conditionExpr '&&' conditionExpr
             | conditionExpr '||'  conditionExpr
             | '(' conditionExpr ')'
             | expr conditionOperator expr
             | expr
             ;

assignment: ID AssignOperator expr ';'
          | '*' ID AssignOperator expr ';'
          | ID '[' expr ']' AssignOperator expr ';'
          ;

definition: (realTypeID|realTypeID) ID ('=' expr)? ';'
          | (realTypeID|realTypeIDPointer) ID '[' PositiveINT ']' ';'
          ;

callProc: functionCall ';';

returnLine: 'return' expr ';';

param:
       expr
     | functionCall
     | String
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
        ('else' 'if' '(' conditionExpr ')' block)*
        ('else' block)?
        ;

BlockComment: '/*' .*? '*/' ->skip;
LineComment: '//' ~[\r\n]* ->skip;
String: '"' .*? '"';
functionCall : ID '(' paramList ')'
             | sizeof '(' typeIdentifier ')'
             ;
functionDeclare: (typeIdentifier|typeIdentifierPointer) ID '(' defineParamList ')' ';';
functionDefine: (typeIdentifier|typeIdentifierPointer) ID '(' defineParamList ')' block;