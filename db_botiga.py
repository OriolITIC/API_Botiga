from client import db_client

def read():
    try:
        conn = db_client()
        cur = conn.cursor()
        cur.execute("select * from product")

        result = cur.fetchall()
    
    except Exception as e:
        return{"status": -1, "message": f"Error de connexió:{e}" }
    
    finally:
        conn.close()

    return result




def producte_schema(peli) -> dict:
    return {"Id": peli[0],
            "titol": peli[1],
            "any": peli[2],
            "puntuacio": peli[3],
            "vots": peli[4]
            }