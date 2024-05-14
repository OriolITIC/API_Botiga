from models.subcategoria import Subcategory
from client import db_client
from typing import List

def create(name, category_id):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = f"INSERT INTO subcategory (name, category_id) VALUES ('{name}', {category_id});"
        cur.execute(query)
        conn.commit()
        subcategory_id = cur.lastrowid
    
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}"}

    finally:
        conn.close()

    return subcategory_id

def create_with_id(subcategory_id, name, category_id):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = f"INSERT INTO subcategory (subcategory_id, name, category_id) VALUES ({subcategory_id}, '{name}', {category_id});"
        cur.execute(query)
        conn.commit()
        subcategory_id = cur.lastrowid
    
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}"}

    finally:
        conn.close()

    return subcategory_id

def read():
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "SELECT * FROM subcategory;"
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
        query = f"SELECT * FROM subcategory WHERE subcategory_id = {id};"
        cur.execute(query)
        
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
        query = f"UPDATE subcategory SET name = '{name}', updated_at = NOW() WHERE subcategory_id = {id};"
        cur.execute(query)
        conn.commit()
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}"}

    finally:
        conn.close()

def update(subcategory_id, name, category_id):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = f"UPDATE subcategory SET name = '{name}', category_id = {category_id}, updated_at = NOW() WHERE subcategory_id = {subcategory_id};"
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
        query = f"DELETE FROM subcategory WHERE subcategory_id = {id};"
        cur.execute(query)
        conn.commit()

    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}"}

    finally:
        conn.close()

def subcategory_schema(subcategory: Subcategory) -> dict:
    return {
        "subcategory_id": subcategory[0],
        "name": subcategory[1],
        "category_id": subcategory[2],
        "created_at": subcategory[3],
        "updated_at":subcategory[4]
    }

def subcategories_schema(subcategories: List[Subcategory]) -> dict:
    return [subcategory_schema(subcategory) for subcategory in subcategories]