from model.creature import Creature

_creatures = [
    Creature(name="Yeti", 
             aka="Abominable Snowman", 
             country="CN", 
             area="Himalayas", 
             description="Hirsute Himalayan"),

    Creature(name="Bigfoot", 
             description="Yeti's Cousin Eddie", 
             country="US", 
             area="*", 
             aka="Sasquatch")
]

def get_all() -> list[Creature]:
    #return all creatures
    return _creatures

def get_one(name: str) -> Creature | None:
    #return one creature
    for _creature in _creatures:
        if _creature.name == name:
            return _creature
    return None

def create(creature: Creature) -> Creature: 
    """Add a creature""" 
    return creature
def modify(creature: Creature) -> Creature: 
    """Partially modify a creature""" 
    return creature
def replace(creature: Creature) -> Creature: 
    """Completely replace a creature""" 
    return creature
def delete(name: str):
#Delete a creature: return None if it existed 
    return None