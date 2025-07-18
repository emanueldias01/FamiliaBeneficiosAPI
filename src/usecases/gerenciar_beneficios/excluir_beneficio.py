from db.connection import get_cursor_and_connection

def deletar_beneficio_por_id(id : int):
    cursor, conn = get_cursor_and_connection()
    
    try:
        cursor.execute('DELETE FROM beneficio WHERE idBeneficio = %s', (id,))
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(f'Erro ao deletar beneficio: {e}')
    finally:
        cursor.close()
        conn.close()
