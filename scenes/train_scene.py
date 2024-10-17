import scenes

class TrainScene(scenes.Scene):

    def render_scene(cls):
        return super().render_scene()

    def get_scene_input(cls) -> scenes.Input:
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