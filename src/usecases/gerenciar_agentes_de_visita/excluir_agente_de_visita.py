from db.connection import get_cursor_and_connection

def deletar_agente_por_id(id : int):
    cursor, conn = get_cursor_and_connection()

    try:
        cursor.execute('DELETE FROM agente WHERE idAgente = %s', (id,))
        conn.commit()
    
    except Exception as e:
        conn.rollback()
        print(f'Erro ao deletar agente: {e}')

    finally:
        cursor.close()
        conn.close()