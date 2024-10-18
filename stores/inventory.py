from engine.store import StoreComposite
from characters._inventory import Inventory, Item

class InventoryStore(StoreComposite):

    _data: Inventory = None

    def __init__(self, name, inventory) -> None:
        super().__init__(name)
        print(inventory)
        _data = inventory

        self.add_getter(self.get_item)
        self.add_getter(self.get_inventory)

        self.add_setter(self.add_item)
        self.add_setter(self.remove_item)

    def get_item(self, id):
        self._data.get_item(id)

    def add_item(self, item):
        self._data.add_item(item)

    def remove_item(self, id):
        self._data.remove_item(id)

    def set_inventory(self, inventory: Inventory):
        self._data = inventory

    def get_inventory(self) -> Inventory:
        return self._data