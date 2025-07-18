from db.connection import get_cursor_and_connection
from models.relatorio.relatorio_observacoes import RelatorioObservacoes
from models.relatorio.relatorio_peso_familia import RelatorioPesoFamilia
from models.relatorio.relatorio_vacinacao_familia import RelatorioVacinacaoFamilia

def buscar_historico_relatorios_familiar(id: int):
    cursor, conn = get_cursor_and_connection()

    try:
        # Busca todos os relatórios associados a visitas da família
        cursor.execute('''
            SELECT v.idRelatorio, v.data, v.hora, v.status, a.nome as agente
            FROM visita v
            INNER JOIN agente a ON v.idAgente = a.idAgente
            WHERE v.idFamilia = %s
            ORDER BY v.data DESC, v.hora DESC
        ''', (id,))

        visitas = cursor.fetchall()
        historico = []

        for visita in visitas:
            id_relatorio, data, hora, status, nome_agente = visita
            relatorio_info = {
                "id_relatorio": id_relatorio,
                "data": data,
                "hora": hora,
                "status": status,
                "agente": nome_agente,
                "tipo": None,
                "conteudo": None
            }

            # Verifica em qual tabela especializada o relatório está
            cursor.execute('SELECT observacoes FROM relatorio_observacoes WHERE idRelatorio = %s', (id_relatorio,))
            row = cursor.fetchone()
            if row:
                relatorio_info["tipo"] = "observacoes"
                relatorio_info["conteudo"] = RelatorioObservacoes(id_relatorio=id_relatorio, observacoes=row[0])
                historico.append(relatorio_info)
                continue

            cursor.execute('SELECT vacinacaoFamilia FROM relatorio_vacinacaoFamilia WHERE idRelatorio = %s', (id_relatorio,))
            row = cursor.fetchone()
            if row:
                relatorio_info["tipo"] = "vacinacao_familia"
                relatorio_info["conteudo"] = RelatorioVacinacaoFamilia(id_relatorio=id_relatorio, vacinacao_familia=row[0])
                historico.append(relatorio_info)
                continue

            cursor.execute('SELECT pesoFamilia FROM relatorio_pesoFamilia WHERE idRelatorio = %s', (id_relatorio,))
            row = cursor.fetchone()
            if row:
                relatorio_info["tipo"] = "peso_familia"
                relatorio_info["conteudo"] = RelatorioPesoFamilia(id_relatorio=id_relatorio, peso_familia=float(row[0]))
                historico.append(relatorio_info)

        return historico

    except Exception as e:
        print(f"Erro ao buscar histórico de relatórios da família {id}: {e}")
        return []

    finally:
        cursor.close()
        conn.close()
