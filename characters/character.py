from abc import abstractmethod
from typing import Self

from characters._states.state import CharacterState
from characters._states.characters_states import DefaultState
from characters._inventory import Inventory

class Character:

    # 0 - 10,000
    _life = 1000

    # 0 - 500
    _strength = 50
    _endurance = 50
    _speed = 50

    # data
    _objects_inventory: Inventory
    _techniques_inventory: Inventory
    _transformations_inventory: Inventory

    _state: CharacterState
    _classe: str

    _name: str

    def __init__(self):
        self.transition_to(DefaultState())
        self._objects_inventory = Inventory("objects_inventory")
        self._techniques_inventory = Inventory("techniques_inventory")
        self._transformations_inventory = Inventory("transformations_inventory")
        self._name = ""

    def get_inventories(self)-> Inventory:
        return [
            self._objects_inventory,
            self._techniques_inventory,
            self._transformations_inventory
        ]

    def get_name(self):
        return self._name

    def take_damages(self, amount):
        self._state.take_damages(amount)

    def heal(self, amount):
        self._state.heal(amount)

    def deal_damages(self, target: Self):
        self._state.deal_damages(target)

    def buff(self, factor):
        self._strength *= factor
        self._endurance *= factor
        self._speed *= factor

    def pick_item(self, item):
        self._inventory.add_item(item)

    def use_item(self, item):
        self._inventory.use_item(item)

    def special_technique(self, technique):
        self._actions.performe_special(technique)

    def transition_to(self, state: CharacterState):
        if self._classe in state.available_classes or "all" in state.available_classes:
            self._state = state
            self._state.character = self
        else:
            raise Exception(f"Cannot transition to {state.__class__}: State not applicable to {self._classe}")

    # Builders methods
    def add_technique(self, technique):
        # use the _action
        print(technique)

    def add_transformation(self, tranformation):
        print(tranformation)

    def add_item(self, item):
        print(item)

    def add_name(self, name):
        self._name = name