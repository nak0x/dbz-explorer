from abc import ABC, abstractmethod

class CharacterState(ABC):

    _default_endurance = 50
    _default_life = 1000
    available_classes = ["all"]

    @property
    def character(self):
        return self._character

    @character.setter
    def character(self, character):
        self._character = character

    @abstractmethod
    def deal_damages(self):
        pass

    @abstractmethod
    def take_damages(self, amount):
        pass

    def get_endurance(self):
        return self._default_endurance

    def get_life(self):
        return self._default_life