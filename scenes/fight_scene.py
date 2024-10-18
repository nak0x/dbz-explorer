from engine.core.input_handler import (
    InputBuilder,
    InputHandler
)
from engine.scene import Scene
import scenes
from enums import EngineSceneEnum

class FightScene(Scene):

    def render_scene(cls):
        return super().render_scene()

    def get_scene_input(cls) -> InputHandler:
        return super().get_scene_input()

    # Scene State switch
    def create_player(cls) -> None:
        raise Exception("Already in CreatePlayerScene.")

    def fight_character(cls) -> None:
        cls._context.mutate(scenes.FightScene())

    def manage_character(cls) -> None:
        cls._context.mutate(scenes.ManageScene())

    def train_character(cls) -> None:
        cls._context.mutate(scenes.TrainScene())

    def home(cls) -> None:
        cls._context.mutate(scenes.HomeScene())