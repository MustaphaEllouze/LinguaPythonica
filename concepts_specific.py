class Mood:
    
    moods = []
    
    def __init__(self,
                name,
                suffix,
                ) :
        self.name=name
        self.suffix=suffix
        Mood.moods.append(self)

class Gender:

    def __init__(self,
                name):
        self.name = name
    
GEND = {'FEM':Gender('FEM'),'MASC':Gender('MASC'),'NEU':Gender('NEU')}

MOODS_list = [
    
        Mood(
            name='IND',
            suffix = [],
        ),
        Mood(
            name='HAB',
            suffix = ['k','i'],
        ),
        Mood(
            name='COND',
            suffix = ['th','a'],
        ),
        Mood(
            name='SUBJ',
            suffix = ['s','e'],
        ),
        Mood(
            name='OPT',
            suffix = ['ch','o'],
        ),
        Mood(
            name='POT',
            suffix = ['r','é'],
        ),
]

MOODS = {mood.name:mood for mood in MOODS_list}