from LinguaPythonica.RedDjinn.Words import (
    Word,
)

from LinguaPythonica.Framework.Sounds import (
    Vowel,
    Consonant,
)

from copy import deepcopy

def diphtongue(word:Word):

    resultat = word.letters.copy()
    resultat2 = []

    dic_modif = {
        'a':{
            'é':list('aé') ,
            'i':list('ay') ,
            'o':list('aw') ,
            'u':list('awu'),
            'e':list('ae') ,
        },
        'é':{
            'a':list('éa') ,
            'i':list('éy') ,
            'o':list('éw') ,
            'u':list('éwu'),
            'e':list('éw') ,
        },
        'i':{
            'a':list('iya') ,
            'é':list('iyé') ,
            'o':list('io')  ,
            'u':list('iw')  ,
            'e':list('ie')  ,
        },
        'o':{
            'a':list('owa') ,
            'é':list('owé') ,
            'i':list('oy') ,
            'u':list('owu'),
            'e':list('o') ,
        },
        'u':{
            'a':list('wa') ,
            'é':list('wé') ,
            'i':list('wyi') ,
            'o':list('uwo'),
            'e':list('u') ,
        },
        'e':{
            'a':list('ea'),
            'é':list('wé'),
            'i':list('ey'),
            'o':list('wo'),
            'u':list('ew'),
        },
    }
    i = 0
    while(i<len(resultat)-1):
        let = resultat[i]
        let2= resultat[i+1]
        if type(let) is Vowel and type(resultat[i+1]) is Vowel:
            resultat2 += dic_modif[let.symbol][let2.symbol]
            i += 1
        else:
            resultat2 += [let.symbol]
        i += 1
    if(i==len(resultat)-1) : resultat2 += [resultat[i].symbol]
    return Word(
        resultat2,
        translation=word.translation,
        add_dictionnary=False,
        extend_variations=word
    )

def change_w(word:Word):
    indices = [i for i,let in enumerate(word.letters) if (let.symbol=='w' and 0<i<len(word.letters) and (type(word.letters[i-1]) is Vowel or word.symbols[i-1]=='f'))]
    new_letters = [let if not i in indices else 'f' for i,let in enumerate(word.symbols)]
    return Word(
        new_letters,
        translation=word.translation,
        add_dictionnary=False,
    )

def change_r(word:Word):
    if(not word.symbols[-1] == 'r'):
        return word
    else:
        return Word(
            word.symbols[:-1]+['l'],
            translation=word.translation,
            add_dictionnary=False,
        )

def glottal_pre_stop(word:Word):
    resultat_symbols = []
    for i,let in enumerate(word.letters[:-1]):
        if(let.symbol=='\'' and type(word.letters[i+1]) is Consonant and word.letters[i+1].stop):
            resultat_symbols.append(word.letters[i+1].symbol)
        else:
            resultat_symbols.append(let.symbol)
    resultat_symbols.append(word.symbols[-1])
    return Word(
        resultat_symbols,
        translation=word.translation,
        add_dictionnary=False,
    )

def evolution(word:Word):
    order = [
        diphtongue,
        change_w,
        change_r,
        glottal_pre_stop,
    ]
    
    resultat = deepcopy(word)
    
    for func in order:
        resultat = func(resultat)
    
    return resultat

def evolution_str(word:Word):
    return str(evolution(word))

def evolution_dict(dic:dict):
    return {k:evolution(w) for k,w in dic.items()}

def evolution_dict_str(dic:dict):
    return {k:evolution_str(w) for k,w in dic.items()}