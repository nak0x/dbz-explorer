from abc import ABC, abstractmethod
from characters import Character

class Archetype(Character, ABC):

    @abstractmethod
    def special_technique(self, technique):
        super().special_technique(technique)