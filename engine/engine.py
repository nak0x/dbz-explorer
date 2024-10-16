from threading import Lock
from engine.state import (
    EngineState,
)
from engine.core.input_handler import (
    InputHandler,
    InputBuilder
)
from engine.store import EngineStore
from time import sleep

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
    _state: EngineState
    _store: EngineStore
    _renderer: EngineRenderer
    _input_handler: InputHandler

    _interupt: bool

    def __init__(cls, store: EngineStore, state: EngineState, input_handler: InputHandler) -> None:
        cls._state = state
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
        cls._input_handler.handle_input(state=cls._state,store=cls._store)

    def _update(cls) -> None:
        # Run the game logic
        pass

    def _render(cls) -> None:
        # Render the game view
        pass