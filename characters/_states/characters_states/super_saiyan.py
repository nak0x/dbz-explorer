from abc import ABC, abstractmethod

from characters._states.state import CharacterState

class SuperSaiyanLevel(ABC):

    _base_endurance: int
    _level_name: str

    @property
    def super_saiyan(self):
        return self._super_saiyan

    @super_saiyan.setter
    def super_saiyan(self, super_saiyan):
        self._super_saiyan = super_saiyan

    def get_endurance(self):
        return self._base_endurance

    def get_level_name(self):
        return self._level_name


class SuperSaiyan(CharacterState):

    _default_endurance = 200
    _default_life = 2000
    _level: SuperSaiyanLevel
    available_classes = ["saiyan"]

    def get_endurance_ratio(self, impact=0):
        return (self._character._endurance / self._default_endurance) + impact

    def get_endurance(self):
        return self._level._base_endurance

    def get_life(self):
        return self._level._base_life

    def deal_damages(self, target):
        damages = self._character._strength * self.get_endurance_ratio()
        target.take_damages(damages)

    def take_damages(self, amount):
        self._character._life -= amount * self.get_endurance_ratio(1)
        self._character._endurance -= amount * self.get_endurance_ratio()


class Saiyan1(SuperSaiyanLevel):
    _base_endurance = 100
    _level_name = "Super Saiyan 1"
    _base_life = 1000


class Saiyan2(SuperSaiyanLevel):
    _base_endurance = 200
    _level_name = "Super Saiyan 2"
    _base_life = 2000


class Saiyan3(SuperSaiyanLevel):
    _base_endurance = 300
    _level_name = "Super Saiyan 3"
    _base_life = 4000


class SuperSaiyanGod(SuperSaiyanLevel):
    _base_endurance = 500
    _level_name = "Super Saiyan Divin"
    _base_life = 7000


class SuperSaiyanBlue(SuperSaiyanLevel):
    _base_endurance = 1000
    _level_name = "Super Saiyan Blue"
    _base_life = 10000