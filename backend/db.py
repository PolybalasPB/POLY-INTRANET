import psycopg2
from psycopg2.extras import RealDictCursor

def get_connection():
    conn = psycopg2.connect(
        dbname="empresa",
        user="postgres",
        password="root",
        host="localhost",
        port="5432"
    )
    return conn