from db.connection import get_cursor_and_connection
from models.relatorio.relatorio import Relatorio
from models.relatorio.relatorio_observacoes.relatorio_observacoes import RelatorioObservacoes
from models.relatorio.relatorio_peso_familia.relatorio_peso_familia import RelatorioPesoFamilia
from models.relatorio.relatorio_vacinacao_familia.relatorio_vacinacao_familia import RelatorioVacinacaoFamilia

def listar_historico_relatorios_por_agente(id: int):
    cursor, conn = get_cursor_and_connection()
    historico = []

    try:
        cursor.execute("""
            SELECT v.idRelatorio, v.data, v.hora, v.status,
                   ro.observacoes,
                   rp.pesoFamilia,
                   rv.vacinacaoFamilia
            FROM visita v
            LEFT JOIN relatorio_observacoes ro ON v.idRelatorio = ro.idRelatorio
            LEFT JOIN relatorio_pesoFamilia rp ON v.idRelatorio = rp.idRelatorio
            LEFT JOIN relatorio_vacinacaoFamilia rv ON v.idRelatorio = rv.idRelatorio
            WHERE v.idAgente = %s
            ORDER BY v.data DESC, v.hora DESC
        """, (id,))

        rows = cursor.fetchall()
        for row in rows:
            relatorio = {
                "id_relatorio": row[0],
                "data": row[1].isoformat() if row[1] else None,
                "hora": row[2].isoformat() if row[2] else None,
                "status": row[3],
                "observacoes": row[4],
                "peso_familia": row[5],
                "vacinacao_familia": row[6]
            }
            historico.append(relatorio)

        return historico

    except Exception as e:
        print(f"Erro ao buscar histórico de relatórios do agente {id}: {e}")
        return []

    finally:
        cursor.close()
        conn.close()
