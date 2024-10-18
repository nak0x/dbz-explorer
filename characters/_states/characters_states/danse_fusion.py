from characters._states.state import CharacterState

class FusionDanceState(CharacterState):

    _default_endurance = 500  # Très grande endurance obtenue par fusion
    _default_life = 8000
    available_classes = ["all"]

    def get_endurance_ratio(self, impact=0):
        return (self._character._endurance / self._default_endurance) + impact

    def deal_damages(self, target):
        # Dégâts énormes dus à l'accumulation de force de deux guerriers
        damages = (self._character._strength * 20) * self.get_endurance_ratio()
        target.take_damages(damages)

    def take_damages(self, amount):
        # Très grande résistance aux dégâts
        self._character._life -= amount * self.get_endurance_ratio(1.2)
        self._character._endurance -= amount * self.get_endurance_ratio()
