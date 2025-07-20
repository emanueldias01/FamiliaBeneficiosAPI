from db.connection import get_cursor_and_connection
from models.visita.visita import Visita

def cadastrar_visita(v: Visita):
    cursor, conn = get_cursor_and_connection()

    try:
        cursor.execute('''
            INSERT INTO visita (
                idAgente, idfamilia, idRelatorio, data, hora, status
            ) VALUES (%s, %s, %s, %s, %s, %s)
        ''', (
            v.idAgente,
            v.idfamilia,
            v.idRelatorio,
            v.data,
            v.hora,
            v.status
        ))

        conn.commit()

    except Exception as e:
        conn.rollback()
        print(f"Erro ao cadastrar visita: {e}")
    finally:
        cursor.close()
        conn.close()
    