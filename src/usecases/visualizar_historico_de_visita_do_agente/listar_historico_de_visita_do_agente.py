from db.connection import get_cursor_and_connection
from models.visita.visita import Visita

def listar_historico_visitas_agente(id_agente: int) -> list[Visita]:
    cursor, conn = get_cursor_and_connection()
    visitas = []

    try:
        cursor.execute('''
            SELECT idagente, idfamilia, idrelatorio, data, hora, status
            FROM visita
            WHERE idagente = %s
            ORDER BY data DESC, hora DESC
        ''', (id_agente,))

        rows = cursor.fetchall()

        for row in rows:
            visita = Visita(
                id_agente=row[0],
                id_familia=row[1],
                id_relatorio=row[2],
                data=row[3],
                hora=row[4].strftime('%H:%M:%S'),
                status=row[5]
            )
            visitas.append(visita)

        return visitas

    except Exception as e:
        print(f"Erro ao listar histórico de visitas do agente {id_agente}: {e}")
        return []

    finally:
        cursor.close()
        conn.close()
