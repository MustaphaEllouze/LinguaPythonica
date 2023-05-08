from LinguaPythonica.Framework.Words import Word

from LinguaPythonica.RedDjinn.concepts_specific import (
    MOODS,
    GEND,
)

class Copula(Word):
    copulae = []
    def __init__(self,
                letters,
                translation=None,
                add_dictionnary=True,
                extend_variations=None,
                ):
        super().__init__(letters, translation=translation+'.COP', add_dictionnary=add_dictionnary,extend_variations=extend_variations)
        self.is_copula = True
        Copula.copulae.append(self)
    
    def mood(self,mood):        
        if(mood not in MOODS.keys()) : raise Exception('Mood non existant')
        
        return Word(self.symbols+MOODS[mood].suffix,
                    translation=self.translation+'.'+mood,
                    add_dictionnary=False,
                    extend_variations=self)
    
    def negate(self):
        return Copula(
            self.symbols+list('nrel'),
            translation=self.translation+'.NEG',
            add_dictionnary=False,
            extend_variations = self,
        )
    
    def manner(self):
        return Copula(
            list('zwit')+self.symbols,
            translation='MANNER.'+self.translation,
            add_dictionnary=False,
            extend_variations = self,
        )


class Pronoun(Word):
    pronouns = []

    def __init__(self,
                letters,
                translation=None,
                add_dictionnary=True,
                person=1,
                plural=False,
                gender=GEND['FEM'],
                tag=''
                ):
        super().__init__(letters, translation, add_dictionnary)
        self.is_pronoun = True
        self.person=person
        self.plural = plural
        self.gender = gender
        self.tag=tag
        Pronoun.pronouns.append(self)

PROUN_list = [
    Pronoun(
        list('mi'),
        translation='Je.FEM',
        person=1,
        plural=False,
        gender=GEND['FEM'],
        tag='1.sg.f',
    ),
    Pronoun(
        list('mie'),
        translation='Je.MASC',
        person=1,
        plural=False,
        gender=GEND['MASC'],
        tag='1.sg.m',
    ),
    Pronoun(
        list('pi'),
        translation='Tu.FEM',
        person=2,
        plural=False,
        gender=GEND['FEM'],
        tag='2.sg.f',
    ),
    Pronoun(
        list('pie'),
        translation='Tu.MASC',
        person=2,
        plural=False,
        gender=GEND['MASC'],
        tag='2.sg.m',
    ),
    Pronoun(
        list('éla'),
        translation='Elle',
        person=3,
        plural=False,
        gender=GEND['FEM'],
        tag='3.sg.f',
    ),
    Pronoun(
        list('élae'),
        translation='Il',
        person=3,
        plural=False,
        gender=GEND['MASC'],
        tag='3.sg.m',
    ),
    Pronoun(
        list('mii'),
        translation='Nous.NEU',
        person=1,
        plural=True,
        gender=GEND['NEU'],
        tag='1.pl.f',
    ),
    Pronoun(
        list('miei'),
        translation='Nous.MASC',
        person=1,
        plural=True,
        gender=GEND['MASC'],
        tag='1.pl.m',
    ),
    Pronoun(
        list('pii'),
        translation='Vous.NEU',
        person=2,
        plural=True,
        gender=GEND['NEU'],
        tag='2.pl.f',
    ),
    Pronoun(
        list('piei'),
        translation='Vous.MASC',
        person=2,
        plural=True,
        gender=GEND['MASC'],
        tag='2.pl.m',
    ),
    Pronoun(
        list('élaé'),
        translation='Elles',
        person=3,
        plural=True,
        gender=GEND['NEU'],
        tag='3.pl.f',
    ),
    Pronoun(
        list('élaei'),
        translation='Ils',
        person=3,
        plural=True,
        gender=GEND['MASC'],
        tag='3.pl.m',
    ),
]

PROUN = {str(pro):pro for pro in PROUN_list}