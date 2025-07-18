from db.connection import get_cursor_and_connection
from models.pessoa.pessoa import Pessoa

def listar_pessoas():
    cursor, conn = get_cursor_and_connection()

    try:
        cursor.execute('SELECT * FROM pessoa')
        result = cursor.fetchall()

        pessoas = []

        for row in result:
            pessoa = Pessoa(
                nis=row[0],
                nome=row[1],
                idade=row[2],
                dataNascimento=row[3],
                genero=row[4],
                idFamilia=row[5]
            )
            pessoas.append(pessoa)
        return pessoas
    
    except Exception as e:
        conn.rollback()
        print(f"Erro ao listar pessoas: {e}")
