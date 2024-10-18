import scenes
from stores import PlayerStore

class CreationScene(scenes.Scene):
    def __init__(cls) -> None:
        super().__init__()
        cls._name = scenes.EngineSceneEnum.PLAYER_CREATION

    def build_input(cls) -> scenes.Input:
        input_builder = scenes.InputBuilder()
        input_builder.add_title("chose a player name")
        return input_builder.input

    def render_scene(cls):
        print(cls._store._data.id)
        print(cls._name.value)

    def get_scene_input(cls) -> scenes.Input:
        return cls._input

    def compute(cls) -> None:
        if cls._store.had_player():
            cls.manage_character()
        else:
            choice = cls._input.get_choice()
            player = PlayerStore("player")
            player.set_data("name", choice)
            cls._store.add_node("root", player)
            cls.manage_character()


    # Scene State switch
    def create_player(cls) -> None:
        raise Exception("Cannot mutate scene: Already in CreationScene.")

    def fight_character(cls) -> None:
        cls._context.mutate(scenes.FightScene())

    def manage_character(cls) -> None:
        cls._context.mutate(scenes.ManageScene())

    def train_character(cls) -> None:
        cls._context.mutate(scenes.TrainScene())

    def home(cls) -> None:
        cls._context.mutate(scenes.HomeScene())