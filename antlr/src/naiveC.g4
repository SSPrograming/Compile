// Define a grammar called Hello
grammar naiveC;
r  :  functionCall
    | functionDeclare
    | functionDefine
    | r functionCall
    | r functionDefine
    | r functionDeclare
;         // match keyword hello followed by an identifier
Include: '#include'  ~[\r\n]* ->skip;
typeIdentifier: TypeInt
               | TypeVoid
               | TypeChar
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

True: 'true'
    ;

False: 'false'
    ;

sizeof: 'sizeof'
    ;

boolExpr: True | False
        ;

idList: ID ',' idList
      | ID
      ;

INT: [1-9][0-9]* | '0';
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

assignment: (ID|ID '[' expr ']') AssignOperator expr ';';

definition: (typeIdentifier|typeIdentifierPointer) ID ('=' expr)? ';';

callProc: functionCall ';';

return: 'return' expr ';';

param:
       expr
     | functionCall
     | String
     ;

paramList: param ',' paramList
         | param
         ;

defineParam: (typeIdentifier|typeIdentifierPointer) ID;

defineParamList: defineParam ',' defineParamList
               | defineParam?
               ;

block:  '{' statements '}';

loopBlock: '{' (assignment|definition|callProc|whileBlock|loopBlock|ifLoopBlock|breakLine|continueLine)* '}';

breakLine: 'break' ';' ;

continueLine: 'continue' ';' ;

statements: (assignment|definition|callProc|whileBlock|block|ifBlock)*;

whileBlock: 'while' '(' conditionExpr ')' loopBlock;

ifBlock: 'if' '(' conditionExpr ')' block;

ifLoopBlock: 'if' '(' conditionExpr ')' loopBlock;

BlockComment: '/*' .*? '*/' ->skip;
LineComment: '//' ~[\r\n]* ->skip;
String: '"' .*? '"';
functionCall : ID '(' paramList ')'
             |sizeof '(' typeIdentifier ')'
             ;
functionDeclare: (typeIdentifier|typeIdentifierPointer) ID '(' defineParamList ')' ';';
functionDefine: (typeIdentifier|typeIdentifierPointer) ID '(' defineParamList ')' '{' statements return? '}';