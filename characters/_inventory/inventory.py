from abc import ABC, abstractmethod
from uuid import uuid4
from typing import Dict

class Item(ABC):

    def __init__(self, inventory, name) -> None:
        self.id = uuid4()
        self._datas = {
            "name": name,
        }
        self._inventory = inventory
        self._inventory.add_item(self)

    def set_data(self, data, value):
        self._datas[data] = value

    def get_data(self, data):
        try:
            return self._datas[data]
        except:
            raise Exception(f"Cannot get data {data}: Data not defined")

    def define_item(self, infos: Dict):
        for type, value in infos.items():
            self.set_data(type, value)

    @abstractmethod
    def use(self, target):
        self._inventory.remove_item(self.id)
        pass

class Inventory:

    def __init__(self, name) -> None:
        self._items = {}
        self.name = name

    def add_item(self, item: Item):
        self._items[item.id] = item

    def get_item(self, id):
        return self._items[id]

    def remove_item(self, id):
        try:
            del self._items[id]
        except:
            # Do nothing if the item is not found
            pass
