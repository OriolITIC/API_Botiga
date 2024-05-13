import mysql.connector
from configuracio import config

def db_client():

    try:
        return mysql.connector.connect(
            host = config["host"],
            port = config["port"],
            user = config["user"],
            password = config["password"],
            database = config["dbname"]
        )
    except Exception as e:
        return {"status": -1, "message": f"Error de connexio: {e}"}