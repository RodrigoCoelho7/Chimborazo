
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "AND BOOLEANO CASO CONTRARIO DEVUELVE DIFERENTE ENCUANTO ENTER ENTERO ENTONCES ESCRIBE FALSO FLOAT FUNCION HACER ID IGUAL INT LISTA NADA OR PARA REAL RESTO SI SIGUIENTE STRING VAR VERDADEROprg : declarations statementsdeclarations : decldeclarations : declarations decldecl : declVdecl : declFdecl : declLdeclV : VAR ids ':' tipoids : IDids : ids ',' IDtipo : ENTEROtipo : REALtipo : BOOLEANOdeclL : LISTA ID '=' listalista : '[' ']'lista : '[' elementos ']'elementos : elementoelementos : elementos ',' elementoelemento : INTelemento : FLOATelemento : BOOLEANOelemento : STRINGelemento : IDelemento : listadeclF : FUNCION ID '(' parametros ')' ':' ENTERO declarations statements DEVUELVE return '.'declF : FUNCION ID '(' ')' ':' ENTERO declarations statements DEVUELVE return '.'parametros : ID ':' tipoparametros : parametros ',' ID ':' tiporeturn : INTreturn : IDstatements : statstatements : statements statstat : atrib ';'stat : conditionsstat : ciclosatrib : ID '=' expexp : exp '+' termoexp : exp '-' termoexp : termotermo : termo '*' fatortermo : termo '/' fatortermo : termo '^' fatortermo : fatorfator : INTfator : FLOATfator : IDfator : '(' exp ')'conditions : SI expL ENTONCES statements endconditionendcondition : '.'endcondition : CASO CONTRARIO statements '.'expL : termoBexpL : expL OR termoBtermoB : fatorBtermoB : termoB AND fatorBfatorB : conditionfatorB : BOOLEANOfatorB : '(' expL ')'condition : exp op expop : '>'op : '<'op : IGUALop : DIFERENTEop : '>' IGUALop : '<' IGUAL ciclos : ENCUANTO expL HACER statements '.'ciclos : PARA expL SIGUIENTE atrib '.'ciclos : PARA expL SIGUIENTE atrib HACER statements '.'"
    
_lr_action_items = {'VAR':([0,2,3,4,5,6,11,64,65,66,67,72,94,112,113,117,119,123,134,135,],[7,7,-2,-4,-5,-6,-3,-7,-10,-11,-12,-13,-14,7,-15,7,7,7,-25,-24,]),'FUNCION':([0,2,3,4,5,6,11,64,65,66,67,72,94,112,113,117,119,123,134,135,],[8,8,-2,-4,-5,-6,-3,-7,-10,-11,-12,-13,-14,8,-15,8,8,8,-25,-24,]),'LISTA':([0,2,3,4,5,6,11,64,65,66,67,72,94,112,113,117,119,123,134,135,],[9,9,-2,-4,-5,-6,-3,-7,-10,-11,-12,-13,-14,9,-15,9,9,9,-25,-24,]),'$end':([1,10,12,14,15,24,25,103,104,106,107,122,126,],[0,-1,-30,-33,-34,-31,-32,-47,-48,-64,-65,-66,-49,]),'ID':([2,3,4,5,6,7,8,9,10,11,12,14,15,17,18,19,24,25,26,32,42,43,46,47,48,49,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,72,73,75,83,84,88,92,94,103,104,106,107,108,113,114,115,116,119,121,122,123,125,126,127,128,129,134,135,],[16,-2,-4,-5,-6,21,22,23,16,-3,-30,-33,-34,38,38,38,-31,-32,38,38,68,69,38,16,38,38,38,38,38,-58,-59,-60,-61,38,38,38,16,16,-7,-10,-11,-12,-13,101,16,-62,-63,16,111,-14,-47,-48,-64,-65,16,-15,101,16,16,16,16,-66,16,16,-49,16,130,130,-25,-24,]),'SI':([2,3,4,5,6,10,11,12,14,15,24,25,47,62,64,65,66,67,72,75,88,94,103,104,106,107,108,113,115,116,119,121,122,123,125,126,127,134,135,],[17,-2,-4,-5,-6,17,-3,-30,-33,-34,-31,-32,17,17,-7,-10,-11,-12,-13,17,17,-14,-47,-48,-64,-65,17,-15,17,17,17,17,-66,17,17,-49,17,-25,-24,]),'ENCUANTO':([2,3,4,5,6,10,11,12,14,15,24,25,47,62,64,65,66,67,72,75,88,94,103,104,106,107,108,113,115,116,119,121,122,123,125,126,127,134,135,],[18,-2,-4,-5,-6,18,-3,-30,-33,-34,-31,-32,18,18,-7,-10,-11,-12,-13,18,18,-14,-47,-48,-64,-65,18,-15,18,18,18,18,-66,18,18,-49,18,-25,-24,]),'PARA':([2,3,4,5,6,10,11,12,14,15,24,25,47,62,64,65,66,67,72,75,88,94,103,104,106,107,108,113,115,116,119,121,122,123,125,126,127,134,135,],[19,-2,-4,-5,-6,19,-3,-30,-33,-34,-31,-32,19,19,-7,-10,-11,-12,-13,19,19,-14,-47,-48,-64,-65,19,-15,19,19,19,19,-66,19,19,-49,19,-25,-24,]),'.':([12,14,15,24,25,34,35,36,37,38,45,75,79,81,82,85,86,87,88,89,103,104,106,107,116,121,122,126,130,131,132,133,],[-30,-33,-34,-31,-32,-38,-42,-43,-44,-45,-35,104,-46,-36,-37,-39,-40,-41,106,107,-47,-48,-64,-65,122,126,-66,-49,-29,134,-28,135,]),'CASO':([12,14,15,24,25,75,103,104,106,107,122,126,],[-30,-33,-34,-31,-32,105,-47,-48,-64,-65,-66,-49,]),'DEVUELVE':([12,14,15,24,25,103,104,106,107,122,125,126,127,],[-30,-33,-34,-31,-32,-47,-48,-64,-65,-66,128,-49,129,]),';':([13,34,35,36,37,38,45,79,81,82,85,86,87,],[25,-38,-42,-43,-44,-45,-35,-46,-36,-37,-39,-40,-41,]),'=':([16,23,],[26,44,]),'BOOLEANO':([17,18,19,32,41,48,49,73,90,114,118,],[31,31,31,31,67,31,31,99,67,99,67,]),'(':([17,18,19,22,26,32,46,48,49,52,53,54,55,56,57,58,59,60,61,83,84,],[32,32,32,43,46,32,46,32,32,46,46,46,-58,-59,-60,-61,46,46,46,-62,-63,]),'INT':([17,18,19,26,32,46,48,49,52,53,54,55,56,57,58,59,60,61,73,83,84,114,128,129,],[36,36,36,36,36,36,36,36,36,36,36,-58,-59,-60,-61,36,36,36,97,-62,-63,97,132,132,]),'FLOAT':([17,18,19,26,32,46,48,49,52,53,54,55,56,57,58,59,60,61,73,83,84,114,],[37,37,37,37,37,37,37,37,37,37,37,-58,-59,-60,-61,37,37,37,98,-62,-63,98,]),':':([20,21,68,69,71,91,111,],[41,-8,-9,90,93,110,118,]),',':([20,21,65,66,67,68,70,94,95,96,97,98,99,100,101,102,109,113,120,124,],[42,-8,-10,-11,-12,-9,92,-14,114,-16,-18,-19,-20,-21,-22,-23,-26,-15,-17,-27,]),'ENTONCES':([27,28,29,30,31,34,35,36,37,38,76,77,78,79,80,81,82,85,86,87,],[47,-50,-52,-54,-55,-38,-42,-43,-44,-45,-51,-53,-56,-46,-57,-36,-37,-39,-40,-41,]),'OR':([27,28,29,30,31,34,35,36,37,38,39,40,50,76,77,78,79,80,81,82,85,86,87,],[48,-50,-52,-54,-55,-38,-42,-43,-44,-45,48,48,48,-51,-53,-56,-46,-57,-36,-37,-39,-40,-41,]),'HACER':([28,29,30,31,34,35,36,37,38,39,45,76,77,78,79,80,81,82,85,86,87,89,],[-50,-52,-54,-55,-38,-42,-43,-44,-45,62,-35,-51,-53,-56,-46,-57,-36,-37,-39,-40,-41,108,]),'SIGUIENTE':([28,29,30,31,34,35,36,37,38,40,76,77,78,79,80,81,82,85,86,87,],[-50,-52,-54,-55,-38,-42,-43,-44,-45,63,-51,-53,-56,-46,-57,-36,-37,-39,-40,-41,]),')':([28,29,30,31,34,35,36,37,38,43,50,51,65,66,67,70,74,76,77,78,79,80,81,82,85,86,87,109,124,],[-50,-52,-54,-55,-38,-42,-43,-44,-45,71,78,79,-10,-11,-12,91,79,-51,-53,-56,-46,-57,-36,-37,-39,-40,-41,-26,-27,]),'AND':([28,29,30,31,34,35,36,37,38,76,77,78,79,80,81,82,85,86,87,],[49,-52,-54,-55,-38,-42,-43,-44,-45,49,-53,-56,-46,-57,-36,-37,-39,-40,-41,]),'+':([33,34,35,36,37,38,45,51,74,79,80,81,82,85,86,87,],[53,-38,-42,-43,-44,-45,53,53,53,-46,53,-36,-37,-39,-40,-41,]),'-':([33,34,35,36,37,38,45,51,74,79,80,81,82,85,86,87,],[54,-38,-42,-43,-44,-45,54,54,54,-46,54,-36,-37,-39,-40,-41,]),'>':([33,34,35,36,37,38,51,79,81,82,85,86,87,],[55,-38,-42,-43,-44,-45,55,-46,-36,-37,-39,-40,-41,]),'<':([33,34,35,36,37,38,51,79,81,82,85,86,87,],[56,-38,-42,-43,-44,-45,56,-46,-36,-37,-39,-40,-41,]),'IGUAL':([33,34,35,36,37,38,51,55,56,79,81,82,85,86,87,],[57,-38,-42,-43,-44,-45,57,83,84,-46,-36,-37,-39,-40,-41,]),'DIFERENTE':([33,34,35,36,37,38,51,79,81,82,85,86,87,],[58,-38,-42,-43,-44,-45,58,-46,-36,-37,-39,-40,-41,]),'*':([34,35,36,37,38,79,81,82,85,86,87,],[59,-42,-43,-44,-45,-46,59,59,-39,-40,-41,]),'/':([34,35,36,37,38,79,81,82,85,86,87,],[60,-42,-43,-44,-45,-46,60,60,-39,-40,-41,]),'^':([34,35,36,37,38,79,81,82,85,86,87,],[61,-42,-43,-44,-45,-46,61,61,-39,-40,-41,]),'ENTERO':([41,90,93,110,118,],[65,65,112,117,65,]),'REAL':([41,90,118,],[66,66,66,]),'[':([44,73,114,],[73,73,73,]),']':([73,94,95,96,97,98,99,100,101,102,113,120,],[94,-14,113,-16,-18,-19,-20,-21,-22,-23,-15,-17,]),'STRING':([73,114,],[100,100,]),'CONTRARIO':([105,],[115,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'prg':([0,],[1,]),'declarations':([0,112,117,],[2,119,123,]),'decl':([0,2,112,117,119,123,],[3,11,3,3,11,11,]),'declV':([0,2,112,117,119,123,],[4,4,4,4,4,4,]),'declF':([0,2,112,117,119,123,],[5,5,5,5,5,5,]),'declL':([0,2,112,117,119,123,],[6,6,6,6,6,6,]),'statements':([2,47,62,108,115,119,123,],[10,75,88,116,121,125,127,]),'stat':([2,10,47,62,75,88,108,115,116,119,121,123,125,127,],[12,24,12,12,24,24,12,12,24,12,24,12,24,24,]),'atrib':([2,10,47,62,63,75,88,108,115,116,119,121,123,125,127,],[13,13,13,13,89,13,13,13,13,13,13,13,13,13,13,]),'conditions':([2,10,47,62,75,88,108,115,116,119,121,123,125,127,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'ciclos':([2,10,47,62,75,88,108,115,116,119,121,123,125,127,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'ids':([7,],[20,]),'expL':([17,18,19,32,],[27,39,40,50,]),'termoB':([17,18,19,32,48,],[28,28,28,28,76,]),'fatorB':([17,18,19,32,48,49,],[29,29,29,29,29,77,]),'condition':([17,18,19,32,48,49,],[30,30,30,30,30,30,]),'exp':([17,18,19,26,32,46,48,49,52,],[33,33,33,45,51,74,33,33,80,]),'termo':([17,18,19,26,32,46,48,49,52,53,54,],[34,34,34,34,34,34,34,34,34,81,82,]),'fator':([17,18,19,26,32,46,48,49,52,53,54,59,60,61,],[35,35,35,35,35,35,35,35,35,35,35,85,86,87,]),'op':([33,51,],[52,52,]),'tipo':([41,90,118,],[64,109,124,]),'parametros':([43,],[70,]),'lista':([44,73,114,],[72,102,102,]),'elementos':([73,],[95,]),'elemento':([73,114,],[96,120,]),'endcondition':([75,],[103,]),'return':([128,129,],[131,133,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> prg","S'",1,None,None,None),
  ('prg -> declarations statements','prg',2,'p_prg','yacc.py',7),
  ('declarations -> decl','declarations',1,'p_declarations_1','yacc.py',12),
  ('declarations -> declarations decl','declarations',2,'p_declarations_mult','yacc.py',18),
  ('decl -> declV','decl',1,'p_decl_V','yacc.py',24),
  ('decl -> declF','decl',1,'p_decl_F','yacc.py',28),
  ('decl -> declL','decl',1,'p_decl_L','yacc.py',31),
  ('declV -> VAR ids : tipo','declV',4,'p_declV','yacc.py',38),
  ('ids -> ID','ids',1,'p_ids_1','yacc.py',44),
  ('ids -> ids , ID','ids',3,'p_ids_mult','yacc.py',48),
  ('tipo -> ENTERO','tipo',1,'p_tipo_int','yacc.py',52),
  ('tipo -> REAL','tipo',1,'p_tipo_REAL','yacc.py',56),
  ('tipo -> BOOLEANO','tipo',1,'p_tipo_BOOL','yacc.py',60),
  ('declL -> LISTA ID = lista','declL',4,'p_declL','yacc.py',68),
  ('lista -> [ ]','lista',2,'p_lista_vazia','yacc.py',71),
  ('lista -> [ elementos ]','lista',3,'p_lista_elem','yacc.py',74),
  ('elementos -> elemento','elementos',1,'p_elementos_1','yacc.py',77),
  ('elementos -> elementos , elemento','elementos',3,'p_elementos_mult','yacc.py',80),
  ('elemento -> INT','elemento',1,'p_elemento_INT','yacc.py',83),
  ('elemento -> FLOAT','elemento',1,'p_elemento_FLOAT','yacc.py',86),
  ('elemento -> BOOLEANO','elemento',1,'p_elemento_BOOL','yacc.py',89),
  ('elemento -> STRING','elemento',1,'p_elemento_STRING','yacc.py',92),
  ('elemento -> ID','elemento',1,'p_elemento_ID','yacc.py',95),
  ('elemento -> lista','elemento',1,'p_elemento_lista','yacc.py',98),
  ('declF -> FUNCION ID ( parametros ) : ENTERO declarations statements DEVUELVE return .','declF',12,'p_declF_parametros','yacc.py',105),
  ('declF -> FUNCION ID ( ) : ENTERO declarations statements DEVUELVE return .','declF',11,'p_declF_vazia','yacc.py',108),
  ('parametros -> ID : tipo','parametros',3,'p_parametros_1','yacc.py',112),
  ('parametros -> parametros , ID : tipo','parametros',5,'p_parametros_mult','yacc.py',117),
  ('return -> INT','return',1,'p_return_INT','yacc.py',122),
  ('return -> ID','return',1,'p_return_ID','yacc.py',125),
  ('statements -> stat','statements',1,'p_statements_1','yacc.py',132),
  ('statements -> statements stat','statements',2,'p_statements_mult','yacc.py',135),
  ('stat -> atrib ;','stat',2,'p_stat_atrib','yacc.py',138),
  ('stat -> conditions','stat',1,'p_stat_conditions','yacc.py',142),
  ('stat -> ciclos','stat',1,'p_stat_ciclos','yacc.py',146),
  ('atrib -> ID = exp','atrib',3,'p_atrib','yacc.py',151),
  ('exp -> exp + termo','exp',3,'p_exp_soma','yacc.py',155),
  ('exp -> exp - termo','exp',3,'p_exp_sub','yacc.py',159),
  ('exp -> termo','exp',1,'p_exp_termo','yacc.py',163),
  ('termo -> termo * fator','termo',3,'p_termo_mul','yacc.py',167),
  ('termo -> termo / fator','termo',3,'p_termo_div','yacc.py',171),
  ('termo -> termo ^ fator','termo',3,'p_termo_pot','yacc.py',175),
  ('termo -> fator','termo',1,'p_termo_fator','yacc.py',179),
  ('fator -> INT','fator',1,'p_fator_INT','yacc.py',183),
  ('fator -> FLOAT','fator',1,'p_fator_FLOAT','yacc.py',187),
  ('fator -> ID','fator',1,'p_fator_ID','yacc.py',191),
  ('fator -> ( exp )','fator',3,'p_fator_exp','yacc.py',195),
  ('conditions -> SI expL ENTONCES statements endcondition','conditions',5,'p_conditions_si','yacc.py',203),
  ('endcondition -> .','endcondition',1,'p_endcpndition','yacc.py',206),
  ('endcondition -> CASO CONTRARIO statements .','endcondition',4,'p_conditions_si_no','yacc.py',209),
  ('expL -> termoB','expL',1,'p_expL_1','yacc.py',212),
  ('expL -> expL OR termoB','expL',3,'p_expL_mult','yacc.py',215),
  ('termoB -> fatorB','termoB',1,'p_termoB_1','yacc.py',218),
  ('termoB -> termoB AND fatorB','termoB',3,'p_termoB_mult','yacc.py',221),
  ('fatorB -> condition','fatorB',1,'p_fatorB_condition','yacc.py',224),
  ('fatorB -> BOOLEANO','fatorB',1,'p_fatorB_BOOL','yacc.py',227),
  ('fatorB -> ( expL )','fatorB',3,'p_fatorB_expL','yacc.py',230),
  ('condition -> exp op exp','condition',3,'p_condition','yacc.py',233),
  ('op -> >','op',1,'p_op_maior','yacc.py',236),
  ('op -> <','op',1,'p_op_menor','yacc.py',239),
  ('op -> IGUAL','op',1,'p_op_IGUAL','yacc.py',242),
  ('op -> DIFERENTE','op',1,'p_op_DIFERENTE','yacc.py',245),
  ('op -> > IGUAL','op',2,'p_op_maiorIGUAL','yacc.py',248),
  ('op -> < IGUAL','op',2,'p_op_menorIGUAL','yacc.py',251),
  ('ciclos -> ENCUANTO expL HACER statements .','ciclos',5,'p_ciclos_while','yacc.py',258),
  ('ciclos -> PARA expL SIGUIENTE atrib .','ciclos',5,'p_ciclos_for_1','yacc.py',261),
  ('ciclos -> PARA expL SIGUIENTE atrib HACER statements .','ciclos',7,'p_ciclos_for_mult','yacc.py',264),
]
