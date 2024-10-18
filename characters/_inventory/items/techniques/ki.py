from characters._inventory import Item
from characters import Character

class KiAttack(Item):

    def __init__(self, name, inventory, damages) -> None:
        super().__init__(inventory, name)
        self.set_data("damages", damages)

    def use(self, target: Character):
        target.take_damages(self.get_data("damages"))