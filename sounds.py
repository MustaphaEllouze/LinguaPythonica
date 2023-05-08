from sounds_class import(
    Consonant,
    Vowel,
)

CONS_list = [
    Consonant(
        'm',
        nasal=True,
        labial=True,
        voiced=True,
    ),
    
    Consonant(
        'n',
        nasal=True,
        alveo=True,
        voiced=True,
    ),

    Consonant(
        'p',
        stop=True,
        labial=True,
        unvoiced=True,
    ),

    Consonant(
        't',
        stop=True,
        alveo=True,
        unvoiced=True,
    ),
    
    Consonant(
        'd',
        stop=True,
        alveo=True,
        voiced=True,
    ),
    
    Consonant(
        'k',
        stop=True,
        velar=True,
        unvoiced=True,
    ),
    
    Consonant(
        'g',
        stop=True,
        velar=True,
        voiced=True,
    ),
    
    Consonant(
        '\'',
        stop=True,
        glottal=True,
        voiced=True,
    ),

    Consonant(
        's',
        fric=True,
        alveo=True,
        unvoiced=True,
    ),

    
    Consonant(
        'z',
        fric=True,
        alveo=True,
        voiced=True,
    ),

    Consonant(
        'ch',
        fric=True,
        postalveo=True,
        unvoiced=True,
    ),

    Consonant(
        'f',
        fric=True,
        labial=True,
        unvoiced=True,
    ),

    Consonant(
        'th',
        fric=True,
        dental=True,
        unvoiced=True,
    ),

    Consonant(
        'y',
        liquid=True,
        palatal=True,
        voiced=True,
    ),

    Consonant(
        'w',
        liquid=True,
        labial=True,
        voiced=True,
    ),

    Consonant(
        'l',
        liquid=True,
        alveo=True,
        unvoiced=True,
    ),
    
    Consonant(
        'r',
        liquid=True,
        alveo=True,
        voiced=True,
    ),
]

VOWE_list = [
    Vowel(
        'a',
        central=True,
        open=True,
    ),
    Vowel(
        'é',
        front=True,
        semiclose=True,
    ),
    Vowel(
        'i',
        front=True,
        close=True,
    ),
    Vowel(
        'o',
        back=True,
        semiclose=True,
    ),
    Vowel(
        'u',
        back=True,
        close=True,
    ),
    Vowel(
        'e',
        central=True,
        semiclose=True,
    ),
]

CONS = {}
for con in CONS_list:
    globals()[con.symbol] = con
    CONS[con.symbol] = con

VOWE = {}
for vow in VOWE_list:
    globals()[vow.symbol] = vow
    VOWE[vow.symbol] = vow