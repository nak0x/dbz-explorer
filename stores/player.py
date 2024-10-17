from typing import Dict
from engine.store import StoreComposite

class PlayerStore(StoreComposite):
    _player_data: Dict

    def __init__(cls) -> None:
        super().__init__()
        cls._player_data = {
            "name": None,
            "level": 1,
            "inventory": {}
        }

        # Setter registery for the store
        cls.add_setter(cls.exist)
        cls.add_setter(cls.set_data)

        # Getters registery for the store
        cls.add_getters(cls.get_data)

    def set_data(cls,data: str, value):
        cls._player_data[data] = value

    def get_data(cls) -> Dict:
        return cls._player_data

    def exist(cls) -> bool:
        return True
