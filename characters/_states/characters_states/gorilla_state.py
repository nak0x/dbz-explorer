from characters._states.state import CharacterState

class GorillaState(CharacterState):

    _default_endurance = 300  # Endurance largement augmentée en forme de Gorille Géant
    _default_life = 5000
    available_classes = ["saiyan"]

    def get_endurance_ratio(self, impact=0):
        return (self._character._endurance / self._default_endurance) + impact

    def deal_damages(self, target):
        # Les Saiyans sous forme de gorille infligent des dégâts considérablement augmentés
        damages = (self._character._strength * 10) * self.get_endurance_ratio()
        target.take_damages(damages)

    def take_damages(self, amount):
        # Le Gorille Géant a une grande résistance aux dégâts
        self._character._life -= (amount * self.get_endurance_ratio(0.5))
        self._character._endurance -= amount * self.get_endurance_ratio()