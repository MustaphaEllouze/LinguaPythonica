from LinguaPythonica.RedDjinn import (
    sounds
)

from LinguaPythonica.RedDjinn.sounds import (
    CONS_list,
    VOWE_list,
)
from LinguaPythonica.RedDjinn.Words import (
    Word,
    Verb,
)

from LinguaPythonica.RedDjinn.words_class_specific import (
    Copula,
)

from LinguaPythonica.RedDjinn.tense import (
    Tense,
)

from LinguaPythonica.RedDjinn.dictionanry import WORDS

from LinguaPythonica.RedDjinn.evolutions import (
    evolution,
    evolution_str,
    evolution_dict,
    evolution_dict_str,
)

manger = Word.get_word_from_tr('Manger')
manger_conj = Tense.conjugate(manger,Tense.PRES)
manger_conj_evol = evolution_dict_str(manger_conj)
#print(manger_conj_evol)

la = Word.get_word_from_tr('La')
femme = Word.get_word_from_tr('Femme')
neutr = Word.get_word_from_tr('Neutralité.COP')
pomme=Word.get_word_from_tr('Pomme')

print(neutr.mood('HAB'),manger_conj['1.sg.f'],pomme)
print(evolution_str(neutr.mood('HAB')),evolution_str(manger_conj['1.sg.f']),evolution_str(pomme))
