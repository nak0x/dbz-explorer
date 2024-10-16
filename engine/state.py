from __future__ import annotations
from abc import ABC, abstractmethod
from enum import Enum

class EngineStateEnum(Enum):
    NOT_STARTED = "not_started"
    PLAYER_CREATION = "player_creation"
    TRAINING = "training"
    FIGHTING = "fighting"
    CHARATER_MANAGMENT = "character_managment"

class EngineState:
    """
    State context of the GE
    """

    _state = None
    value = None

    def __init__(cls, state: State) -> None:
        cls.value = state.name
        cls.mutate(state)

    def mutate(cls, state: State):
        cls._state = state
        cls.value = state.name
        cls._state.context = cls

    def get_state(cls) -> EngineStateEnum:
        return cls.value

class State(ABC):
    """
    The base state of the game.
    """

    @property
    def context(cls) -> EngineState:
        return cls._context

    @context.setter
    def context(cls, context: EngineState) -> None:
        cls._context = context

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


class CreatingCharacterState(State):
    def create_player(cls) -> None:
        raise Exception(f"Already in PlayerCreation state.")

    def train_character(cls) -> None:
        cls.context.mutate(TrainingState())

    def fight_character(cls) -> None:
        cls.context.mutate(FightingState())

    def manage_character(cls) -> None:
        cls.context.mutate(ManagingCharacterState())

class TrainingState(State):
    def create_player(cls) -> None:
        cls.context.mutate(CreatingCharacterState())

    def train_character(cls) -> None:
        raise Exception(f"Already in Training state.")

    def fight_character(cls) -> None:
        cls.context.mutate(FightingState())

    def manage_character(cls) -> None:
        cls.context.mutate(ManagingCharacterState())

class FightingState(State):
    def create_player(cls) -> None:
        cls.context.mutate(CreatingCharacterState())

    def train_character(cls) -> None:
        cls.context.mutate(TrainingState())

    def fight_character(cls) -> None:
        raise Exception(f"Already in Fighting state.")

    def manage_character(cls) -> None:
        cls.context.mutate(ManagingCharacterState())

class ManagingCharacterState(State):
    def create_player(cls) -> None:
        cls.context.mutate(CreatingCharacterState())

    def train_character(cls) -> None:
        cls.context.mutate(TrainingState())

    def fight_character(cls) -> None:
        cls.context.mutate(FightingState())

    def manage_character(cls) -> None:
        raise Exception(f"Already in PlayerCreation state.")
