from db.connection import get_cursor_and_connection
from models.familia.familia import Familia

def criar_familia(f : Familia):
    cursor, conn = get_cursor_and_connection()
    
    try:
        cursor.execute(
            """INSERT INTO familia
                       (nome, rua, numero, bairro, cidade, telefone, renda, numeroMembros)
                       VALUES
                       (%s, %s, %s, %s, %s, %s, %s, %s)
                       RETURNING idfamilia
                       """,
        (f.nome, f.rua, f.numero, f.bairro, f.cidade, f.telefone, f.renda, f.numero_membros))

        id_familia = cursor.fetchone()[0]
        conn.commit()

        f.id_familia = id_familia

        return f
    
    except Exception as e:
        conn.rollback()
        print(f"Erro ao cadastrar família: {e}")

    finally:
        cursor.close()
        conn.close()