grammar Scheme;

root : instru* EOF ;

instru: bucle
      | ifcondition
      | condition
      | expr
      | assignation
      | imprimir
      | funcion
      | constante
      | entrada
      ;

funcion : '(define' '(' VAR (VAR)* ')' expr ')' ;

constante : '(define' VAR expr ')' ;

entrada : '(' 'read' ')' ;

expr : '(' operacion_aritmetica (expr|VAR|NUM)* ')'
     | '(' operacion_relacional (expr|VAR|NUM)* ')'
     | '(' 'car' expr ')'
     | '(' 'cdr' expr ')'
     | '(' 'cons' expr expr ')'
     | '(' 'null?' expr ')'
     | '(' 'quote' lista ')'
     | '(' 'display' expr ')'
     | '(' 'newline' ')'
     | '(' 'and' expr (expr)* ')'
     | '(' 'or' expr (expr)* ')'
     | '(' 'not' expr ')'
     | '(' VAR (expr|VAR|NUM)* ')'  // Para funciones de orden superior y llamadas a funciones
     | if_expr
     | cond_expr
     | let_expr
     | VAR
     | NUM
     | BOOLEAN
     ;

operacion_aritmetica: '+'  // Operadores aritméticos
                    | '-'
                    | '*'
                    | '/'
                    ;

operacion_relacional: '>'
                    | '<'
                    | '>='
                    | '<='
                    | '='
                    | '<>'
                    ;

bucle : '(while' condition instru* ')' ;

assignation : '(set!' VAR expr ')' ;

imprimir : '(' 'write' expr ')' ;

condition : '(' expr operacion_relacional expr ')' ;

ifcondition: if_expr ;

if_expr : '(if' condition expr expr ')' ;

cond_expr : '(cond' cond_clause+ ')' ;

cond_clause : '(' condition expr ')' 
            | '(' '#t' expr ')' 
            ;

let_expr : '(let' '(' let_binding+ ')' expr ')' ;

let_binding : '(' VAR expr ')' ;

lista : '(' (expr|NUM|VAR)* ')' ;

BOOLEAN : '#t' | '#f' ;

NUM : [0-9]+ ;

VAR : [a-zA-Z]+ ;

WS : [ \n\t]+ -> skip ;
