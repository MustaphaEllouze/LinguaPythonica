from sounds import (
    CONS_list,
    VOWE_list,
)

from words_class import (
    Word,
    Verb,
)

from words_class_specific import (
    Copula,
    PROUN,
)

WORDS = [
    Word(
        ['th','n','a','y'],
        translation='Femme',
    ),
    Word(
        list('tfé\''),
        translation='Pomme'
    ),
    Word(
        list('mren'),
        translation='Création'
    ),
    Word(
        list('zwit'),
        translation='Manière'
    ),
    Word(
        list('mro')+['ch'],
        translation='Rougeur'
    ),
    Word(
        list('flut'),
        translation='TBD'
    ),
    Verb(
        list('ménal'),
        translation='Manger',
    ),
    Verb(
        list('dérar'),
        translation='Brûler',
    ),
    Copula(
        list('\'éam'),
        translation='Joie'
    ),
    Copula(
        list('tair'),
        translation='Surprise'
    ),
    Copula(
        list('seid'),
        translation='Tristesse'
    ),
    Copula(
        list('mués'),
        translation='Peur'
    ),
    Copula(
        list('diég'),
        translation='Dégoût'
    ),
    Copula(
        list('guar'),
        translation='Colère'
    ),
    Copula(
        list('loes'),
        translation='Envie'
    ),
    Copula(
        list('féin'),
        translation='Fierté'
    ),
    Copula(
        list('ma\''),
        translation='Neutralité'
    ),
    Word(
        ['i','th'],
        translation='La'
    ),
    Word(
        ['ch','o','s'],
        translation='Fait'
    ),
    Word(
        list('nrel'),
        translation='Négation'
    ),
    Word(
        list('prak'),
        translation='Application'
    ),
    Word(
        list('pfoe'),
        translation='Chose'
    ),
    Word(
        list('kral'),
        translation='Qualité (qui qualifie)'
    )
    
]

WORDS += [PROUN[pro] for pro in PROUN.keys()]