"""Ensemble des tests du module
"""

import unittest

from LinguaPythonica.Laspak import (
    Sounds as LaspakSounds,
)

class TestLaspak(unittest.TestCase):
    """Tests unitaires pour LinguaPythonica.Laspak
    """

    def test_00_consonnes(
            self,
    ):
        """Vérifie si toutes les consonnes sont définies
        """
        expected_consonants = ['m', 'p', 'b', 't', 'd', 'f', 'v', 'th', 'n', 's', 'z', 'ch', 'j', 'y', 'r', 'l', 'w', 'k', 'g', 'q', 'x', 'h', "'"]
        for cons_symbol in expected_consonants :
            self.assertIn(
                cons_symbol,
                LaspakSounds.LaspakConsonant.laspak_consonants.keys()
                )
    
    def test_01_voyelles(
            self,
    ):
        """Vérifie si toutes les voyelles sont définies
        """
        expected_vowels = ['a', 'e', 'i', 'o', 'u']
        for vow_symbol in expected_vowels :
            self.assertIn(
                vow_symbol,
                LaspakSounds.LaspakVowel.laspak_vowels.keys()
                )

if __name__ == '__main__':
    unittest.main()