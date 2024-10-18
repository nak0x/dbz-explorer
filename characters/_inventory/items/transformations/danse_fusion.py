from characters._inventory import Item
from characters import Character
from characters._states.characters_states import FusionDanceState

class TransformationFusionDanse(Item):

    def __init__(self, name, inventory) -> None:
        super().__init__(inventory, name)
        self.set_data("available_classes", ["any"])

    def use(self, target: Character, partner: Character):
        available_classes = self.get_data("available_classes")
        if target._classe in available_classes or "all" in available_classes:
            target.transition_to(FusionDanceState())
        else:
            print("Fusion par danse impossible : conditions de fusion non respectées.")