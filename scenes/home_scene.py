from engine.core.input_handler import (
    InputBuilder,
    Input,
    InputHandler
)
from engine.scene import Scene
import scenes
from enums import EngineSceneEnum

class HomeScene(Scene):
    def __init__(self) -> None:
        super().__init__()
        self._name = EngineSceneEnum.NOT_STARTED

    def build_input(self) -> InputHandler:
        input_builder = InputBuilder()
        input_builder.add_title("Start or quit the game")
        input_builder.add_custom("Start")
        input_builder.add_custom("Quit")
        return input_builder.input

    def render_scene(self):
        print(self._store._data)
        print(self._name.value)

    def get_scene_input(self) -> Input:
        return self._input

    def compute(self) -> None:
        choice = self._input.handle_input()
        if choice == "Quit":
            exit(0)
        elif choice == "Start":
            self.create_player()


    # Scene State switch
    def create_player(self) -> None:
        self._context.mutate(scenes.CreationScene())

    def fight_character(self) -> None:
        self._context.mutate(scenes.FightScene())

    def manage_character(self) -> None:
        self._context.mutate(scenes.ManageScene())

    def train_character(self) -> None:
        self._context.mutate(scenes.TrainScene())

    def home(self) -> None:
        # Handle the case where we call the quit command on the home
        if self._input.handle_input() == "Quit":
            exit(0)
        raise Exception("Cannot mutate: Already at HomeScene.")