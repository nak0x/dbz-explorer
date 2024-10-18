from abc import ABC, abstractmethod
from typing import Dict
from time import sleep

from engine.store import EngineStore
from enums import EngineSceneEnum

class Input:
    _choice: int | str
    _available_choice: list
    _options: list[Dict]
    _title: str

    def __init__(cls) -> None:
        cls._options = []
        cls._available_choice = []
        cls._choice = None

    def add_title(cls, title: str):
        cls._title = title

    def add_option(cls, name: str, value=None) -> None:
        if value == None:
            value = name
        cls._options.append({"name": name, "value": value, "id": len(cls._options) + 1})
        cls._available_choice.append(len(cls._options))
        cls._available_choice.append(value)

    def get_options_str(cls) -> str:
        options_str = f"{cls._title}\n"
        for key, value in enumerate(cls._options):
            options_str += f"[{key+1}] {value['name']} "
        return options_str

    def set_choice(cls, choice: int) -> None:
        cls._choice = choice

    def get_choice(cls) -> int | str:
        try:
            for value in cls._options:
                if cls._choice == value["name"] or cls._choice == value["id"]:
                    return value["value"]
            return cls._choice
        except:
            return None

    def is_valide(cls) -> bool:
        if cls._choice in cls._available_choice:
            return True
        elif len(cls._available_choice) <= 0 and cls._choice != None:
            return True
        return False


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

    def add_custom(cls, name, value=None) -> None:
        cls._input.add_option(name, value)

    def add_title(cls, title: str) -> None:
        cls._input.add_title(title)


class InputHandler:
    _history: list[Input]

    def __init__(cls) -> None:
        cls._history = []
        pass

    def handle_input(cls, request: Input) -> Input:
        while not request.is_valide():
            choice = cls.execute_input(request)
            request.set_choice(choice)
            sleep(0.02)

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