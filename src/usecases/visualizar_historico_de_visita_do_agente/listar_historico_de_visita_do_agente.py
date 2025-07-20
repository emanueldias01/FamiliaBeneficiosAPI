from db.connection import get_cursor_and_connection
from models.visita.visita import Visita
from datetime import datetime

def listar_historico_visitas_agente(id_agente: int) -> list[Visita]:
    cursor, conn = get_cursor_and_connection()
    visitas = []

    try:
        cursor.execute('''
            SELECT idAgente, idfamilia, data, hora, status
            FROM visita
            WHERE idAgente = %s
            ORDER BY data DESC, hora DESC
        ''', (id_agente,))

        rows = cursor.fetchall()

        for row in rows:
            visita = Visita(
                id_agente=row[0],
                id_familia=row[1],
                data=row[2],
                hora=row[3].strftime('%H:%M:%S') if isinstance(row[3], datetime.time) else row[3],
                status=row[4]
            )
            visitas.append(visita)

        return visitas

    except Exception as e:
        print(f"Erro ao listar histórico de visitas do agente {id_agente}: {e}")
        return []

    finally:
        cursor.close()
        conn.close()
