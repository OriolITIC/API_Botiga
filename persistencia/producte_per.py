from models.producte import Product
from client import db_client
from typing import List

def create(name, company, price, subcategory_id, description, units, created_at=None, updated_at=None):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = f"INSERT INTO product (name, company, price, subcategory_id, description, units) VALUES (%s, %s, %s, %s, %s, %s);"
        values = (name, company, price, subcategory_id, description, units)
        cur.execute(query, values)
        conn.commit()
        product_id = cur.lastrowid
    
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}"}

    finally:
        conn.close()

    return product_id

def read():
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "SELECT * FROM product;"
        cur.execute(query)
        
        result = cur.fetchall()

    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}"}
    
    finally:
        conn.close()

    return result

def update_name(id, name):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = f"UPDATE product SET name = {name} WHERE product = {id};"
        cur.execute(query)
        conn.commit()
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}"}

    finally:
        conn.close()

def delete_by_Id(id):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = f"DELETE FROM product WHERE product_id = {id};"
        cur.execute(query)
        conn.commit()

    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}"}

    finally:
        conn.close()

def product_schema(product: Product) -> dict:
    return {
        "product_id": product[0],
        "name": product[1],
        "description": product[2],
        "company": product[3],
        "price": product[4],
        "units": product[5],
        "subcategory_id": product[6],
        "created_at": product[7],
        "updated_at": product[8]
    }

def products_schema(products: List[Product]) -> dict:
    return [product_schema(product) for product in products]