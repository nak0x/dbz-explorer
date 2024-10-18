from abc import ABC, abstractmethod

from characters import Character
from characters._builders.builder import CharacterBuilderDirector, CharacterBuilder
from characters._builders.character_builders import (
    SaiyanBuilder,
    NamekianBuilder,
    AndroidBuilder
)

class CharacterCreator(ABC):

    @abstractmethod
    def create_character_builder(self) -> CharacterBuilder:
        pass

    def create_character(self) -> Character:
        # Call the factory method to create a Product object.
        builder_director = CharacterBuilderDirector()
        builder = self.create_character_builder()
        builder_director.builder = builder
        builder_director.build_character()
        return builder_director.builder.character


class SaiyanCreator(CharacterCreator):
    def create_character_builder(self) -> Character:
        return SaiyanBuilder()

class NamekiansCreator(CharacterCreator):
    def create_character_builder(self) -> Character:
        return NamekianBuilder()

class AndroidsCreator(CharacterCreator):
    def create_character_builder(self) -> Character:
        return AndroidBuilder()
