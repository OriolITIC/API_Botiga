from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import db_botiga

app = FastAPI()

class film(BaseModel):
    titol: str
    any: int
    puntuacio:float
    vots: int

@app.get("/")
def read_root():
    return {"Hello": "World"}

#@app.get("/items/{item_id}")
#def read_item(item_id: int, q: Union[str, None] = None):
    #return {"item_id": item_id, "q": q}

@app.get("/productes")
def read_producte():
    return db_botiga.pelis_schema(db_botiga.read())

@app.get("/productes/{producte_id}")
def read_producte_by_id(peli_id: int):
    movie = db_botiga.read_by_id(peli_id)
    if movie:
        return db_botiga.peli_schema(movie)
    else:
        return {"message": "Movie not found"}
