from __future__ import annotations
from abc import ABC, abstractmethod
from engine.core.input_handler import Input
from typing import List
from enums import EngineSceneEnum

class EngineScene:
    """
    Scene context of the GE
    """

    _scene = None
    value = None

    def __init__(cls, scene: Scene) -> None:
        cls.value = scene.name
        cls.mutate(scene)

    def mutate(cls, scene: Scene):
        cls._scene = scene
        cls.value = scene.name
        cls._scene.context = cls

    # Facade for accessing scene value more ealsy
    def get_scene_name(cls) -> EngineSceneEnum:
        return cls.value

    def get_scene(cls) -> Scene:
        return cls._scene

    def get_choice(cls) -> int | str:
        return cls._scene.get_scene_input().get_choice()

class Scene(ABC):

    def __init__(cls) -> None:
        cls._input = cls.build_input()

    # Property

    @property
    def context(cls) -> EngineScene:
        return cls._context

    @context.setter
    def context(cls, context: EngineScene) -> None:
        cls._context = context

    @property
    def name(cls) -> EngineSceneEnum:
        return cls._name

    @name.setter
    def name(cls, name: EngineSceneEnum) -> None:
        cls._name = name

    @name.getter
    def name(cls) -> EngineSceneEnum:
        return cls._name

    # Methods

    @abstractmethod
    def build_input(cls) -> Input:
        pass

    @abstractmethod
    def render_scene(cls) -> None:
        pass

    @abstractmethod
    def get_scene_input(cls) -> Input:
        pass

    @abstractmethod
    def compute(cls) -> None:
        pass

    # Scene State switch

    @abstractmethod
    def create_player(cls) -> None:
        pass

    @abstractmethod
    def train_character(cls) -> None:
        pass

    @abstractmethod
    def fight_character(cls) -> None:
        pass

    @abstractmethod
    def manage_character(cls) -> None:
        pass

    @abstractmethod
    def home(cls) -> None:
        pass

class CreatingCharacterScene(Scene):
    def create_player(cls) -> None:
        raise Exception(f"Already in PlayerCreation scene.")

    def train_character(cls) -> None:
        cls.context.mutate(TrainingScene())

    def fight_character(cls) -> None:
        cls.context.mutate(FightingScene())

    def manage_character(cls) -> None:
        cls.context.mutate(ManagingCharacterScene())

class TrainingScene(Scene):
    def create_player(cls) -> None:
        cls.context.mutate(CreatingCharacterScene())

    def train_character(cls) -> None:
        raise Exception(f"Already in Training scene.")

    def fight_character(cls) -> None:
        cls.context.mutate(FightingScene())

    def manage_character(cls) -> None:
        cls.context.mutate(ManagingCharacterScene())

class FightingScene(Scene):
    def create_player(cls) -> None:
        cls.context.mutate(CreatingCharacterScene())

    def train_character(cls) -> None:
        cls.context.mutate(TrainingScene())

    def fight_character(cls) -> None:
        raise Exception(f"Already in Fighting scene.")

    def manage_character(cls) -> None:
        cls.context.mutate(ManagingCharacterScene())

class ManagingCharacterScene(Scene):
    def create_player(cls) -> None:
        cls.context.mutate(CreatingCharacterScene())

    def train_character(cls) -> None:
        cls.context.mutate(TrainingScene())

    def fight_character(cls) -> None:
        cls.context.mutate(FightingScene())

    def manage_character(cls) -> None:
        raise Exception(f"Already in PlayerCreation scene.")
