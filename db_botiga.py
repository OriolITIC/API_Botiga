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




