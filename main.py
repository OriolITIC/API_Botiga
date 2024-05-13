from typing import Union
from fastapi import FastAPI
import persistencia.producte_per as producte_pers

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/product")
def read_producte():
    return producte_pers.read()

@app.get("/productAll")
def read_all_productes():
    return producte_pers.readAll()

@app.get("/product/{id}")
def read_producte_by_id(id: int):
    producte = producte_pers.read_by_id(id)
    if producte:
        return producte
    else:
        return {"message": "Movie not found"}

@app.post("/product")
async def create_producte(data: producte):
    product_id = data.product_id
    name = data.name
    description = data.description
    company = data.company
    price = data.price
    units = data.units
    subcategory_id = data.subcategory_id
    created_at = data.created_at
    updated_at = data.updated_at

    producte_pers.create(product_id,name,description,company
                                      ,price,units,subcategory_id,created_at,updated_at)
    return {
        "msg": "S'ha afegit correctament"
    }

@app.put("/product/producte/{id}")
def update_producte(id:str,vots:int):
    producte_pers.update_producte(id,vots)

@app.delete("/product/{id}")
def delete_film(id:int):
    pelis_db.delete_producte(id)
