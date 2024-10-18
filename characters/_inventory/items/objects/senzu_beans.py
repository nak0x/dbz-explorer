from characters._inventory import Item
from characters import Character

class SenzuBean(Item):
    def use(self, target: Character):
        target.heal(-1)