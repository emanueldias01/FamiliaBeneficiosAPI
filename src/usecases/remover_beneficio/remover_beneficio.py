from db.connection import get_cursor_and_connection

def remover_beneficio_da_familia(idB : int, idF : int):
    cursor, conn = get_cursor_and_connection()

    try:
        cursor.execute('DELETE FROM tem WHERE idFamilia = %s AND idBeneficio = %s', (idF, idB))
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(f'Erro ao remover beneficio de familia: {e}')
    finally:
        cursor.close()
        conn.close()