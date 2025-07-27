from pydantic import BaseModel
from db.connection import get_cursor_and_connection
from models.relatorio import relatorio
from models.relatorio.relatorio_observacoes import relatorio_observacoes
from models.relatorio.relatorio_peso_familia import relatorio_peso_familia
from models.relatorio.relatorio_vacinacao_familia import relatorio_vacinacao_familia

class TipoRelatorio(BaseModel):
    dados_vacinacao : str
    dados_peso : str
    dados_observacao : str

def cadastrar_relatorio(tipo : TipoRelatorio):
    cursor, conn = get_cursor_and_connection()

    try:
        cursor.execute('INSERT INTO relatorio DEFAULT VALUES RETURNING idrelatorio')
        id_relatorio = cursor.fetchone()[0]
        
        cursor.execute(
            'INSERT INTO relatorio_observacoes (observacoes, idrelatorio) VALUES (%s, %s)',
            (tipo.dados_observacao, id_relatorio)
        )

        cursor.execute(
            'INSERT INTO relatorio_vacinacaoFamilia (vacinacaoFamilia, idrelatorio) VALUES (%s, %s)',
            (tipo.dados_vacinacao, id_relatorio)
        )

        cursor.execute(
            'INSERT INTO relatorio_pesoFamilia (pesoFamilia, idrelatorio) VALUES (%s, %s)',
            (tipo.dados_peso, id_relatorio)
        )

        conn.commit()
        return id_relatorio

    except Exception as e:
        conn.rollback()
        print(f"Erro ao cadastrar relatório: {e}")
        return None

    finally:
        cursor.close()
        conn.close()
    