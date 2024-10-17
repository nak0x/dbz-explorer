import os
import scenes
from stores import PlayerStore

class ManageScene(scenes.Scene):
    def __init__(cls) -> None:
        super().__init__()
        cls._name = scenes.EngineSceneEnum.PLAYER_CREATION
        cls._store = scenes.EngineStore()

    def build_input(cls) -> scenes.Input:
        input_builder = scenes.InputBuilder()
        input_builder.add_title("Chose an action")
        input_builder.add_custom("Home")
        input_builder.add_custom("Train")
        input_builder.add_custom("Fight")
        return input_builder.input

    def render_scene(cls):
        # Os compliant cli clearing
        os.system('cls' if os.name == 'nt' else 'clear')
        print(cls._store.get_map())

    def get_scene_input(cls) -> scenes.Input:
        return cls._input

    def compute(cls) -> None:
        choice = cls._input.get_choice()
        pass

    # Scene State switch
    def create_player(cls) -> None:
        cls._context.mutate(scenes.CreationScene())

    def fight_character(cls) -> None:
        cls._context.mutate(scenes.FightScene())

    def manage_character(cls) -> None:
        raise Exception("Cannot mutate scene: Already in CreationScene.")

    def train_character(cls) -> None:
        cls._context.mutate(scenes.TrainScene())

    def home(cls) -> None:
        cls._context.mutate(scenes.HomeScene())