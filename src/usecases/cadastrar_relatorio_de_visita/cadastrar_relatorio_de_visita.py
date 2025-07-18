from pydantic import BaseModel
from db.connection import get_cursor_and_connection
from models.relatorio import relatorio
from models.relatorio.relatorio_observacoes import relatorio_observacoes
from models.relatorio.relatorio_peso_familia import relatorio_peso_familia
from models.relatorio.relatorio_vacinacao_familia import relatorio_vacinacao_familia

class TipoRelatorio(BaseModel):
    tipo_relatorio : str
    dados : str

def cadastrar_relatorio(tipo : TipoRelatorio):
    cursor, conn = get_cursor_and_connection()

    try:
        # 1. Cria registro em relatorio e pega o id
        cursor.execute('INSERT INTO relatorio DEFAULT VALUES RETURNING idRelatorio')
        id_relatorio = cursor.fetchone()[0]

        # 2. Insere na tabela correspondente
        if tipo.tipo_relatorio == 'relatorio_observacoes':
            cursor.execute(
                'INSERT INTO relatorio_observacoes (observacoes, idRelatorio) VALUES (%s, %s)',
                (tipo.dados, id_relatorio)
            )

        elif tipo.tipo_relatorio == 'relatorio_vacinacaoFamilia':
            cursor.execute(
                'INSERT INTO relatorio_vacinacaoFamilia (vacinacaoFamilia, idRelatorio) VALUES (%s, %s)',
                (tipo.dados, id_relatorio)
            )

        elif tipo.tipo_relatorio == 'relatorio_pesoFamilia':
            cursor.execute(
                'INSERT INTO relatorio_pesoFamilia (pesoFamilia, idRelatorio) VALUES (%s, %s)',
                (tipo.dados, id_relatorio)
            )

        else:
            raise ValueError("Tipo de relatório inválido.")

        conn.commit()
        return id_relatorio

    except Exception as e:
        conn.rollback()
        print(f"Erro ao cadastrar relatório: {e}")
        return None

    finally:
        cursor.close()
        conn.close()
    