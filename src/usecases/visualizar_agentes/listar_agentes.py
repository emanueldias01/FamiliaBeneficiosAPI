from db.connection import get_cursor_and_connection
from models.agente_visita.agente_visita import AgenteVisita

def listar_agente():
    cursor, conn = get_cursor_and_connection()
    agentes = []

    try:
        cursor.execute('SELECT idAgente, nome, contato, login, senha FROM agente')
        rows = cursor.fetchall()

        for row in rows:
            agente = AgenteVisita(
                idAgente=row[0],
                nome=row[1],
                contato=row[2],
                login=row[3],
                senha=row[4]
            )
            agentes.append(agente)

        return agentes

    except Exception as e:
        print(f"Erro ao listar agentes: {e}")
        return []
    finally:
        cursor.close()
        conn.close()