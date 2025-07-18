from db.connection import get_cursor_and_connection
from models.beneficio.beneficio import Beneficio

def listar_beneficios():
    cursor, conn = get_cursor_and_connection()
    beneficios = []

    try:
        cursor.execute('SELECT idBeneficio, nome, descricao, criterios, tipo, valor FROM beneficio')
        rows = cursor.fetchall()

        for row in rows:
            b = Beneficio(
                idBeneficio=row[0],
                nome=row[1],
                descricao=row[2],
                criterios=row[3],
                tipo=row[4],
                valor=row[5]
            )
            beneficios.append(b)

        return beneficios

    except Exception as e:
        print(f"Erro ao buscar benefícios: {e}")
        return []
    finally:
        cursor.close()
        conn.close()