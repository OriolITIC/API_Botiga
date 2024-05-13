from typing import Union, List
from fastapi import FastAPI
import persistencia.producte_per as producte_pers

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/product", response_model = List[dict])
def read_producte():
    return producte_pers.products_schema(producte_pers.read())

@app.get("/product/{id}")
def read_producte_by_id(id: int):
    producte = producte_pers.read_by_id(id)
    if producte:
        return producte
    else:
        return {"message": "product not found"}

@app.post("/product")
def create(name:str, company:str, price:float, subcategory_id:int, description:str=None, units:int=None, created_at=None, updated_at=None):
    return producte_pers.create(name, company, price, subcategory_id, description, units, created_at, updated_at)

@app.put("/product/{id}")
def update_name(id:int, name:str):
    return producte_pers.update_name(id, name)

@app.delete("/product/{id}")
def delete(id:int):
    return producte_pers.delete_by_Id(id)

@app.get("/productAll")
def read_all_productes():
    return producte_pers.readAll_list_schema(producte_pers.readAll())
