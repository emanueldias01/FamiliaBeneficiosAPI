from db.connection import get_cursor_and_connection
from models.familia.familia import Familia

def deletar_familia_por_id(id : int):
    cursor, conn = get_cursor_and_connection()
    
    try:
        cursor.execute('DELETE FROM familia WHERE idFamilia = %s', (id,))
        conn.commit()
    finally:
        cursor.close()
        conn.close()