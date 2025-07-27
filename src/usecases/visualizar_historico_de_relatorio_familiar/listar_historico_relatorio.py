from db.connection import get_cursor_and_connection
from models.relatorio.relatorio_observacoes.relatorio_observacoes import RelatorioObservacoes
from models.relatorio.relatorio_peso_familia.relatorio_peso_familia import RelatorioPesoFamilia
from models.relatorio.relatorio_vacinacao_familia.relatorio_vacinacao_familia import RelatorioVacinacaoFamilia

def buscar_historico_relatorios_familiar(id: int):
    cursor, conn = get_cursor_and_connection()

    try:
        # Busca todos os relatórios associados a visitas da família
        cursor.execute('''
            SELECT v.idrelatorio, v.data, v.hora, v.status, a.nome as agente
            FROM visita v
            INNER JOIN agente a ON v.idagente = a.idagente
            WHERE v.idfamilia = %s
            ORDER BY v.data DESC, v.hora DESC
        ''', (id,))

        visitas = cursor.fetchall()

        for visita in visitas:
            id_relatorio, data, hora, status, nome_agente = visita
            
            relatorio_info = {
                "id_relatorio": id_relatorio,
                "data": data,
                "hora": hora,
                "status": status,
                "agente": nome_agente,
                "dados": {
                    "observacoes": "",
                    "peso_familia": "",
                    "vacinacao_familia": ""
                }    
            }

            cursor.execute('SELECT observacoes FROM relatorio_observacoes WHERE idrelatorio = %s', (id_relatorio,))
            row = cursor.fetchone()
            relatorio_info["dados"]["observacoes"] = row[0]
            
            cursor.execute('SELECT vacinacaoFamilia FROM relatorio_vacinacaoFamilia WHERE idrelatorio = %s', (id_relatorio,))            
            row = cursor.fetchone()
            relatorio_info["dados"]["vacinacao_familia"] = row[0]

            cursor.execute('SELECT pesoFamilia FROM relatorio_pesoFamilia WHERE idrelatorio = %s', (id_relatorio,))
            row = cursor.fetchone()
            relatorio_info["dados"]["peso_familia"] = row[0]

        return relatorio_info

    except Exception as e:
        print(f"Erro ao buscar histórico de relatórios da família {id}: {e}")
        return []

    finally:
        cursor.close()
        conn.close()
