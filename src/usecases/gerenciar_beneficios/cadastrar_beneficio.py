from db.connection import get_cursor_and_connection
from models.beneficio.beneficio import Beneficio

def criar_beneficio(b : Beneficio):
    cursor, conn = get_cursor_and_connection()

    try:
        cursor.execute("""
            INSERT INTO beneficio(nome, descricao, criterios, tipo, valor)
            VALUES(%s, %s, %s, %s, %s)
        """, (b.nome, b.descricao, b.criterios, b.tipo, b.valor))
        conn.commit()

    except Exception as e:
        conn.rollback()
        print(f'Erro ao cadastrar beneficio: {e}')
    
    finally:
        cursor.close()
        conn.close()