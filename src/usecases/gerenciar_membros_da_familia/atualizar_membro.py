from db.connection import get_cursor_and_connection
from models.pessoa.pessoa import Pessoa

def edita_pessoa(p : Pessoa, idP : int):
    cursor, conn = get_cursor_and_connection()

    try:
        # 1. Buscar a renda e id da família anterior da pessoa
        cursor.execute('SELECT renda, idFamilia FROM pessoa WHERE NIS = %s', (idP,))
        result = cursor.fetchone()
        if not result:
            print("Pessoa não encontrada.")
            return

        renda_antiga, id_familia = result

        # 2. Atualizar os dados da pessoa
        cursor.execute('''
            UPDATE pessoa
            SET nome = %s,
                idade = %s,
                dataNascimento = %s,
                genero = %s,
                anoEscolar = %s,
                renda = %s,
                ocupacao = %s
            WHERE NIS = %s
        ''', (
            p.nome,
            p.idade,
            p.dataNascimento,
            p.genero,
            p.anoEscolar,
            p.renda,
            p.ocupacao,
            idP
        ))

        # 3. Atualizar a renda da família, se a renda mudou
        if p.renda is not None and renda_antiga is not None:
            diferenca_renda = p.renda - renda_antiga
            cursor.execute('''
                UPDATE familia
                SET renda = renda + %s
                WHERE idFamilia = %s
            ''', (diferenca_renda, id_familia))
        elif p.renda is not None and renda_antiga is None:
            cursor.execute('''
                UPDATE familia
                SET renda = renda + %s
                WHERE idFamilia = %s
            ''', (p.renda, id_familia))
        elif p.renda is None and renda_antiga is not None:
            cursor.execute('''
                UPDATE familia
                SET renda = renda - %s
                WHERE idFamilia = %s
            ''', (renda_antiga, id_familia))

        conn.commit()

    except Exception as e:
        conn.rollback()
        print(f"Erro ao editar pessoa: {e}")
    finally:
        cursor.close()
        conn.close()