from db.connection import get_cursor_and_connection
from models.beneficio.beneficio import Beneficio

def vizualizar_beneficios_recebidos_por_familia_id(id: int):
    cursor, conn = get_cursor_and_connection()

    try:
        cursor.execute("""
            SELECT b.idBeneficio, b.nome, b.descricao, b.criterios, b.tipo, b.valor, t.dataInicio
            FROM tem t
            INNER JOIN beneficio b ON t.idBeneficio = b.idBeneficio
            WHERE t.idFamilia = %s
        """, (id,))

        rows = cursor.fetchall()
        beneficios = []

        for row in rows:
            beneficio = Beneficio(
                id_beneficio=row[0],
                nome=row[1],
                descricao=row[2],
                criterios=row[3],
                tipo=row[4],
                valor=float(row[5])
            )
            beneficio_data = {
                "beneficio": beneficio,
                "data_inicio": row[6].isoformat() if row[6] else None
            }
            beneficios.append(beneficio_data)

        return beneficios

    except Exception as e:
        print(f"Erro ao buscar benefícios da família {id}: {e}")
        return []

    finally:
        cursor.close()
        conn.close()
