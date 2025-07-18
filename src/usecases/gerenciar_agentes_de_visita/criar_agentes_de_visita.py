from db.connection import get_cursor_and_connection
from models.agente_visita.agente_visita import AgenteVisita

def criar_agente(a : AgenteVisita):
    cursor, conn = get_cursor_and_connection()

    try:
        cursor.execute('''
            INSERT INTO agente (nome, contato, login, senha)
            VALUES (%s, %s, %s, %s)
        ''', (
            a.nome,
            a.contato,
            a.login,
            a.senha
        ))
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(f"Erro ao criar agente: {e}")
    finally:
        cursor.close()
        conn.close()