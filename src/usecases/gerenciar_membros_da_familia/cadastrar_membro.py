from db.connection import get_cursor_and_connection
from models.pessoa.pessoa import Pessoa

def cria_pessoa_membro_familia(p : Pessoa, idF : int):
    cursor, conn = get_cursor_and_connection()

    try:
        # 1. Inserir a nova pessoa
        cursor.execute('''
            INSERT INTO pessoa (NIS, nome, idade, dataNascimento, genero, idfamilia, anoEscolar, renda, ocupacao)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        ''', (
            p.nis,
            p.nome,
            p.idade,
            p.dataNascimento,
            p.genero,
            idF,
            p.anoEscolar,
            p.renda,
            p.ocupacao
        ))

        # 2. Atualizar o número de membros da família (+1)
        cursor.execute('''
            UPDATE familia
            SET numeroMembros = COALESCE(numeroMembros, 0) + 1
            WHERE idfamilia = %s
        ''', (idF,))

        # 3. Atualizar a renda da família, somando com a renda da nova pessoa (se fornecida)
        if p.renda is not None:
            cursor.execute('''
                UPDATE familia
                SET renda = renda + %s
                WHERE idfamilia = %s
            ''', (p.renda, idF))

        conn.commit()

    except Exception as e:
        conn.rollback()
        print(f"Erro ao criar pessoa: {e}")
    finally:
        cursor.close()
        conn.close()