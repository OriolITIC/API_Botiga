from models.producte import Product
from client import db_client
from typing import List

def create(name, company, price, subcategory_id, description=None, units=None, created_at=None, updated_at=None):
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

    return {"message": f"S'ha afegit correctament"}

def create_with_id(product_id, name, company, price, subcategory_id, description=None, units=None, created_at=None, updated_at=None):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = f"INSERT INTO product (product_id, name, company, price, subcategory_id, description, units) VALUES (%s, %s, %s, %s, %s, %s, %s);"
        values = (product_id, name, company, price, subcategory_id, description, units)
        cur.execute(query, values)
        conn.commit()
        product_id = cur.lastrowid
    
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}"}
    
    finally:
        conn.close()

    return {"message": f"S'ha afegit correctament"}

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

def read_by_id(id):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "SELECT * FROM product WHERE product_id = %s;"
        cur.execute(query, (id,))
        
        result = cur.fetchone()

    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}"}
    
    finally:
        conn.close()

    return result

def update_name(id, name):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "UPDATE product SET name = %s, updated_at = NOW() WHERE product_id = %s;"
        values = (name, id)
        cur.execute(query, values)
        conn.commit()
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}"}

    finally:
        conn.close()

    return {"message": f"S'ha modificat correctament"}

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

    return {"message": f"S'ha borrat correctament"}

def readAll():
    try:
        conn = db_client()
        cur = conn.cursor()
        query = """
            SELECT c.name AS category_name, s.name AS subcategory_name, p.name AS product_name, p.company AS product_brand, p.price
            FROM product p
            JOIN subcategory s ON p.subcategory_id = s.subcategory_id
            JOIN category c ON s.category_id = c.category_id;
        """
        cur.execute(query)
        
        result = cur.fetchall()

    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}"}
    
    finally:
        conn.close()

    return result

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

def readAll_schema(product) -> dict:
    return {
        "category_name": product[0],
        "subcategory_name": product[1],
        "product_name": product[2],
        "product_brand": product[3],
        "price": product[4]
    } 

def readAll_list_schema(products) -> dict:
    return [readAll_schema(product) for product in products]