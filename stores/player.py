from typing import Dict
from engine.store import StoreComposite

class PlayerStore(StoreComposite):
    _data: Dict

    def __init__(self, name) -> None:
        super().__init__(name)
        self._data = {
            "name": None,
            "level": 1,
            "characters_name": []
        }

        # Setter registery for the store
        self.add_setter(self.set_data)

        # Getters registery for the store
        self.add_getter(self.get_data)
        self.add_getter(self.have_characters)

    def set_data(self,data: str, value):
        self._data[data] = value

    def get_data(self, data: str) -> Dict:
        try:
            return self._data[data]
        except:
            raise Exception(f"Cannot get data {data}: Data does not exist.")

    def have_characters(self):
        if len(self.get_data("characters_name")) <= 0:
            return False
        return True
