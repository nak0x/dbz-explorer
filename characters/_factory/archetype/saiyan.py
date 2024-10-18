from characters._factory.archetype import Archetype

class Saiyan(Archetype):
    _classe = "saiyan"
    def special_technique(self):
        if self._life <= self._state.get_life() * 0.1:
            # use decorator to increase perf
            pass