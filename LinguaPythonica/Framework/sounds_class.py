class Consonant :
    
    consonants = {}

    def __init__(self,
                symbol,
                stop        =False,
                fric        =False,
                liquid      =False,
                nasal       =False,
                voiced      =False,
                unvoiced    =False,
                labial      =False,
                dental      =False,
                alveo       =False,
                postalveo   =False,
                palatal     =False,
                velar       =False,
                glottal     =False,
                ):

        self.symbol = symbol

        if(sum([stop,fric,liquid,nasal])!=1):
            raise Exception('Mauvais type stop fric liquid nasal')
        
        if(sum([voiced,unvoiced])!=1):
            raise Exception('Mauvais type voiced unvoiced')

        if(sum([labial,dental,alveo,postalveo,palatal,velar,glottal])!=1):
            raise Exception('Mauvais type labial alveo postalveo palatal velar glottal dental')

        self.stop = stop
        self.fric = fric
        self.liquid = liquid
        self.nasal = nasal
        self.voiced = voiced
        self.unvoiced = unvoiced
        self.labial = labial
        self.dental = dental
        self.alveo = alveo
        self.postalveo = postalveo
        self.palatal = palatal
        self.velar = velar
        self.glottal = glottal

        Consonant.consonants[self.symbol]=self

class Vowel : 

    vowels = {}

    def __init__(self,
                symbol      =False,
                front       =False,
                central     =False,
                back        =False, 
                close       =False, 
                semiclose    =False,
                open        =False,
                ):
        
        self.symbol = symbol

        if(sum([front,central,back])!=1):
            raise Exception('Mauvais type front central back')
        
        if(sum([close,open,semiclose])!=1):
            raise Exception('Mauvais type rounded unrounded')

        self.front = front
        self.central = central
        self.back = back
        self.close = close
        self.open = open
        self.semiclose = semiclose

        Vowel.vowels[self.symbol]=self

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
        "'",
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