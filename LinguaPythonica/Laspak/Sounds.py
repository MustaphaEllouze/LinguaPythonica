from abc import ABC,abstractmethod
from LinguaPythonica.Framework.Sounds import(
    Sound,
    Consonant,
    Vowel,
)

class LaspakSound(Sound,ABC):
    """Sons du Laspak
    """

    @abstractmethod
    def __init__(self):
        pass

class LaspakConsonant(Consonant,LaspakSound):
    """Consonnes du Laspak
    """

    # Dictionnaire des instances
    laspak_consonants = {}

    def __init__(self,*args,**kwargs):
        """Constructeur, la construction est gérée par Consonant"""
        super().__init__(*args,**kwargs)
        LaspakConsonant.laspak_consonants[self.symbol]=self
        LaspakConsonant.laspak_consonants[self.symbol.upper()]=self

class LaspakVowel(Vowel,LaspakSound):
    """Voyelles du Laspak
    """

    # Dictionnaire des instances
    laspak_vowels = {}

    def __init__(self,*args,**kwargs):
        """Constructeur, la construction est gérée par Vowel"""
        super().__init__(*args,**kwargs)
        LaspakVowel.laspak_vowels[self.symbol]=self
        LaspakVowel.laspak_vowels[self.symbol.upper()]=self

