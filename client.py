import mysql.connector
import client

def db_client():

    try:
        return mysql.connector.connect(
            host = client.,
            port = port,
            user = user,
            password = password,
            database = dbname
        )
    except Exception as e:
        return {"status": -1, "message": f"Error de connexio: {e}"}