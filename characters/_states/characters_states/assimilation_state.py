from characters._states.state import CharacterState

class AssimilationState(CharacterState):

    _default_endurance = 200  # Endurance augmentée après assimilation
    _default_life = 4000
    available_classes = ["namekian"]

    def get_endurance_ratio(self, impact=0):
        return (self._character._endurance / self._default_endurance) + impact

    def deal_damages(self, target):
        # Force augmentée suite à l'assimilation d'un autre Namekian
        damages = (self._character._strength * 5) * self.get_endurance_ratio()
        target.take_damages(damages)

    def take_damages(self, amount):
        # L'assimilation offre une meilleure résistance
        self._character._life -= (amount * self.get_endurance_ratio(1))
        self._character._endurance -= amount * self.get_endurance_ratio()
