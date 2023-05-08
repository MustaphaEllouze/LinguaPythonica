from LinguaPythonica.Framework.Words import Root

from LinguaPythonica.Laspak.Assembling.sounds_inventory import (
    LASPAK_CONSONANTS_DICT,
    LASPAK_VOWELS_DICT,
)

class LaspakRoot(Root):

    # Dictionnaire des racines
    dict_roots = {}
    
    def __init__(
            self,
            letter1: str,
            letter2: str,
            letter3: str,
            translation: str = ''
            ):
        """
        Args:
            letter1 (str): Première consonne de la racine
            letter2 (str): Deuxième consonne de la racine
            letter3 (str): Troisième consonne de la racine
            translation (str, optional): Traduction de la racine. Defaults to ''.
        """

        if self.check_rules(letter1=letter1,letter2=letter2,letter3=letter3):
            pass
        else:
            raise Exception(f"Les lettres choisies pour la racine sont fausses : {(letter1,letter2,letter3)}")

        # Construction
        super().__init__(
            letters=[
                LASPAK_CONSONANTS_DICT[letter1],
                LASPAK_CONSONANTS_DICT[letter2],
                LASPAK_CONSONANTS_DICT[letter3],
                ],
            translation=translation,
            )
        
        # Remplissage du dictionnaire
        LaspakRoot.dict_roots[translation]=self
    
    def check_rules(
            self,
            letter1:str,
            letter2:str,
            letter3:str,
    ):
        """Checker de racine valide. On vérifie que les lettres passées sont des consonnes définies.
        """
        return (set([letter1,letter2,letter3]).issubset(set(LASPAK_CONSONANTS_DICT.keys())))

    def __str__(self) -> str:
        """Racine --> Majuscule"""
        return super().__str__().upper()
    