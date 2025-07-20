from db.connection import get_cursor_and_connection
from models.beneficio.beneficio import Beneficio

def editar_beneficio(beneficio: Beneficio, idB: int):
    cursor, conn = get_cursor_and_connection()

    try:
        cursor.execute('''
            UPDATE beneficio
            SET nome = %s,
                descricao = %s,
                criterios = %s,
                tipo = %s,
                valor = %s
            WHERE idbeneficio = %s
        ''', (
            beneficio.nome,
            beneficio.descricao,
            beneficio.criterios,
            beneficio.tipo,
            beneficio.valor,
            idB
        ))

        conn.commit()

    except Exception as e:
        conn.rollback()
        print(f"Erro ao editar benefício: {e}")
    finally:
        cursor.close()
        conn.close()
    