from characters._states.state import CharacterState

class DefaultState(CharacterState):

    _default_endurance = 50
    _default_life = 1000
    available_classes = ["all"]

    def get_endurance_ratio(self, impact=0):
        return (self._character._endurance / self._default_endurance) + impact

    def deal_damages(self, target):
        damages = self._character._strength * self.get_endurance_ratio()
        target.take_damages(damages)

    def take_damages(self, amount):
        self._character._life -= amount * self.get_endurance_ratio(1)
        self._character._endurance -= amount * self.get_endurance_ratio()