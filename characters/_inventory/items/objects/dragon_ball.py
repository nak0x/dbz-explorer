from characters._inventory import Item
from characters import Character

class DragonBall(Item):
    def use(self, target: Character):
        # Extreme x100 buff
        target.buff(100)