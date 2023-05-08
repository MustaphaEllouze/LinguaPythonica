from abc import ABC,abstractmethod

class Gender(ABC):
    """Représente un genre
    """

    @abstractmethod
    def __init__(self):
        pass

class Person(ABC):
    """Représente le type personne
    """
    def __init__(
            self,
            type_person:int,
    ):
        if type_person not in [1,2,3,4]:
            raise Exception('Mauvaise type de personne')
        
        self.type_person = type_person
