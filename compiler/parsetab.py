
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "AND BOOLEANO CASO CONTRARIO DEVUELVE DIFERENTE ENCUANTO ENTER ENTERO ENTONCES ESCRIBIR FALSO FLOAT FUNCION HACER ID IGUAL INT LEER LISTA NADA OR PARA REAL RESTO SI SIGUIENTE STR STRING VAR VERDADEROprg : declarations statementsdeclarations : decldeclarations : declarations decldecl : declVdecl : declFdecl : declLdeclV : VAR vari ':' tipovari : atribDvari : IDvari : vari ',' atribDvari : vari ',' IDtipo : ENTEROtipo : REALtipo : BOOLEANOtipo : STRatribD : ID '=' STRINGatribD : ID '=' VERDADEROatribD : ID '=' FALSOatribD : ID '=' expdeclL : LISTA ID '=' listalista : '[' ']'lista : '[' elementos ']'elementos : elementoelementos : elementos ',' elementoelemento : INTelemento : FLOATelemento : BOOLEANOelemento : STRINGelemento : IDelemento : listadeclF : FUNCION ID '(' parametros ')' ':' tipo declarations statements DEVUELVE return '.'parametros : parametros : ID ':' tipoparametros : parametros ',' ID ':' tiporeturn : INTreturn : IDreturn : FLOATreturn : VERDADEROreturn : FALSOstatements : statstatements : statements statstat : atrib ';'stat : conditionsstat : ciclosstat : writeatrib : ID '=' STRINGatrib : ID '=' VERDADEROatrib : ID '=' FALSOatrib : ID '=' expexp : exp '+' termoexp : exp '-' termoexp : termotermo : termo '*' fatortermo : termo '/' fatortermo : termo RESTO fatortermo : termo '^' fatortermo : fatorfator : INTfator : VERDADEROfator : FALSOfator : FLOATfator : IDfator : ID '(' content_params ')' fator : '(' exp ')'fator : castfator : readcontent_params : content_params : list_paramslist_params : explist_params : list_params ',' expconditions : SI expL ENTONCES statements endconditionendcondition : '.'endcondition : CASO CONTRARIO statements '.'expL : termoBexpL : expL OR termoBtermoB : fatorBtermoB : termoB AND fatorBfatorB : conditionfatorB : VERDADEROfatorB : FALSOfatorB : '(' expL ')'condition : exp op expop : '>'op : '<'op : IGUALop : DIFERENTEop : '>' IGUALop : '<' IGUALciclos : ENCUANTO expL HACER statements '.'ciclos : PARA expL SIGUIENTE atrib '.'ciclos : PARA expL SIGUIENTE atrib HACER statements '.'write : ESCRIBIR '(' ID ')' ';'write : ESCRIBIR '(' STRING ')' ';'read : LEER '(' STRING ')'cast : tipocast '(' exp ')'cast : tipocast '(' STRING ')'tipocast : REALtipocast : ENTEROtipocast : STR"
    
_lr_action_items = {'VAR':([0,2,3,4,5,6,11,86,87,88,89,90,99,131,156,161,166,177,],[7,7,-2,-4,-5,-6,-3,-7,-12,-13,-14,-15,-20,-21,-22,7,7,-31,]),'FUNCION':([0,2,3,4,5,6,11,86,87,88,89,90,99,131,156,161,166,177,],[8,8,-2,-4,-5,-6,-3,-7,-12,-13,-14,-15,-20,-21,-22,8,8,-31,]),'LISTA':([0,2,3,4,5,6,11,86,87,88,89,90,99,131,156,161,166,177,],[9,9,-2,-4,-5,-6,-3,-7,-12,-13,-14,-15,-20,-21,-22,9,9,-31,]),'$end':([1,10,12,14,15,16,27,28,140,141,148,149,151,152,165,168,],[0,-1,-40,-43,-44,-45,-41,-42,-71,-72,-89,-90,-92,-93,-91,-73,]),'ID':([2,3,4,5,6,7,8,9,10,11,12,14,15,16,18,19,20,27,28,29,36,52,54,55,56,62,63,64,65,68,69,70,71,72,73,74,75,76,77,78,79,80,82,83,86,87,88,89,90,99,100,104,112,113,124,130,131,140,141,144,148,149,150,151,152,156,157,158,160,164,165,166,168,169,170,177,],[17,-2,-4,-5,-6,24,25,26,17,-3,-40,-43,-44,-45,42,42,42,-41,-42,42,42,84,92,42,97,42,17,42,42,42,42,42,-83,-84,-85,-86,42,42,42,42,42,42,17,17,-7,-12,-13,-14,-15,-20,138,17,-87,-88,17,155,-21,-71,-72,42,-89,-90,17,-92,-93,-22,138,17,17,17,-91,17,-73,17,171,-31,]),'SI':([2,3,4,5,6,10,11,12,14,15,16,27,28,63,82,86,87,88,89,90,99,104,124,131,140,141,148,149,150,151,152,156,158,160,164,165,166,168,169,177,],[18,-2,-4,-5,-6,18,-3,-40,-43,-44,-45,-41,-42,18,18,-7,-12,-13,-14,-15,-20,18,18,-21,-71,-72,-89,-90,18,-92,-93,-22,18,18,18,-91,18,-73,18,-31,]),'ENCUANTO':([2,3,4,5,6,10,11,12,14,15,16,27,28,63,82,86,87,88,89,90,99,104,124,131,140,141,148,149,150,151,152,156,158,160,164,165,166,168,169,177,],[19,-2,-4,-5,-6,19,-3,-40,-43,-44,-45,-41,-42,19,19,-7,-12,-13,-14,-15,-20,19,19,-21,-71,-72,-89,-90,19,-92,-93,-22,19,19,19,-91,19,-73,19,-31,]),'PARA':([2,3,4,5,6,10,11,12,14,15,16,27,28,63,82,86,87,88,89,90,99,104,124,131,140,141,148,149,150,151,152,156,158,160,164,165,166,168,169,177,],[20,-2,-4,-5,-6,20,-3,-40,-43,-44,-45,-41,-42,20,20,-7,-12,-13,-14,-15,-20,20,20,-21,-71,-72,-89,-90,20,-92,-93,-22,20,20,20,-91,20,-73,20,-31,]),'ESCRIBIR':([2,3,4,5,6,10,11,12,14,15,16,27,28,63,82,86,87,88,89,90,99,104,124,131,140,141,148,149,150,151,152,156,158,160,164,165,166,168,169,177,],[21,-2,-4,-5,-6,21,-3,-40,-43,-44,-45,-41,-42,21,21,-7,-12,-13,-14,-15,-20,21,21,-21,-71,-72,-89,-90,21,-92,-93,-22,21,21,21,-91,21,-73,21,-31,]),'.':([12,14,15,16,27,28,38,39,40,41,42,43,44,58,59,60,61,102,103,104,108,110,111,114,115,116,117,124,125,140,141,143,145,146,147,148,149,151,152,160,164,165,168,171,172,173,174,175,176,],[-40,-43,-44,-45,-41,-42,-52,-57,-58,-61,-62,-65,-66,-46,-47,-48,-49,-59,-60,141,-64,-50,-51,-53,-54,-55,-56,148,149,-71,-72,-63,-95,-96,-94,-89,-90,-92,-93,165,168,-91,-73,-36,177,-35,-37,-38,-39,]),'CASO':([12,14,15,16,27,28,104,140,141,148,149,151,152,165,168,],[-40,-43,-44,-45,-41,-42,142,-71,-72,-89,-90,-92,-93,-91,-73,]),'DEVUELVE':([12,14,15,16,27,28,140,141,148,149,151,152,165,168,169,],[-40,-43,-44,-45,-41,-42,-71,-72,-89,-90,-92,-93,-91,-73,170,]),';':([13,38,39,40,41,42,43,44,58,59,60,61,102,103,108,110,111,114,115,116,117,126,127,143,145,146,147,],[28,-52,-57,-58,-61,-62,-65,-66,-46,-47,-48,-49,-59,-60,-64,-50,-51,-53,-54,-55,-56,151,152,-63,-95,-96,-94,]),'=':([17,24,26,92,],[29,55,57,55,]),'VERDADERO':([18,19,20,29,36,55,62,64,65,68,69,70,71,72,73,74,75,76,77,78,79,80,112,113,144,170,],[34,34,34,59,34,94,102,34,34,102,102,102,-83,-84,-85,-86,102,102,102,102,102,102,-87,-88,102,175,]),'FALSO':([18,19,20,29,36,55,62,64,65,68,69,70,71,72,73,74,75,76,77,78,79,80,112,113,144,170,],[35,35,35,60,35,95,103,35,35,103,103,103,-83,-84,-85,-86,103,103,103,103,103,103,-87,-88,103,176,]),'(':([18,19,20,21,25,29,36,42,45,46,47,48,49,55,62,64,65,68,69,70,71,72,73,74,75,76,77,78,79,80,112,113,144,],[36,36,36,52,56,62,36,79,80,81,-97,-98,-99,62,62,36,36,62,62,62,-83,-84,-85,-86,62,62,62,62,62,62,-87,-88,62,]),'INT':([18,19,20,29,36,55,62,64,65,68,69,70,71,72,73,74,75,76,77,78,79,80,100,112,113,144,157,170,],[40,40,40,40,40,40,40,40,40,40,40,40,-83,-84,-85,-86,40,40,40,40,40,40,134,-87,-88,40,134,173,]),'FLOAT':([18,19,20,29,36,55,62,64,65,68,69,70,71,72,73,74,75,76,77,78,79,80,100,112,113,144,157,170,],[41,41,41,41,41,41,41,41,41,41,41,41,-83,-84,-85,-86,41,41,41,41,41,41,135,-87,-88,41,135,174,]),'LEER':([18,19,20,29,36,55,62,64,65,68,69,70,71,72,73,74,75,76,77,78,79,80,112,113,144,],[46,46,46,46,46,46,46,46,46,46,46,46,-83,-84,-85,-86,46,46,46,46,46,46,-87,-88,46,]),'REAL':([18,19,20,29,36,53,55,62,64,65,68,69,70,71,72,73,74,75,76,77,78,79,80,112,113,128,144,154,162,],[47,47,47,47,47,88,47,47,47,47,47,47,47,-83,-84,-85,-86,47,47,47,47,47,47,-87,-88,88,47,88,88,]),'ENTERO':([18,19,20,29,36,53,55,62,64,65,68,69,70,71,72,73,74,75,76,77,78,79,80,112,113,128,144,154,162,],[48,48,48,48,48,87,48,48,48,48,48,48,48,-83,-84,-85,-86,48,48,48,48,48,48,-87,-88,87,48,87,87,]),'STR':([18,19,20,29,36,53,55,62,64,65,68,69,70,71,72,73,74,75,76,77,78,79,80,112,113,128,144,154,162,],[49,49,49,49,49,90,49,49,49,49,49,49,49,-83,-84,-85,-86,49,49,49,49,49,49,-87,-88,90,49,90,90,]),':':([22,23,24,38,39,40,41,42,43,44,91,92,93,94,95,96,97,102,103,108,110,111,114,115,116,117,129,143,145,146,147,155,],[53,-8,-9,-52,-57,-58,-61,-62,-65,-66,-10,-11,-16,-17,-18,-19,128,-59,-60,-64,-50,-51,-53,-54,-55,-56,154,-63,-95,-96,-94,162,]),',':([22,23,24,38,39,40,41,42,43,44,56,87,88,89,90,91,92,93,94,95,96,98,102,103,108,110,111,114,115,116,117,119,120,131,132,133,134,135,136,137,138,139,143,145,146,147,153,156,159,163,167,],[54,-8,-9,-52,-57,-58,-61,-62,-65,-66,-32,-12,-13,-14,-15,-10,-11,-16,-17,-18,-19,130,-59,-60,-64,-50,-51,-53,-54,-55,-56,144,-69,-21,157,-23,-25,-26,-27,-28,-29,-30,-63,-95,-96,-94,-33,-22,-70,-24,-34,]),'STRING':([29,52,55,80,81,100,157,],[58,85,93,122,123,137,137,]),'ENTONCES':([30,31,32,33,34,35,38,39,40,41,42,43,44,102,103,105,106,107,108,109,110,111,114,115,116,117,143,145,146,147,],[63,-74,-76,-78,-79,-80,-52,-57,-58,-61,-62,-65,-66,-59,-60,-75,-77,-81,-64,-82,-50,-51,-53,-54,-55,-56,-63,-95,-96,-94,]),'OR':([30,31,32,33,34,35,38,39,40,41,42,43,44,50,51,66,102,103,105,106,107,108,109,110,111,114,115,116,117,143,145,146,147,],[64,-74,-76,-78,-79,-80,-52,-57,-58,-61,-62,-65,-66,64,64,64,-59,-60,-75,-77,-81,-64,-82,-50,-51,-53,-54,-55,-56,-63,-95,-96,-94,]),'HACER':([31,32,33,34,35,38,39,40,41,42,43,44,50,58,59,60,61,102,103,105,106,107,108,109,110,111,114,115,116,117,125,143,145,146,147,],[-74,-76,-78,-79,-80,-52,-57,-58,-61,-62,-65,-66,82,-46,-47,-48,-49,-59,-60,-75,-77,-81,-64,-82,-50,-51,-53,-54,-55,-56,150,-63,-95,-96,-94,]),'SIGUIENTE':([31,32,33,34,35,38,39,40,41,42,43,44,51,102,103,105,106,107,108,109,110,111,114,115,116,117,143,145,146,147,],[-74,-76,-78,-79,-80,-52,-57,-58,-61,-62,-65,-66,83,-59,-60,-75,-77,-81,-64,-82,-50,-51,-53,-54,-55,-56,-63,-95,-96,-94,]),')':([31,32,33,34,35,38,39,40,41,42,43,44,56,66,67,79,84,85,87,88,89,90,98,101,102,103,105,106,107,108,109,110,111,114,115,116,117,118,119,120,121,122,123,143,145,146,147,153,159,167,],[-74,-76,-78,-59,-60,-52,-57,-58,-61,-62,-65,-66,-32,107,108,-67,126,127,-12,-13,-14,-15,129,108,-59,-60,-75,-77,-81,-64,-82,-50,-51,-53,-54,-55,-56,143,-68,-69,145,146,147,-63,-95,-96,-94,-33,-70,-34,]),'AND':([31,32,33,34,35,38,39,40,41,42,43,44,102,103,105,106,107,108,109,110,111,114,115,116,117,143,145,146,147,],[65,-76,-78,-79,-80,-52,-57,-58,-61,-62,-65,-66,-59,-60,65,-77,-81,-64,-82,-50,-51,-53,-54,-55,-56,-63,-95,-96,-94,]),'*':([34,35,38,39,40,41,42,43,44,59,60,94,95,102,103,108,110,111,114,115,116,117,143,145,146,147,],[-59,-60,75,-57,-58,-61,-62,-65,-66,-59,-60,-59,-60,-59,-60,-64,75,75,-53,-54,-55,-56,-63,-95,-96,-94,]),'/':([34,35,38,39,40,41,42,43,44,59,60,94,95,102,103,108,110,111,114,115,116,117,143,145,146,147,],[-59,-60,76,-57,-58,-61,-62,-65,-66,-59,-60,-59,-60,-59,-60,-64,76,76,-53,-54,-55,-56,-63,-95,-96,-94,]),'RESTO':([34,35,38,39,40,41,42,43,44,59,60,94,95,102,103,108,110,111,114,115,116,117,143,145,146,147,],[-59,-60,77,-57,-58,-61,-62,-65,-66,-59,-60,-59,-60,-59,-60,-64,77,77,-53,-54,-55,-56,-63,-95,-96,-94,]),'^':([34,35,38,39,40,41,42,43,44,59,60,94,95,102,103,108,110,111,114,115,116,117,143,145,146,147,],[-59,-60,78,-57,-58,-61,-62,-65,-66,-59,-60,-59,-60,-59,-60,-64,78,78,-53,-54,-55,-56,-63,-95,-96,-94,]),'+':([34,35,37,38,39,40,41,42,43,44,59,60,61,67,94,95,96,101,102,103,108,109,110,111,114,115,116,117,120,121,143,145,146,147,159,],[-59,-60,69,-52,-57,-58,-61,-62,-65,-66,-59,-60,69,69,-59,-60,69,69,-59,-60,-64,69,-50,-51,-53,-54,-55,-56,69,69,-63,-95,-96,-94,69,]),'-':([34,35,37,38,39,40,41,42,43,44,59,60,61,67,94,95,96,101,102,103,108,109,110,111,114,115,116,117,120,121,143,145,146,147,159,],[-59,-60,70,-52,-57,-58,-61,-62,-65,-66,-59,-60,70,70,-59,-60,70,70,-59,-60,-64,70,-50,-51,-53,-54,-55,-56,70,70,-63,-95,-96,-94,70,]),'>':([34,35,37,38,39,40,41,42,43,44,67,102,103,108,110,111,114,115,116,117,143,145,146,147,],[-59,-60,71,-52,-57,-58,-61,-62,-65,-66,71,-59,-60,-64,-50,-51,-53,-54,-55,-56,-63,-95,-96,-94,]),'<':([34,35,37,38,39,40,41,42,43,44,67,102,103,108,110,111,114,115,116,117,143,145,146,147,],[-59,-60,72,-52,-57,-58,-61,-62,-65,-66,72,-59,-60,-64,-50,-51,-53,-54,-55,-56,-63,-95,-96,-94,]),'IGUAL':([34,35,37,38,39,40,41,42,43,44,67,71,72,102,103,108,110,111,114,115,116,117,143,145,146,147,],[-59,-60,73,-52,-57,-58,-61,-62,-65,-66,73,112,113,-59,-60,-64,-50,-51,-53,-54,-55,-56,-63,-95,-96,-94,]),'DIFERENTE':([34,35,37,38,39,40,41,42,43,44,67,102,103,108,110,111,114,115,116,117,143,145,146,147,],[-59,-60,74,-52,-57,-58,-61,-62,-65,-66,74,-59,-60,-64,-50,-51,-53,-54,-55,-56,-63,-95,-96,-94,]),'BOOLEANO':([53,100,128,154,157,162,],[89,136,89,89,136,89,]),'[':([57,100,157,],[100,100,100,]),']':([100,131,132,133,134,135,136,137,138,139,156,163,],[131,-21,156,-23,-25,-26,-27,-28,-29,-30,-22,-24,]),'CONTRARIO':([142,],[158,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'prg':([0,],[1,]),'declarations':([0,161,],[2,166,]),'decl':([0,2,161,166,],[3,11,3,11,]),'declV':([0,2,161,166,],[4,4,4,4,]),'declF':([0,2,161,166,],[5,5,5,5,]),'declL':([0,2,161,166,],[6,6,6,6,]),'statements':([2,63,82,150,158,166,],[10,104,124,160,164,169,]),'stat':([2,10,63,82,104,124,150,158,160,164,166,169,],[12,27,12,12,27,27,12,12,27,27,12,27,]),'atrib':([2,10,63,82,83,104,124,150,158,160,164,166,169,],[13,13,13,13,125,13,13,13,13,13,13,13,13,]),'conditions':([2,10,63,82,104,124,150,158,160,164,166,169,],[14,14,14,14,14,14,14,14,14,14,14,14,]),'ciclos':([2,10,63,82,104,124,150,158,160,164,166,169,],[15,15,15,15,15,15,15,15,15,15,15,15,]),'write':([2,10,63,82,104,124,150,158,160,164,166,169,],[16,16,16,16,16,16,16,16,16,16,16,16,]),'vari':([7,],[22,]),'atribD':([7,54,],[23,91,]),'expL':([18,19,20,36,],[30,50,51,66,]),'termoB':([18,19,20,36,64,],[31,31,31,31,105,]),'fatorB':([18,19,20,36,64,65,],[32,32,32,32,32,106,]),'condition':([18,19,20,36,64,65,],[33,33,33,33,33,33,]),'exp':([18,19,20,29,36,55,62,64,65,68,79,80,144,],[37,37,37,61,67,96,101,37,37,109,120,121,159,]),'termo':([18,19,20,29,36,55,62,64,65,68,69,70,79,80,144,],[38,38,38,38,38,38,38,38,38,38,110,111,38,38,38,]),'fator':([18,19,20,29,36,55,62,64,65,68,69,70,75,76,77,78,79,80,144,],[39,39,39,39,39,39,39,39,39,39,39,39,114,115,116,117,39,39,39,]),'cast':([18,19,20,29,36,55,62,64,65,68,69,70,75,76,77,78,79,80,144,],[43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'read':([18,19,20,29,36,55,62,64,65,68,69,70,75,76,77,78,79,80,144,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'tipocast':([18,19,20,29,36,55,62,64,65,68,69,70,75,76,77,78,79,80,144,],[45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,]),'op':([37,67,],[68,68,]),'tipo':([53,128,154,162,],[86,153,161,167,]),'parametros':([56,],[98,]),'lista':([57,100,157,],[99,139,139,]),'content_params':([79,],[118,]),'list_params':([79,],[119,]),'elementos':([100,],[132,]),'elemento':([100,157,],[133,163,]),'endcondition':([104,],[140,]),'return':([170,],[172,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> prg","S'",1,None,None,None),
  ('prg -> declarations statements','prg',2,'p_prg','yacc.py',9),
  ('declarations -> decl','declarations',1,'p_declarations_1','yacc.py',15),
  ('declarations -> declarations decl','declarations',2,'p_declarations_mult','yacc.py',28),
  ('decl -> declV','decl',1,'p_decl_V','yacc.py',41),
  ('decl -> declF','decl',1,'p_decl_F','yacc.py',45),
  ('decl -> declL','decl',1,'p_decl_L','yacc.py',49),
  ('declV -> VAR vari : tipo','declV',4,'p_declV','yacc.py',56),
  ('vari -> atribD','vari',1,'p_vari_atrib','yacc.py',72),
  ('vari -> ID','vari',1,'p_vari_id','yacc.py',76),
  ('vari -> vari , atribD','vari',3,'p_vari_atribs','yacc.py',81),
  ('vari -> vari , ID','vari',3,'p_vari_ids','yacc.py',85),
  ('tipo -> ENTERO','tipo',1,'p_tipo_int','yacc.py',90),
  ('tipo -> REAL','tipo',1,'p_tipo_REAL','yacc.py',94),
  ('tipo -> BOOLEANO','tipo',1,'p_tipo_BOOL','yacc.py',99),
  ('tipo -> STR','tipo',1,'p_tipo_STRING','yacc.py',103),
  ('atribD -> ID = STRING','atribD',3,'p_atribD_string','yacc.py',107),
  ('atribD -> ID = VERDADERO','atribD',3,'p_atribD_true','yacc.py',112),
  ('atribD -> ID = FALSO','atribD',3,'p_atribD_false','yacc.py',117),
  ('atribD -> ID = exp','atribD',3,'p_atribD','yacc.py',122),
  ('declL -> LISTA ID = lista','declL',4,'p_declL','yacc.py',131),
  ('lista -> [ ]','lista',2,'p_lista_vazia','yacc.py',136),
  ('lista -> [ elementos ]','lista',3,'p_lista_elem','yacc.py',140),
  ('elementos -> elemento','elementos',1,'p_elementos_1','yacc.py',144),
  ('elementos -> elementos , elemento','elementos',3,'p_elementos_mult','yacc.py',148),
  ('elemento -> INT','elemento',1,'p_elemento_INT','yacc.py',152),
  ('elemento -> FLOAT','elemento',1,'p_elemento_FLOAT','yacc.py',157),
  ('elemento -> BOOLEANO','elemento',1,'p_elemento_BOOL','yacc.py',162),
  ('elemento -> STRING','elemento',1,'p_elemento_STRING','yacc.py',167),
  ('elemento -> ID','elemento',1,'p_elemento_ID','yacc.py',172),
  ('elemento -> lista','elemento',1,'p_elemento_lista','yacc.py',177),
  ('declF -> FUNCION ID ( parametros ) : tipo declarations statements DEVUELVE return .','declF',12,'p_declF_parametros','yacc.py',185),
  ('parametros -> <empty>','parametros',0,'p_parametros_0','yacc.py',198),
  ('parametros -> ID : tipo','parametros',3,'p_parametros_1','yacc.py',205),
  ('parametros -> parametros , ID : tipo','parametros',5,'p_parametros_mult','yacc.py',214),
  ('return -> INT','return',1,'p_return_INT','yacc.py',223),
  ('return -> ID','return',1,'p_return_ID','yacc.py',227),
  ('return -> FLOAT','return',1,'p_return_FLOAT','yacc.py',231),
  ('return -> VERDADERO','return',1,'p_return_TRUE','yacc.py',235),
  ('return -> FALSO','return',1,'p_return_FALSE','yacc.py',239),
  ('statements -> stat','statements',1,'p_statements_1','yacc.py',247),
  ('statements -> statements stat','statements',2,'p_statements_mult','yacc.py',251),
  ('stat -> atrib ;','stat',2,'p_stat_atrib','yacc.py',255),
  ('stat -> conditions','stat',1,'p_stat_conditions','yacc.py',259),
  ('stat -> ciclos','stat',1,'p_stat_ciclos','yacc.py',263),
  ('stat -> write','stat',1,'p_stat_write','yacc.py',267),
  ('atrib -> ID = STRING','atrib',3,'p_atrib_string','yacc.py',274),
  ('atrib -> ID = VERDADERO','atrib',3,'p_atrib_true','yacc.py',281),
  ('atrib -> ID = FALSO','atrib',3,'p_atrib_false','yacc.py',289),
  ('atrib -> ID = exp','atrib',3,'p_atrib','yacc.py',297),
  ('exp -> exp + termo','exp',3,'p_exp_soma','yacc.py',308),
  ('exp -> exp - termo','exp',3,'p_exp_sub','yacc.py',313),
  ('exp -> termo','exp',1,'p_exp_termo','yacc.py',318),
  ('termo -> termo * fator','termo',3,'p_termo_mul','yacc.py',322),
  ('termo -> termo / fator','termo',3,'p_termo_div','yacc.py',327),
  ('termo -> termo RESTO fator','termo',3,'p_termo_resto','yacc.py',332),
  ('termo -> termo ^ fator','termo',3,'p_termo_pot','yacc.py',337),
  ('termo -> fator','termo',1,'p_termo_fator','yacc.py',353),
  ('fator -> INT','fator',1,'p_fator_INT','yacc.py',357),
  ('fator -> VERDADERO','fator',1,'p_fator_VERDADERO','yacc.py',361),
  ('fator -> FALSO','fator',1,'p_fator_FALSO','yacc.py',365),
  ('fator -> FLOAT','fator',1,'p_fator_FLOAT','yacc.py',369),
  ('fator -> ID','fator',1,'p_fator_ID','yacc.py',373),
  ('fator -> ID ( content_params )','fator',4,'p_fator_FUNC','yacc.py',377),
  ('fator -> ( exp )','fator',3,'p_fator_exp','yacc.py',407),
  ('fator -> cast','fator',1,'p_fator_cast','yacc.py',411),
  ('fator -> read','fator',1,'p_fator_read','yacc.py',415),
  ('content_params -> <empty>','content_params',0,'p_content_paramns_0','yacc.py',419),
  ('content_params -> list_params','content_params',1,'p_content_paramns_1','yacc.py',423),
  ('list_params -> exp','list_params',1,'p_params_function_1','yacc.py',427),
  ('list_params -> list_params , exp','list_params',3,'p_params_function_mult','yacc.py',431),
  ('conditions -> SI expL ENTONCES statements endcondition','conditions',5,'p_conditions_si','yacc.py',438),
  ('endcondition -> .','endcondition',1,'p_endcpndition','yacc.py',445),
  ('endcondition -> CASO CONTRARIO statements .','endcondition',4,'p_conditions_si_no','yacc.py',450),
  ('expL -> termoB','expL',1,'p_expL_1','yacc.py',456),
  ('expL -> expL OR termoB','expL',3,'p_expL_mult','yacc.py',460),
  ('termoB -> fatorB','termoB',1,'p_termoB_1','yacc.py',464),
  ('termoB -> termoB AND fatorB','termoB',3,'p_termoB_mult','yacc.py',468),
  ('fatorB -> condition','fatorB',1,'p_fatorB_condition','yacc.py',472),
  ('fatorB -> VERDADERO','fatorB',1,'p_fatorB_VERDADERO','yacc.py',476),
  ('fatorB -> FALSO','fatorB',1,'p_fatorB_FALSE','yacc.py',480),
  ('fatorB -> ( expL )','fatorB',3,'p_fatorB_expL','yacc.py',484),
  ('condition -> exp op exp','condition',3,'p_condition','yacc.py',488),
  ('op -> >','op',1,'p_op_maior','yacc.py',492),
  ('op -> <','op',1,'p_op_menor','yacc.py',496),
  ('op -> IGUAL','op',1,'p_op_IGUAL','yacc.py',500),
  ('op -> DIFERENTE','op',1,'p_op_DIFERENTE','yacc.py',504),
  ('op -> > IGUAL','op',2,'p_op_maiorIGUAL','yacc.py',508),
  ('op -> < IGUAL','op',2,'p_op_menorIGUAL','yacc.py',512),
  ('ciclos -> ENCUANTO expL HACER statements .','ciclos',5,'p_ciclos_while','yacc.py',520),
  ('ciclos -> PARA expL SIGUIENTE atrib .','ciclos',5,'p_ciclos_for_1','yacc.py',525),
  ('ciclos -> PARA expL SIGUIENTE atrib HACER statements .','ciclos',7,'p_ciclos_for_mult','yacc.py',530),
  ('write -> ESCRIBIR ( ID ) ;','write',5,'p_write_r','yacc.py',540),
  ('write -> ESCRIBIR ( STRING ) ;','write',5,'p_write_r_string','yacc.py',544),
  ('read -> LEER ( STRING )','read',4,'p_read_w','yacc.py',548),
  ('cast -> tipocast ( exp )','cast',4,'p_cast_exp','yacc.py',556),
  ('cast -> tipocast ( STRING )','cast',4,'p_cast_string','yacc.py',560),
  ('tipocast -> REAL','tipocast',1,'p_tipocast_float','yacc.py',564),
  ('tipocast -> ENTERO','tipocast',1,'p_tipocast_int','yacc.py',568),
  ('tipocast -> STR','tipocast',1,'p_tipocast_string','yacc.py',572),
]
