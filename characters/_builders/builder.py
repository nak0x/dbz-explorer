from abc import ABC, abstractmethod
from engine import Engine
from engine.core.input_handler import InputBuilder

class CharacterBuilder(ABC):

    @property
    @abstractmethod
    def character(self):
        pass

    @abstractmethod
    def add_unique_technique(self, technique):
        pass

    @abstractmethod
    def add_transformation(self, transformation):
        pass

    @abstractmethod
    def add_special_item(self, item):
        pass

    @abstractmethod
    def add_name(self, name):
        pass

class CharacterBuilderDirector:
    _engine: Engine

    def __init__(self):
        self._builder = None
        self._engine = Engine()

    @property
    def builder(self):
        return self._builder

    @builder.setter
    def builder(self, builder: CharacterBuilder):
        self._builder =  builder

    def build_character(self, options = {
        "technique": None,
        "transformation": None,
        "items": None,
        "name": None
    }):

        if options["technique"] == None:
            options["technique"] = self.get_technique()
        if options["transformation"] == None:
            options["transformation"] = self.get_transformation()
        if options["items"] == None:
            options["items"] = self.get_special_item()
        if options["name"] == None:
            options["name"] = self.get_name()

        # self._builder.add_unique_technique(options["technique"])
        # self._builder.add_transformation(options["transformation"])
        # self._builder.add_special_item(options["items"])
        self._builder.add_name(options["name"])

        return self._builder.character

    def get_technique(self):
        pass

    def get_transformation(self):
        pass

    def get_special_item(self):
        pass

    def get_name(self):
        input_builder = InputBuilder()
        input_builder.add_title("Chose a name for the character:")
        return self._engine.handle_input(input_builder.input)
