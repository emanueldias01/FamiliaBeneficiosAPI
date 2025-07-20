from db.connection import get_cursor_and_connection
from models.beneficio.beneficio import Beneficio

def busca_beneficio_por_id(id : int):
    cursor, conn = get_cursor_and_connection()

    try:
        cursor.execute('SELECT * FROM beneficio WHERE idbeneficio = %s', (id,))
        row = cursor.fetchall()

        if row is None:
            return None

        beneficio = Beneficio(
            id_beneficio=row[0],
            nome=row[1],
            descricao=row[2],
            criterios=row[3],
            tipo=row[4],
            valor=row[5]
        )

        return beneficio
    
    except Exception as e:
        print(f'Erro ao buscar beneficio: {e}')
    finally:
        cursor.close()
        conn.close()