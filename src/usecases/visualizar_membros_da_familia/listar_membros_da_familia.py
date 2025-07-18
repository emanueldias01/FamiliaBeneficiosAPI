from models.pessoa.pessoa import Pessoa, GeneroEnum
from db.connection import get_cursor_and_connection

def listar_membros_familia(idFamilia: int):
    cursor, conn = get_cursor_and_connection()
    membros = []

    try:
        cursor.execute('''
            SELECT nis, nome, idade, dataNascimento, genero, idFamilia,
                   anoEscolar, renda, ocupacao
            FROM pessoa
            WHERE idFamilia = %s
        ''', (idFamilia,))
        
        result = cursor.fetchall()

        for row in result:
            membro = Pessoa(
                nis=str(row[0]),
                nome=row[1],
                idade=row[2],
                dataNascimento=row[3],
                genero=GeneroEnum(row[4]) if row[4] else GeneroEnum.OUTRO,
                idFamilia=row[5],
                anoEscolar=row[6],
                renda=float(row[7]) if row[7] is not None else 0.0,
                ocupacao=row[8]
            )
            membros.append(membro)

        return membros

    except Exception as e:
        print(f"Erro ao listar membros da família: {e}")
        return []
    finally:
        cursor.close()
        conn.close()
