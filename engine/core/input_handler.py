from abc import ABC, abstractmethod

from engine.store import EngineStore
from enums import EngineSceneEnum

class Input:
    _choice: int | str
    _options: list[str]
    _title: str

    def __init__(cls) -> None:
        cls._options = []

    def add_title(cls, title: str):
        cls._title = title

    def add_option(cls, option: str) -> None:
        cls._options.append(option)

    def get_options_str(cls) -> str:
        options_str = f"{cls._title}\n"
        for key, value in enumerate(cls._options):
            options_str += f"[{key}] {value} "
        return options_str

    def set_choice(cls, choice: int) -> None:
        cls._choice = choice

    def get_choice(cls) -> int | str:
        try:
            return cls._choice
        except:
            return None


class InputBuilderMeta(ABC):
    @property
    @abstractmethod
    def input(cls) -> None:
        pass

    @abstractmethod
    def add_validation(cls) -> None:
        pass

    @abstractmethod
    def add_custom(cls, custom: str) -> None:
        pass

    @abstractmethod
    def add_title(cls, title: str) -> None:
        pass

class InputBuilder(InputBuilderMeta):

    def __init__(cls) -> None:
        cls.reset()

    def reset(cls) -> None:
        cls._input = Input()

    @property
    def input(cls) -> Input:
        return cls._input

    def add_validation(cls) -> None:
        cls._input.add_option("Yes")
        cls._input.add_option("No")

    def add_custom(cls, custom: str) -> None:
        cls._input.add_option(custom)

    def add_title(cls, title: str) -> None:
        cls._input.add_title(title)


class InputHandler:
    _history: list[Input]

    def __init__(cls) -> None:
        cls._history = []
        pass

    def handle_input(cls, request: Input) -> Input:
        choice = cls.execute_input(request)
        # If choice === "quit" -> notify to quit the game
        request.set_choice(choice)
        cls._history.append(request)
        return request

    def execute_input(cls, request: Input) -> Input:
        row_input = input(f"{request.get_options_str()} ~> ")
        try:
           choice = int(row_input)
        except ValueError:
            choice = row_input
        return choice

    def get_last_input(cls) -> Input:
        return cls._history[-1]