import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("HOST_NAME")
db_username = os.getenv("USER_NAME")
db_port = os.getenv("PORT")
db_name = os.getenv("DATA_BASE")

conn = psycopg2.connect(host=db_host, dbname=db_name, user=db_username, password=db_password, port=db_port)



print("Database Connectd...")
conn.close()