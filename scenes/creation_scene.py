from engine.core.input_handler import (
    InputBuilder,
    InputHandler
)
from engine.scene import Scene
import scenes
from enums import EngineSceneEnum
from stores import PlayerStore

class CreationScene(Scene):
    def __init__(self) -> None:
        super().__init__()
        self._name = EngineSceneEnum.PLAYER_CREATION

    def build_input(self) -> InputHandler:
        input_builder = InputBuilder()
        input_builder.add_title("chose a player name")
        return input_builder.input

    def render_scene(self):
        print(self._store._data.id)
        print(self._name.value)

    def get_scene_input(self) -> InputHandler:
        return self._input

    def compute(self) -> None:
        if self._store.had_player():
            self.manage_character()
        else:
            choice = self._input.handle_input()
            player = PlayerStore("player")
            player.set_data("name", choice)
            self._store.add_node("root", player)
            self.manage_character()


    # Scene State switch
    def create_player(self) -> None:
        raise Exception("Cannot mutate scene: Already in CreationScene.")

    def fight_character(self) -> None:
        self._context.mutate(scenes.FightScene())

    def manage_character(self) -> None:
        self._context.mutate(scenes.ManageScene())

    def train_character(self) -> None:
        self._context.mutate(scenes.TrainScene())

    def home(self) -> None:
        self._context.mutate(scenes.HomeScene())