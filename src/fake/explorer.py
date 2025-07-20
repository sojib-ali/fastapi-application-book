from model.explorer import Explorer

_explorers = [
    Explorer(name = "Claude Hande",
             country = "FR",
             description = "Scarce during full moons"),
    Explorer(name = "Noah Weiser",
             country = "DE",
             description = "Myopic machete man"),
]

def get_all() -> list[Explorer]:
    #return all explorers
    return _explorers

def get_one(name: str) -> Explorer | None: 
    for _expolorer in _explorers:
        if _expolorer.name == name:
            return _expolorer
    return None

def create(explorer:Explorer) -> Explorer:
    #Add an explorer
    return explorer

def modify(explorer: Explorer) -> Explorer:
    #partially modify an explorer
    return explorer

def replace(explorer: Explorer) -> Explorer:
    #completely replace an explorer
    return explorer

def delete(name: str) -> bool: 
    #Delete an explorer: return None if it existed
    return None