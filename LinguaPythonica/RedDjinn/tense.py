from LinguaPythonica.RedDjinn.words_class_specific import (
    PROUN,
)
from LinguaPythonica.RedDjinn.concepts_specific import (
    GEND,
)

from LinguaPythonica.Framework.words_class import (
    Verb,
)

class Tense:

    PRES = {
        '1.sg.f' : (list('o'),list('')  ), 
        '1.sg.m' : (list('o'),list('e') ),
        '2.sg.f' : (list('u'),list('')  ),
        '2.sg.m' : (list('u'),list('e') ),
        '3.sg.f' : (list('é'),list('')  ),
        '3.sg.m' : (list('é'),list('e') ),
        '1.pl.f' : (list('no'),list('') ),
        '1.pl.m' : (list('no'),list('e')),
        '2.pl.f' : (list('fu'),list('') ),
        '2.pl.m' : (list('fu'),list('e')),
        '3.pl.f' : (list('li'),list('') ),
        '3.pl.m' : (list('li'),list('e')),
    }

    PAST = {
        '1.sg.f' : (list('wo'),list('')  ), 
        '1.sg.m' : (list('wo'),list('e') ),
        '2.sg.f' : (list('wu'),list('')  ),
        '2.sg.m' : (list('wu'),list('e') ),
        '3.sg.f' : (list('wé'),list('')  ),
        '3.sg.m' : (list('wé'),list('e') ),
        '1.pl.f' : (list('nwo'),list('') ),
        '1.pl.m' : (list('nwo'),list('e')),
        '2.pl.f' : (list('fwu'),list('') ),
        '2.pl.m' : (list('fwu'),list('e')),
        '3.pl.f' : (list('lwi'),list('') ),
        '3.pl.m' : (list('lwi'),list('e')),
    }

    FUT = {
        '1.sg.f' : (list('ro'),list('')  ), 
        '1.sg.m' : (list('ro'),list('e') ),
        '2.sg.f' : (list('ru'),list('')  ),
        '2.sg.m' : (list('ru'),list('e') ),
        '3.sg.f' : (list('ré'),list('')  ),
        '3.sg.m' : (list('ré'),list('e') ),
        '1.pl.f' : (list('nro'),list('') ),
        '1.pl.m' : (list('nro'),list('e')),
        '2.pl.f' : (list('fru'),list('') ),
        '2.pl.m' : (list('fru'),list('e')),
        '3.pl.f' : (list('lri'),list('') ),
        '3.pl.m' : (list('lri'),list('e')),
    }

    def conjugate(verb:Verb,tense):
        if(tense==Tense.PRES)   : name_tense = 'PRES'
        elif(tense==Tense.PAST) : name_tense = 'PAST'
        elif(tense==Tense.FUT)  : name_tense = 'FUT'
        return verb.conjugate(tense,name_tense)
    
    def conjugate_str(verb:Verb,tense):
        return {pers:str(v) for pers,v in Tense.conjugate(verb,tense).items()}
