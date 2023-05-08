from sounds import (
    CONS,
    VOWE,
)

from sounds_class import (
    Vowel,
    Consonant,
)

from collections import defaultdict

class Word :
    words = []
    translations_str = defaultdict(list)
    translations = defaultdict(list)

    def __init__(self,
                letters,
                translation=None,
                add_dictionnary = True,
                extend_variations = None,
                ):
        self.letters = []
        for l in letters:
            if(l in VOWE.keys()):
                self.letters.append(VOWE[l])
            elif(l in CONS.keys()):
                self.letters.append(CONS[l])
            else:
                raise Exception('Lettre inconnue : '+str(l.symbol))
        self.translation = translation
        self.is_verb = False
        self.is_copula = False
        self.is_pronoun = False
        self.symbols = [let.symbol for let in self.letters]
        if(add_dictionnary) : Word.words.append(self)
        self.variations = [self]
        if(not extend_variations is None):
            extend_variations.variations.append(self)
        Word.translations_str[translation].append(str(self))
        Word.translations[translation].append(self)
    
    def __str__(self):
        res = ''
        for s in [let.symbol for let in self.letters] : res += s
        return res
    
    def plural(self):
        for i,let in enumerate(self.letters[::-1]):
            if(type(let) is Vowel):
                break
        
        
        if(let.symbol == 'a'):
            letter_to_insert = 'e'
        elif(let.symbol == 'é'):
            letter_to_insert = 'i'
        elif(let.symbol == 'i'):
            letter_to_insert = 'i'
        elif(let.symbol == 'o'):
            letter_to_insert = 'u'
        elif(let.symbol == 'u'):
            letter_to_insert = 'u'
        elif(let.symbol == 'e'):
            letter_to_insert = 'i'
        else:
            raise Exception('Vowel non reconnue, ou pas de Vowel')

        resultat = self.symbols.copy()
        resultat.insert(len(self.letters)-i,letter_to_insert)

        return Word(
            resultat,
            translation=self.translation+'.PLU',
            add_dictionnary=False,
            extend_variations = self,
        )
    
    def masculine(self):
        return Word(
            self.symbols+['e'],
            translation=self.translation+'.MASC',
            add_dictionnary=False,
            extend_variations = self,
        )
    
    def genetive_abs(self):
        return Word(
            self.symbols+list('pfoe'),
            translation=self.translation+'.GEN-ABS',
            add_dictionnary=False,
            extend_variations = self,
        )
    
    def genetive_erg(self):
        return Word(
            self.symbols+list('kral'),
            translation=self.translation+'.GEN-ERG',
            add_dictionnary=False,
            extend_variations = self,
        )
    
    def substantive (self):
        return Word(
            self.symbols+['ch','o','s'],
            translation=self.translation+'.SUBS',
            add_dictionnary=False,
            extend_variations = self,
        )

    def get_word_from_tr(translation):
        return Word.translations[translation][0]
    

class Verb(Word):
    verbs = []
    def __init__(self,
                letters,
                translation=None,
                add_dictionnary=True,
                extend_variations = None,
                check_rules=True,
                ):
        super().__init__(letters, translation=translation, add_dictionnary=add_dictionnary,extend_variations=extend_variations)
        if(check_rules) : self.check_rules()
        self.is_verb = True
        Verb.verbs.append(self)
    
    def conjugate(self,
                 tense,
                 name_tense):
        first_part = list(str(self)[:-1])
        second_part = list(str(self)[-1])
        res = {
            pronoun:
                Verb(
                    first_part+tense[pronoun][0]+second_part+tense[pronoun][1],
                    translation=self.translation+'.'+pronoun+'.'+name_tense,
                    add_dictionnary=False,
                    extend_variations=self,
                    check_rules=False,
                    ) 
            for pronoun in tense.keys()
            }
        return res
        
    def check_rules(self):
        if(self.letters[-1].liquid or self.letters[-1].nasal):
            if(self.letters[-2].symbol !='a'):
                raise Exception('Mauvaise terminaison verbe : '+str(self))
        if(self.letters[-1].fric):
            if(self.letters[-2].symbol !='i'):
                raise Exception('Mauvaise terminaison verbe : '+str(self))
        if(self.letters[-1].stop):
            if(self.letters[-2].symbol !='o'):
                raise Exception('Mauvaise terminaison verbe : '+str(self))