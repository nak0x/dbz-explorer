from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
from enums import EngineSceneEnum

from engine.core.input_handler import InputHandler
from engine.store import EngineStore

class EngineScene:
    """
    Scene context of the GE
    """

    _scene = None
    value = None

    def __init__(self, scene: Scene) -> None:
        self.value = scene.name
        self.mutate(scene)

    def mutate(self, scene: Scene):
        self._scene = scene
        self.value = scene.name
        self._scene.context = self

    # Facade for accessing scene value more ealsy
    def get_scene_name(self) -> EngineSceneEnum:
        return self.value

    def get_scene(self) -> Scene:
        return self._scene

    def get_choice(self) -> int | str:
        return self._scene.get_scene_input().get_last_input().get_choice()

class Scene(ABC):

    def __init__(self) -> None:
        self._store = EngineStore()
        self._input = self.build_input()

    # Property

    @property
    def context(self) -> EngineScene:
        return self._context

    @context.setter
    def context(self, context: EngineScene) -> None:
        self._context = context

    @property
    def name(self) -> EngineSceneEnum:
        return self._name

    @name.setter
    def name(self, name: EngineSceneEnum) -> None:
        self._name = name

    @name.getter
    def name(self) -> EngineSceneEnum:
        return self._name

    # Methods

    @abstractmethod
    def build_input(self) -> InputHandler:
        pass

    @abstractmethod
    def render_scene(self) -> None:
        pass

    @abstractmethod
    def get_scene_input(self) -> InputHandler:
        pass

    @abstractmethod
    def compute(self) -> None:
        pass

    # Scene State switch

    @abstractmethod
    def create_player(self) -> None:
        pass

    @abstractmethod
    def train_character(self) -> None:
        pass

    @abstractmethod
    def fight_character(self) -> None:
        pass

    @abstractmethod
    def manage_character(self) -> None:
        pass

    @abstractmethod
    def home(self) -> None:
        pass
