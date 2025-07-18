from db.connection import get_cursor_and_connection
from models.familia.familia import Familia

def busca_familia_por_id(id : int):
    cursor, conn = get_cursor_and_connection()
    
    try:
        cursor.execute("SELECT * FROM familia WHERE idFamilia = %s", (id,))
        row = cursor.fetchone()

        if row is None:
            return None

        familia = Familia(
            id_familia=row[0],
            nome=row[1],
            rua=row[2],
            numero=row[3],
            bairro=row[4],
            cidade=row[5],
            telefone=row[6],
            renda=row[7],
            numero_membros=row[8]
        )
        return familia
    
    except Exception as e:
        conn.rollback()
        print(f"Erro ao editar família: {e}")
        
    finally:
        cursor.close()
        conn.close()