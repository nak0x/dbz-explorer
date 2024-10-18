from characters._factory.archetype import Archetype

class Android(Archetype):
    _classe = "android"
    def special_technique(self):
        # No special technique - they tank
        pass

    def take_damages(self, amount):
        super().take_damages(amount)
        self._endurance = self._state.get_endurance()