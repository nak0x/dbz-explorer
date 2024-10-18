from characters._states.state import CharacterState

class FusionPotaraState(CharacterState):

    _default_endurance = 700  # Endurance encore plus grande que la fusion par danse
    _default_life =  10000
    available_classes = ["all"]

    def get_endurance_ratio(self, impact=0):
        return (self._character._endurance / self._default_endurance) + impact

    def deal_damages(self, target):
        # Force colossale obtenue grâce à la fusion Potara
        damages = (self._character._strength * 25) * self.get_endurance_ratio()
        target.take_damages(damages)

    def take_damages(self, amount):
        # La fusion Potara permet une très grande résistance
        self._character._life -= amount * self.get_endurance_ratio(1.5)
        self._character._endurance -= amount * self.get_endurance_ratio()
