from db.connection import get_cursor_and_connection
from models.pessoa.pessoa import Pessoa

def buscar_pessoa_por_nis(nis : int):
    cursor, conn = get_cursor_and_connection()

    try:
        cursor.execute('SELECT * FROM pessoa WHERE nis = %s'(nis,))
        row = cursor.fetchall()

        if row is None:
            return None
        
        pessoa = Pessoa(
            nis=row[0],
            nome=row[1],
            idade=row[2],
            dataNascimento=row[3],
            genero=row[4],
            idFamilia=[5],
            anoEscolar=row[6],
            renda=row[7],
            ocupacao=row[8]
        )
        
        return pessoa
    
    except Exception as e:
        print(f'Erro ao buscar pessoa por nis: {e}')
    
    finally:
        cursor.close()
        conn.close()
        