import os
import scenes

class HomeScene(scenes.Scene):
    def __init__(cls) -> None:
        super().__init__()
        cls._name = scenes.EngineSceneEnum.NOT_STARTED
        cls._store = scenes.EngineStore()

    def build_input(cls) -> scenes.Input:
        input_builder = scenes.InputBuilder()
        input_builder.add_title("Start or quit the game")
        input_builder.add_custom("Start")
        input_builder.add_custom("Quit")
        return input_builder.input

    def render_scene(cls):
        # Os compliant cli clearing
        os.system('cls' if os.name == 'nt' else 'clear')
        print(cls._store._data)
        print(cls._name.value)

    def get_scene_input(cls) -> scenes.Input:
        return cls._input

    def compute(cls) -> None:
        choice = cls._input.get_choice()
        if choice in ["quit", 1]:
            exit(0)
        elif choice == 0:
            cls.create_player()


    # Scene State switch
    def create_player(cls) -> None:
        cls._context.mutate(scenes.CreationScene())

    def fight_character(cls) -> None:
        cls._context.mutate(scenes.FightScene())

    def manage_character(cls) -> None:
        cls._context.mutate(scenes.ManageScene())

    def train_character(cls) -> None:
        cls._context.mutate(scenes.TrainScene())

    def home(cls) -> None:
        # Handle the case where we call the quit command on the home
        if cls._input.get_choice() == "quit":
            exit(0)
        raise Exception("Cannot mutate: Already at HomeScene.")