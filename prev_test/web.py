from prev_test.model import Creature
from fastapi import FastAPI
from prev_test.data import get_creatures

app = FastAPI()

@app.get("/creature")
def get_all() -> list[Creature]:  
    return get_creatures()