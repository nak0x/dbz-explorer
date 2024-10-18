from engine import Engine
from engine.core.input_handler import (
    InputBuilder,
    InputHandler
)
from engine.scene import Scene
import scenes
from enums import EngineSceneEnum
from stores import CharacterStore
from characters._factory.factory import (
    SaiyanCreator,
    NamekiansCreator,
    AndroidsCreator
)

class ManageScene(Scene):
    def __init__(self) -> None:
        super().__init__()
        self._name = EngineSceneEnum.PLAYER_CREATION
        self._engine = Engine()

    def build_input(self) -> InputHandler:
        input_builder = InputBuilder()
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

    def get_scene_input(self) -> InputHandler:
        return self._input

    def compute(self) -> None:
        choice = self._input.handle_input()
        match choice:
            case "Home":
                self.home()
            case "Train":
                self.train_character()
            case "Fight":
                self.fight_character()
            case "Create":
                classe_input_builder = InputBuilder()
                classe_input_builder.add_title("What type of warrior do you want to create")
                classe_input_builder.add_custom("Saiynan", SaiyanCreator())
                classe_input_builder.add_custom("Namekian", NamekiansCreator())
                classe_input_builder.add_custom("Android", AndroidsCreator())
                classe_input = classe_input_builder.input
                classe_choice = classe_input.handle_input()
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