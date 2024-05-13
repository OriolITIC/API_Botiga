from models.categoria import Category
from client import db_client
from typing import List

def create(name):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = f"INSERT INTO category (name) VALUES ({name});"
        cur.execute(query)
        conn.commit()
        category_id = cur.lastrowid
    
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}"}

    finally:
        conn.close()

    return category_id

def read():
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "SELECT * FROM category;"
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
        query = f"UPDATE category SET name = {name} WHERE category_id = {id};"
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
        query = f"DELETE FROM category WHERE category_id = {id};"
        cur.execute(query)
        conn.commit()

    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}"}

    finally:
        conn.close()

def category_schema(category: Category) -> dict:
    return {
        "category_id": category[0],
        "name": category[1],
        "created_at": category[2],
        "updated_at": category[3]
    }

def categories_schema(categories: List[Category]) -> dict:
    return [category_schema(category) for category in categories]