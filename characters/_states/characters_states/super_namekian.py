from characters._states.state import CharacterState

class SuperNamekianState(CharacterState):

    _default_endurance = 250  # Augmentation modérée d'endurance sans perte de vitesse
    _default_life = 4500
    available_classes = ["namekian"]

    def get_endurance_ratio(self, impact=0):
        return (self._character._endurance / self._default_endurance) + impact

    def deal_damages(self, target):
        # Force augmentée sans pénaliser la vitesse
        damages = (self._character._strength * 4) * self.get_endurance_ratio()
        target.take_damages(damages)

    def take_damages(self, amount):
        # L'endurance accrue permet de mieux encaisser les coups
        self._character._life -= amount * self.get_endurance_ratio(0.7)
        self._character._endurance -= amount * self.get_endurance_ratio()
