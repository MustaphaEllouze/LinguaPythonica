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
        expected_consonants = []
        for cons_symbol in expected_consonants :
            self.assertIn(cons_symbol,LaspakSounds.CONS.keys())
    
    def test_01_voyelles(
            self,
    ):
        """Vérifie si toutes les voyelles sont définies
        """
        expected_vowels = []
        for vow_symbol in expected_vowels :
            self.assertIn(vow_symbol,LaspakSounds.VOWE.keys())

if __name__ == '__main__':
    unittest.main()