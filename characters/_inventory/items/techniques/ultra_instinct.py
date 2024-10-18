from characters._inventory import Item
from characters import Character

class UltraInstinct(Item):

    def use(self, target: Character):
        target.buff(1.33)