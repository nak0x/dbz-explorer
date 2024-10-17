from threading import Lock
from time import sleep

from engine.scene import EngineScene
from engine.core.input_handler import InputHandler
from engine.store import EngineStore

class EngineMeta(type):
    """
    This is a thread-safe implementation of Singleton.
    """

    _instances = {}

    _lock: Lock = Lock()
    """
    We now have a lock object that will be used to synchronize threads during
    first access to the Singleton.
    """

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Engine(metaclass=EngineMeta):
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
            cls._render()
            cls._handle_input()
            cls._update()
            sleep(0.016)

    def _handle_input(cls) -> None:
        request = cls._scene.get_scene().get_scene_input()
        cls._input_handler.handle_input(request)

    def _update(cls) -> None:
        # Run the game logic by calling the per scene compute logic
        # TODO: Implement a command proxy
        if cls._scene.get_choice() == "quit":
            cls._scene.get_scene().home()

        cls._scene.get_scene().compute()

    def _render(cls) -> None:
        scene = cls._scene.get_scene()
        scene.render_scene()