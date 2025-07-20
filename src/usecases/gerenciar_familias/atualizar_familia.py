from db.connection import get_cursor_and_connection
from models.familia.familia import Familia

def edita_familia(f : Familia, id : int):
    cursor, conn = get_cursor_and_connection()

    try:
        cursor.execute('''
            UPDATE familia
            SET nome = %s,
                rua = %s,
                numero = %s,
                bairro = %s,
                cidade = %s,
                telefone = %s,
                renda = %s,
                numeromembros = %s
            WHERE idfamilia = %s
        ''', (
            f.nome,
            f.rua,
            f.numero,
            f.bairro,
            f.cidade,
            f.telefone,
            f.renda,
            f.numero_membros,
            id
        ))
        conn.commit()
        
    except Exception as e:
        conn.rollback()
        print(f"Erro ao editar família: {e}")

    finally:
        cursor.close()
        conn.close()