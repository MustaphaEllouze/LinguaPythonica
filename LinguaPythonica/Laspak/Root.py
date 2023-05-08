from LinguaPythonica.Framework.Words import Root

from LinguaPythonica.Laspak.Sounds import (
    LaspakConsonant,
)

class LaspakRoot(Root):

    # Dictionnaire des racines
    dict_roots = {}
    
    def __init__(
            self,
            letter1: LaspakConsonant,
            letter2: LaspakConsonant,
            letter3: LaspakConsonant,
            translation: str = ''
            ):
        """
        Args:
            letter1 (LaspakConsonant): Première consonne de la racine
            letter2 (LaspakConsonant): Deuxième consonne de la racine
            letter3 (LaspakConsonant): Troisième consonne de la racine
            translation (str, optional): Traduction de la racine. Defaults to ''.
        """
        # Construction
        super().__init__(
            letters=[letter1,letter2,letter3],
            translation=translation,
            )
        
        # Remplissage du dictionnaire
        LaspakRoot.dict_roots[translation]=self