
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="flask_database",
    user="postgres",
    password="heritage"
)

def connection():
    return conn