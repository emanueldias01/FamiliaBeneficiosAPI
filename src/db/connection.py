import psycopg2

def get_cursor_and_connection():
    conn = psycopg2.connect(
        dbname='familia_beneficios_db',
        user='admin',
        password='admin123',
        host='localhost',
        port='5432'
    )
    cur = conn.cursor()
    return cur, conn