from LinguaPythonica.Laspak.Sounds import (
    LaspakConsonant,
    LaspakVowel,
)

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

# Dictionnaire pour récupérer à partir des symboles -- On rajoute aussi les majuscules
LASPAK_CONSONANTS_DICT = {lettre.symbol:lettre for lettre in LASPAK_CONSONANTS}
LASPAK_CONSONANTS_DICT = dict(LASPAK_CONSONANTS_DICT,**{lettre.symbol.upper():lettre for lettre in LASPAK_CONSONANTS})
LASPAK_VOWELS_DICT     = {lettre.symbol:lettre for lettre in LASPAK_VOWELS}
LASPAK_VOWELS_DICT     = dict(LASPAK_VOWELS_DICT,**{lettre.symbol.upper():lettre for lettre in LASPAK_VOWELS})