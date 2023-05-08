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
                symbol      :str,
                stop        :bool=False,
                fric        :bool=False,
                liquid      :bool=False,
                nasal       :bool=False,
                voiced      :bool=False,
                unvoiced    :bool=False,
                labial      :bool=False,
                dental      :bool=False,
                alveo       :bool=False,
                postalveo   :bool=False,
                palatal     :bool=False,
                velar       :bool=False,
                uvular      :bool=False,
                glottal     :bool=False,
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
        Consonant.consonants[self.symbol.upper()]=self


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
                symbol      :str,
                front       :bool=False,
                central     :bool=False,
                back        :bool=False, 
                close       :bool=False, 
                semiclose   :bool=False,
                open        :bool=False,
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
        Vowel.vowels[self.symbol.upper()]=self
