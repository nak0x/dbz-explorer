from abc import ABC, abstractmethod
from typing import Dict, Any
from time import sleep

from engine.core import GenericObserver, GenericSubject

class Input(GenericSubject):
    _choice: Any | None = None
    _available_choice: list = []
    _options: list[Dict] = []
    _title: str = ""

    def __init__(self) -> None:
        self._options = []
        self._available_choice = []
        self._choice = None

    @property
    def choice(self):
        return self._choice

    @choice.setter
    def choice(self, value):
        self._choice = value
        self.notify()

    # Subject
    def notify(self) -> None:
        for observer in self._observers.values():
            observer.update(self)

    def attach(self, observer: GenericObserver) -> None:
        self._observers[observer._id] = observer
        self.start()

    def detach(self, id) -> None:
        return super().detach(id)

    # InputBuilder
    def add_title(self, title: str):
        self._title = title

    def add_option(self, name: str, value=None) -> None:
        if value == None:
            value = name
        self._options.append({"name": name, "value": value, "id": len(self._options) + 1})
        self._available_choice.append(len(self._options))
        self._available_choice.append(value)

    # Logiques
    def start(self):
        while not self.is_valide():
            self.execute_input()
            choice = self.get_choice()
            self.set_choice(choice)
            # update at 60ups
            sleep(0.016)
        self.notify()

    def execute_input(self):
        row_input = input(f"{self.get_options_str()} ~> ")
        try:
           choice = int(row_input)
        except ValueError:
            choice = row_input
        self.set_choice(choice)

    def get_options_str(self) -> str:
        options_str = f"{self._title}\n"
        for key, value in enumerate(self._options):
            options_str += f"[{key+1}] {value['name']} "
        return options_str

    def set_choice(self, choice: int) -> None:
        self._choice = choice

    def get_choice(self) -> int | str:
        try:
            for value in self._options:
                if self._choice == value["name"] or self._choice == value["id"]:
                    return value["value"]
            return self._choice
        except:
            return None

    def is_valide(self) -> bool:
        if self._choice:
            choice = self._choice
            if choice in self._available_choice:
                return True
            elif len(self._available_choice) <= 0 and choice != None:
                return True
        return False


class InputBuilderMeta(ABC):
    @property
    @abstractmethod
    def input(self) -> None:
        pass

    @abstractmethod
    def add_validation(self) -> None:
        pass

    @abstractmethod
    def add_custom(self, custom: str) -> None:
        pass

    @abstractmethod
    def add_title(self, title: str) -> None:
        pass

class InputBuilder(InputBuilderMeta):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._input = Input()

    @property
    def input(self) -> Input:
        input_handler = InputHandler()
        input_handler.hold_input(self._input)
        return input_handler

    def add_validation(self) -> None:
        self._input.add_option("Yes")
        self._input.add_option("No")

    def add_custom(self, name, value=None) -> None:
        self._input.add_option(name, value)

    def add_title(self, title: str) -> None:
        self._input.add_title(title)


class InputHandler(GenericObserver):
    _history: list[Input]
    _is_running: bool
    _on_hold: Input

    def __init__(self) -> None:
        self._history = []
        self._is_running = False
        self._on_hold = None
        pass

    def start(self):
        self._is_running = True

    def stop(self):
        self._is_running = False

    def update(self, subject: GenericSubject):
        self._history.append(subject)
        self.stop()

    def hold_input(self, request: Input):
        self._on_hold = request

    def handle_input(self):
        self.start()
        self._on_hold.attach(self)
        while self._is_running:
            print("test")
            sleep(0.016)
        response = self.get_last_input()
        return response.get_choice()

    def get_last_input(self) -> Input:
        if len(self._history) > 0:
            return self._history[-1]
        else:
            return self._on_hold