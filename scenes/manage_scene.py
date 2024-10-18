import scenes
from stores import CharacterStore
from engine import Engine
from engine.core.input_handler import InputBuilder
from characters._factory.factory import (
    SaiyanCreator,
    NamekiansCreator,
    AndroidsCreator
)

class ManageScene(scenes.Scene):
    def __init__(self) -> None:
        super().__init__()
        self._name = scenes.EngineSceneEnum.PLAYER_CREATION
        self._engine = Engine()

    def build_input(self) -> scenes.Input:
        input_builder = scenes.InputBuilder()
        input_builder.add_title("Chose an action")
        input_builder.add_custom("Home")
        input_builder.add_custom("Train")
        input_builder.add_custom("Fight")
        player_have_characters = self._store.get_component_getter("root/player", ["have_characters"])[0]
        if not player_have_characters():
            input_builder.add_custom("Get your first character", "Create")
        return input_builder.input

    def render_scene(self):
        print(self._store.get_map())

    def get_scene_input(self) -> scenes.Input:
        return self._input

    def compute(self) -> None:
        choice = self._input.get_choice()
        match choice:
            case "Home":
                self.home()
            case "Train":
                self.train_character()
            case "Fight":
                self.fight_character()
            case "Create":
                character_classe_input = InputBuilder()
                character_classe_input.add_title("What type of warrior do you want to create")
                character_classe_input.add_custom("Saiynan", SaiyanCreator())
                character_classe_input.add_custom("Namekian", NamekiansCreator())
                character_classe_input.add_custom("Android", AndroidsCreator())
                classe_choice = self._engine.handle_input(character_classe_input.input)
                character_store = CharacterStore("")
                character_store.create_new_caracter(classe_choice)
                self._store.add_node("root/player", character_store)

    # Scene State switch
    def create_player(self) -> None:
        self._context.mutate(scenes.CreationScene())

    def fight_character(self) -> None:
        self._context.mutate(scenes.FightScene())

    def manage_character(self) -> None:
        raise Exception("Cannot mutate scene: Already in CreationScene.")

    def train_character(self) -> None:
        self._context.mutate(scenes.TrainScene())

    def home(self) -> None:
        self._context.mutate(scenes.HomeScene())