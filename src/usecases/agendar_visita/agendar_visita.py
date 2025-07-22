from db.connection import get_cursor_and_connection
from models.visita.visita import Visita

def cadastrar_visita(v: Visita):
    cursor, conn = get_cursor_and_connection()

    try:
        cursor.execute('''
            INSERT INTO visita (
                idagente, idfamilia, idrelatorio, data, hora, status
            ) VALUES (%s, %s, %s, %s, %s, %s)
        ''', (
            v.id_agente,
            v.id_familia,
            v.id_relatorio,
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
    