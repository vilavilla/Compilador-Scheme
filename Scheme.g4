grammar Scheme;

root
    : declaration* expr* EOF
    ;

// Expressions
expr
    : '(' expr ')'                             #groupExpr
    | ID                                       #variableExpr
    | NUM                                      #numberExpr
    | STRING                                   #stringExpr
    | '#t'                                     #trueExpr
    | '#f'                                     #falseExpr
    | '(' (SUM | SUB | PROD | DIV | MOD | EXP) expr expr ')'  #arithmeticExpr
    | '(' 'if' expr expr expr ')'              #ifExpr
    | '(' 'cond' condClause+ ')'               #condExpr
    | '(' 'let' '(' letBinding (letBinding)* ')' expr+ ')'   #letExpr
    | '(' 'read' ')'                           #readExpr
    | '(' 'display' expr ')'                   #displayExpr
    | '(' 'write' expr ')'                     #writeExpr
    | '(' 'newline' ')'                        #newlineExpr
    | '(' (LESS | LESSEQ | GREATER | GREATEREQ | EQ | NOTEQ) expr expr ')' #comparisonExpr
    | '(' (AND | OR | NOT) expr+ ')'           #logicalExpr
    | '(' 'car' expr ')'                       #carExpr
    | '(' 'cdr' expr ')'                       #cdrExpr
    | '(' 'cons' expr expr ')'                 #consExpr
    | '(' 'null?' expr ')'                     #nullExpr
    | ID expr*                                 #functionCallExpr
    | LIST                                     #listLiteralExpr
    | EMPTY_LIST                               #emptyListExpr
    ;

// Let bindings
letBinding
    : '(' ID expr ')'                          #letBindingPair
    ;

// Conditional clauses
condClause
    : '(' expr expr ')'                        #condClauseExpr
    | '(' 'else' expr ')'                        #condElseClause
    ;

// Declarations
declaration
    : '(' 'define' ID expr ')'                 #constantDeclaration
    | '(' 'define' '(' ID ID* ')' block ')'    #functionDeclaration
    ;

// Blocks are made up Statements
block
    : stmt*
    ;

// Statements
stmt
    : expr                                      #expressionStmt
    | '(' 'define' ID expr ')'                  #assignmentStmt
    | '(' 'if' expr block ')'                   #ifStmt
    | '(' 'if' expr block 'else' block ')'      #ifElseStmt
    ;

// Operators
SUM     : '+';
SUB     : '-';
PROD    : '*';
DIV     : '/';
MOD     : 'mod';
EXP     : '^';
NOTEQ   : '<>';
LESSEQ  : '<=';
GREATEREQ: '>=' ;
LESS    : '<';
GREATER : '>';
EQ      : '=';
AND     : 'and';
OR      : 'or';
NOT     : 'not';

// List literals
LIST : '\'' '(' (NUM | ID | STRING) (WS (NUM | ID | STRING))* ')';
EMPTY_LIST : '\'' '()';

// Strings
STRING  : '"' (~["\\] | '\\' .)* '"';

// Identifiers and numbers
ID : [a-zA-Z][a-zA-Z0-9_-]*;
NUM         : [0-9]+;

// Comments and whitespace
COMMENT : ';' ~[\r\n]* -> skip; // Comentarios en Scheme
WS      : [ \t\n\r]+ -> skip;
