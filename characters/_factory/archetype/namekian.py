from characters._factory.archetype import Archetype

class Namekian(Archetype):
    _classe = "namekian"
    def special_technique(self):
        if self._life <= self._state.get_life():
            self._life += (self._state.get_life() - self._life) * 0.2