from time import sleep
import os

from engine.core import ThreadSafeSingletonMeta
from engine.scene import EngineScene
from engine.core.input_handler import InputHandler, Input
from engine.store import EngineStore

class Engine(metaclass=ThreadSafeSingletonMeta):
    _scene: EngineScene
    _store: EngineStore
    _input_handler: InputHandler

    _interupt: bool

    def __init__(
            cls,
            store: EngineStore,
            scene: EngineScene,
            input_handler: InputHandler
    ) -> None:
        cls._scene = scene
        cls._store = store
        cls._input_handler = input_handler
        cls._interupt = True

    def run(cls) -> None:
        while cls._interupt:
            # Os compliant cli clearing
            os.system('cls' if os.name == 'nt' else 'clear')
            cls._render()
            cls.handle_input()
            cls._update()
            sleep(0.016)

    def handle_input(cls, request: Input = None):
        if request == None:
            request = cls._scene.get_scene().get_scene_input()
        cls._input_handler.handle_input(request)
        return request.get_choice()

    def _update(cls) -> None:
        # Run the game logic by calling the per scene compute logic
        # TODO: Implement a command proxy
        if cls._scene.get_choice() == "quit":
            cls._scene.get_scene().home()

        cls._scene.get_scene().compute()

    def _render(cls) -> None:
        scene = cls._scene.get_scene()
        scene.render_scene()