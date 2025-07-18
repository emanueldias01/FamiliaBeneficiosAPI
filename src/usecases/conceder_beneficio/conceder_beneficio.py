from db.connection import get_cursor_and_connection
from datetime import date
  
def conceder_beneficio_a_familia  (idB : int, idF : int):
    cursor, conn = get_cursor_and_connection()
    try:
        cursor.execute("""
            INSERT INTO tem(idFamilia, idBeneficio, dataInicio)
            values(%s, %s, %s)
        """,
        (idB, idF, date.today()))

        conn.commit()

    except Exception as e:
        conn.rollback()
        print(f'Erro ao conceder beneficio: {e}')
    finally:
        cursor.close()
        conn.close()