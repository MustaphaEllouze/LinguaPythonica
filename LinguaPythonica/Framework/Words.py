from __future__ import annotations

from abc import (
    ABC,
    abstractmethod,
)

from collections import defaultdict

from LinguaPythonica.Framework.Sounds import Sound

class Word(ABC):
    """Représente un mot. Classe abstraite.

    Class Attributes : 
        - dict_words        : dict{str:Word}         : Clés = symboles
        - translations      : dict{str:list[Word]}   : Clés = traductions

    Attributes : 
        - letters           :   list[Sound]     : Liste des lettres qui composent le mot
        - translation       :   str             : Traduction du mot
        - symbols           :   list[str]       : Liste des symboles qui forment le mot
        - variations        :   list[Word]      : Liste de variations des mots

    """

    # Dictionnaire des mots
    dict_words = {}     # Clés = Str ; Value = self 

    # Dictionnaire : str(traduction) --> self
    translations = defaultdict(list)

    def __init__(
                self,
                letters                 :list[Sound],
                translation             :str        =   '',
                add_dictionnary         :bool       =   True,
                extend_variations       :Word       =   None,
            ):
        """
        Args:
            letters (list[str]): Lettres qui composent le mot
            translation (str, optional): Traduction du mot. Defaults to None.
            add_dictionnary (bool, optional): True si le mot doit être . Defaults to True.
            extend_variations (Word, optional): Le mot dont la nouvelle instance est un dérivé, add_dictionnary doti valoir True. Defaults to None.
            check_rules (bool, optional): True s'il faut checker la morphosyntaxique. Defaults to True.
        """
        
        # --- Lettres du mots
        self.letters = letters

        # --- Traduction
        self.translation = translation

        # Symboles de chaque lettre du mot
        self.symbols = [let.symbol for let in self.letters]

        # S'il faut ajouter au dictionnaire
        if(add_dictionnary) : 
            Word.words[str(self)]=self
            self.variations = [self]

            # Si le mot est une variation    
            if(not extend_variations is None):
                extend_variations.variations.append(self)
        else:
            self.variations = None
        
        # Ajout dans le dictionnaire de traduction
        Word.translations[translation].append(self)
    
    def __str__(self)->str:
        res = ''
        for s in [let.symbol for let in self.letters] : res += s
        return res

    def get_word_from_translation(translation)->Word:
        """Renvoie un mot à partir d'une traduction

        Args:
            translation (str): Mot dont on veut avoir la traduction

        Returns:
            Word: Mot traduit ; renvoie None si traduction pas trouvée
        """
        if translation in Word.translations.keys():
            return Word.translations[translation][0]
        else:
            return None

    @abstractmethod
    def plural(self):
        """Renvoie le pluriel du mot
        """
        pass

    @abstractmethod
    def substantive(self):
        """Renvoie le substantif du mot
        """
        pass

    @abstractmethod
    def check_rules(self):
        """Vérifie que les mots obéissent à la morphosyntaxique
        """
        pass
            

class Verb(Word,ABC):
    """Représente un verbe, classe abstraite"""

    # Dictionnaire des mots
    dict_verbs = {}     # Clés = Str ; Value = self 

    def __init__(self,
                letters             :       list[str]        ,
                translation         :       str         =  '',
                add_dictionnary     :       bool        =True,
                extend_variations   :       Word        =None,
                check_rules         :       bool        =True,
                ):
        """
        Args:
            letters (list[str]): Lettres qui composent le mot
            translation (str, optional): Traduction du mot. Defaults to None.
            add_dictionnary (bool, optional): True si le mot doit être . Defaults to True.
            extend_variations (Word, optional): Le mot dont la nouvelle instance est un dérivé, add_dictionnary doti valoir True. Defaults to None.
            check_rules (bool, optional): True s'il faut checker la morphosyntaxique. Defaults to True.
        """
        super().__init__(
            letters=letters,
            translation=translation,
            add_dictionnary=add_dictionnary,
            extend_variations=extend_variations,
            check_rules=check_rules,
        )
    
    @abstractmethod
    def conjugate(
        self,
        ):
        pass