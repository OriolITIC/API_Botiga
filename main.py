from typing import Union, List
from fastapi import FastAPI, File, UploadFile
import csv
import io
import persistencia.categoria_per as category_pers
import persistencia.subcategoria_per as subcategory_pers
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

@app.post("/loadProducts")
async def load_products(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        csv_data = io.StringIO(contents.decode("utf-8"))
        reader = csv.DictReader(csv_data)

        category_id_set = set()
        subcategory_id_set = set()

        for row in reader:
            category_id = int(row["id_categoria"])
            category_name = row["nom_categoria"]
            subcategory_id = int(row["id_subcategoria"])
            subcategory_name = row["nom_subcategoria"]
            product_id = int(row["id_producto"])
            product_name = row["nom_producto"]
            product_description = row["descripcion_producto"]
            product_company = row["companyia"]
            product_price = row["precio"]
            product_units = float(row["unidades"])

            # miramos si ya existe category_id 
            if (category_id not in category_id_set):
                if (category_pers.read_by_id(category_id) is not None):
                    category_pers.update_name(category_id, category_name)
                else:
                    category_pers.create_with_id(category_id, category_name)
                category_id_set.add(category_id)

            if (subcategory_id not in subcategory_id_set):
                if (subcategory_pers.read_by_id(subcategory_id) is not None):
                    subcategory_pers.update_name(subcategory_id, subcategory_name)
                else:
                    subcategory_pers.create_with_id(subcategory_id, subcategory_name, category_id)
                category_id_set.add(category_id)

            if (producte_pers.read_by_id(product_id) is not None):
                producte_pers.update_name(product_id, product_name)
            else:
                producte_pers.create_with_id(product_id, product_name, product_company, product_price, subcategory_id, product_description, product_units)

        return {"message": "S'ha carregat correctament"}

    except Exception as e:
        raise {"status": -1, "message": f"Error: {str(e)}"}
