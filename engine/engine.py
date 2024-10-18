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

    _keep_alive: bool

    def __init__(
            self,
            store: EngineStore,
            scene: EngineScene,
            input_handler: InputHandler
    ) -> None:
        self._scene = scene
        self._store = store
        self._input_handler = input_handler
        self._keep_alive = True

    def run(self) -> None:
        while self._keep_alive:
            # Os compliant cli clearing
            os.system('cls' if os.name == 'nt' else 'clear')
            self._render()
            self.handle_input()
            self._update()
            sleep(0.016)

    def handle_input(self, request: InputHandler = None):
        response = self._scene.get_scene().get_scene_input()
        return response

    def stop(self):
        self._keep_alive = False

    def _update(self) -> None:
        # Run the game logic by calling the per scene compute logic
        # TODO: Implement a command proxy
        if self._scene.get_choice() == "quit":
            self._scene.get_scene().home()

        self._scene.get_scene().compute()

    def _render(self) -> None:
        scene = self._scene.get_scene()
        scene.render_scene()