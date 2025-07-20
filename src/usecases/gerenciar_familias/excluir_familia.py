from db.connection import get_cursor_and_connection

def deletar_familia_por_id(id : int):
    cursor, conn = get_cursor_and_connection()
    
    try:
        cursor.execute('DELETE FROM familia WHERE idfamilia = %s', (id,))
        conn.commit()

    except Exception as e:
        conn.rollback()
        print(f"Erro ao excluir família: {e}")

    finally:
        cursor.close()
        conn.close()