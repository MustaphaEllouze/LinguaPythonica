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

class LaspakVowel(Vowel,LaspakSound):
    """Voyelles du Laspak
    """

    # Dictionnaire des instances
    laspak_vowels = {}

    def __init__(self,*args,**kwargs):
        """Constructeur, la construction est gérée par Vowel"""
        super().__init__(*args,**kwargs)
        LaspakVowel.laspak_vowels[self.symbol]=self

# Définition des consonnes
LASPAK_CONSONANTS = [
    LaspakConsonant(
        'm',
        nasal=True,
        labial=True,
        voiced=True,
    ),

    LaspakConsonant(
        'p',
        stop=True,
        labial=True,
        unvoiced=True,
    ),

    LaspakConsonant(
        'b',
        stop=True,
        labial=True,
        voiced=True,
    ),

    LaspakConsonant(
        't',
        stop=True,
        alveo=True,
        unvoiced=True,
    ),

    LaspakConsonant(
        'd',
        stop=True,
        alveo=True,
        voiced=True,
    ),
    
    LaspakConsonant(
        'f',
        fric=True,
        labial=True,
        unvoiced=True,
    ),

    LaspakConsonant(
        'v',
        fric=True,
        labial=True,
        unvoiced=True,
    ),

    LaspakConsonant(
        'th',
        fric=True,
        dental=True,
        unvoiced=True,
    ),
    
    LaspakConsonant(
        'n',
        nasal=True,
        alveo=True,
        voiced=True,
    ),
    
    LaspakConsonant(
        's',
        fric=True,
        alveo=True,
        unvoiced=True,
    ),
    
    LaspakConsonant(
        'z',
        fric=True,
        alveo=True,
        voiced=True,
    ),

    LaspakConsonant(
        'ch',
        fric=True,
        postalveo=True,
        unvoiced=True,
    ),

    LaspakConsonant(
        'j',
        fric=True,
        postalveo=True,
        voiced=True,
    ),
    
    LaspakConsonant(
        'y',
        liquid=True,
        palatal=True,
        voiced=True,
    ),

    LaspakConsonant(
        'r',
        liquid=True,
        alveo=True,
        voiced=True,
    ),
    
    LaspakConsonant(
        'l',
        liquid=True,
        alveo=True,
        unvoiced=True,
    ),

    LaspakConsonant(
        'w',
        liquid=True,
        labial=True,
        voiced=True,
    ),

    LaspakConsonant(
        'k',
        stop=True,
        velar=True,
        unvoiced=True,
    ),
    
    LaspakConsonant(
        'g',
        stop=True,
        velar=True,
        voiced=True,
    ),

    LaspakConsonant(
        'q',
        stop=True,
        uvular=True,
        unvoiced=True,
    ),

    LaspakConsonant(
        'x',
        fric=True,
        velar=True,
        unvoiced=True,
    ),

    LaspakConsonant(
        'h',
        fric=True,
        glottal=True,
        unvoiced=True,
    ),
    
    LaspakConsonant(
        '\'',
        stop=True,
        glottal=True,
        voiced=True,
    ),
   
]

# Définition des voyelles
LASPAK_VOWELS = [
    LaspakVowel(
        'a',
        central=True,
        open=True,
    ),
    LaspakVowel(
        'e',
        front=True,
        semiclose=True,
    ),
    LaspakVowel(
        'i',
        front=True,
        close=True,
    ),
    LaspakVowel(
        'o',
        back=True,
        semiclose=True,
    ),
    LaspakVowel(
        'u',
        back=True,
        close=True,
    ),
]