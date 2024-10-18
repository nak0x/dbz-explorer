from characters._builders.builder import CharacterBuilder
from characters._factory.archetype.namekian import Namekian

class NamekianBuilder(CharacterBuilder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._character = Namekian()

    @property
    def character(self) -> Namekian:
        character = self._character
        self.reset()
        return character

    def add_unique_technique(self, technique):
        if "namekian" in technique.available_classes or "all" in technique.available_classes:
            self._character.add_technique(technique)
        else:
            raise Exception(f"Cannot add technique {technique.name}: Not supported by classes namekian.")

    def add_transformation(self, transformation):
        if "namekian" in transformation.available_classes or "all" in transformation.available_classes:
            self._character.add_transformation(transformation)
        else:
            raise Exception(f"Cannot add transformation {transformation.name}: Not supported by classes namekian.")

    def add_special_item(self, item):
        self._character.add_item(item)

    def add_name(self, name):
        self._character.add_name(name)