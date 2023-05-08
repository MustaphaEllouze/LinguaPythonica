from abc import ABC,abstractmethod

class Sound(ABC):
    """Représente un son (voyelle ou consonne).
    Classe abstraite
    """

    @abstractmethod
    def __init__(self) -> None:
        pass

class Consonant(Sound):
    """Représente une consonne

    Class Attributes : 
        - consonants    : dict{str:Consonant}   : Clés = symboles

    Attributes : 
        - symbol        :   str     : Symbole qui représente

        - stop          :   bool    : Stop  
        - fric          :   bool    : Fricative  
        - liquid        :   bool    : Liquide  
        - nasal         :   bool    : Nasale  
        
        - voiced        :   bool    : Voisée
        - unvoiced      :   bool    : Non voisée

        - labial        :   bool    : Labiale  
        - dental        :   bool    : Dentale  
        - alveo         :   bool    : Alvéolaire  
        - postalveo     :   bool    : Post-alvéolaire  
        - palatal       :   bool    : Palatale  
        - velar         :   bool    : Vélaire  
        - uvular        :   bool    : Uvulaire  
        - glottal       :   bool    : Glottale  

    Raises:
        Exception: Si pas exactement 1 parmi stop,fric,liquid,nasal
        Exception: Si pas exactement 1 parmi voiced,unvoiced
        Exception: Si pas exactement 1 parmi labial,dental,alveo,postalveo,palatal,velar,glottal
    """
    
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
                uvular      =False,
                glottal     =False,
                ):

        # Gestion des exceptions
        if(sum([stop,fric,liquid,nasal])!=1):
            raise Exception('Mauvais type stop fric liquid nasal')                
        if(sum([voiced,unvoiced])!=1):
            raise Exception('Mauvais type voiced unvoiced')
        if(sum([labial,dental,alveo,postalveo,palatal,velar,uvular,glottal])!=1):
            raise Exception('Mauvais type labial alveo postalveo palatal velar glottal dental uvular')

        # Attributs d'instances
        self.symbol = symbol

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
        self.uvular = uvular
        self.glottal = glottal

        # Update des attributs de classe
        Consonant.consonants[self.symbol]=self


class Vowel(Sound): 
    """Représente une voyelle

    Class Attributes : 
        - vowels        : dict{str:Vowel}   : Clés = symboles

    Attributes : 
        - symbol        :   str     : Symbole qui représente   

        - front         :   bool    : 
        - central       :   bool    : 
        - back          :   bool    : 

        - close         :   bool    : 
        - semiclose     :   bool    : 
        - open          :   bool    : 


    Raises:
        Exception: Si pas exactement 1 parmi front,central,back
        Exception: Si pas exactement 1 parmi close,open,semiclose
    """

    vowels = {}

    def __init__(
                self,
                symbol      =False,
                front       =False,
                central     =False,
                back        =False, 
                close       =False, 
                semiclose   =False,
                open        =False,
                ):
        
        # Gestion des exceptions
        if(sum([front,central,back])!=1):
            raise Exception('Mauvais type front,central,back')
        
        if(sum([close,open,semiclose])!=1):
            raise Exception('Mauvais type close,open,semiclose')


        # Attributs d'instance
        self.symbol = symbol

        self.front = front
        self.central = central
        self.back = back

        self.close = close
        self.open = open
        self.semiclose = semiclose

        # Attributs de classe
        Vowel.vowels[self.symbol]=self
