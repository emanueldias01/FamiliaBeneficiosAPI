from db.connection import get_cursor_and_connection
from models.familia.familia import Familia

def lista_familias_cadastradas():
    cursor, conn = get_cursor_and_connection()

    try:
        cursor.execute('SELECT * FROM familia')
        result = cursor.fetchall()

        familias = []
        for row in result:
            familia = Familia(
                id_familia=row[0],
                nome=row[1],
                rua=row[2],
                numero=row[3],
                bairro=row[4],
                cidade=row[5],
                telefone=row[6],
                renda=row[7],
                numero_membros=row[8]
            )
            familias.append(familia)

        return familias

    finally:
        cursor.close()
        conn.close()