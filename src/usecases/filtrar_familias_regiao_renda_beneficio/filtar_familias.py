from db.connection import get_cursor_and_connection
from models.familia.familia import Familia
from pydantic import BaseModel

class FiltroFamilia(BaseModel):
    bairro : str
    renda : float
    beneficioId : int

def filtar_familias_beneficios(filtro : FiltroFamilia):
    cursor, conn = get_cursor_and_connection()
    familias = []

    try:
        cursor.execute('''
            SELECT f.*
            FROM familia f
            JOIN tem t ON f.idFamilia = t.idFamilia
            WHERE f.bairro = %s AND f.renda = %s AND t.idBeneficio = %s
        ''', (filtro.bairro, filtro.renda, filtro.beneficioId))

        result = cursor.fetchall()

        for row in result:
            familia = {
                "idFamilia": row[0],
                "nome": row[1],
                "rua": row[2],
                "numero": row[3],
                "bairro": row[4],
                "cidade": row[5],
                "telefone": row[6],
                "renda": float(row[7]),
                "numeroMembros": row[8]
            }
            familias.append(familia)

        return familias

    except Exception as e:
        print(f"Erro ao filtrar famílias: {e}")
        return []
    finally:
        cursor.close()
        conn.close()