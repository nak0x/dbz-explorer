from engine.store import StoreComposite
from characters import Character
from characters._factory.factory import CharacterCreator
from stores.inventory import InventoryStore

class CharacterStore(StoreComposite):

    _data: Character

    def __init__(self, name) -> None:
        super().__init__(name)

        self.add_setter(self.set_character)
        self.add_getter(self.get_character)

    # Getter/Setters

    def set_character(self, character: Character):
        self._data = character
        self.id = character.get_name()
        for inventory in self._data.get_inventories():
            self.add_inventory(inventory)

    def add_inventory(self, inventory):
        inventory_store = InventoryStore(inventory.name, inventory)
        inventory_store.set_inventory(inventory)
        self.add_node(self._id, inventory_store)

    def get_character(self) -> Character:
        return self._data

    # Logics
    def create_new_caracter(self, character_creator):
        character = character_creator.create_character()
        self.set_character(character)