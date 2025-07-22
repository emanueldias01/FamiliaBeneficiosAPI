from db.connection import get_cursor_and_connection
from models.agente_visita.agente_visita import AgenteVisita

def editar_agente(a : AgenteVisita, id : int):
    cursor, conn = get_cursor_and_connection()

    try:
        cursor.execute('''
            UPDATE agente
            SET nome = %s,
                contato = %s,
                login = %s,
                senha = %s
            WHERE idagente = %s
        ''', (
            a.nome,
            a.contato,
            a.login,
            a.senha,
            id
        ))
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(f"Erro ao editar agente: {e}")
    finally:
        cursor.close()
        conn.close()