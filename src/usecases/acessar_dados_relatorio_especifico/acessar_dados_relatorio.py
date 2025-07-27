from db.connection import get_cursor_and_connection

def buscar_relatorio(id : int):
    cursor, conn = get_cursor_and_connection()
    try:
        cursor.execute("""
                       SELECT rv.vacinacaoFamilia, ro.observacoes, rp.pesoFamilia 
                       FROM relatorio r
                       INNER JOIN relatorio_vacinacaoFamilia rv ON r.idrelatorio = rv.idrelatorio
                       INNER JOIN relatorio_observacoes ro ON r.idrelatorio = ro.idrelatorio
                       INNER JOIN relatorio_pesoFamilia rp ON r.idrelatorio = rp.idrelatorio
                       WHERE r.idrelatorio = %s""",(id,))
        row = cursor.fetchall()

        print(row)
        if row is None:
            return None
        else:
            row = row[0] 
        relatorio = {
            "id": id,
            "vacinacaoFamilia": row[0],
            "observacoes": row[1],
            "pesoFamilia": row[2]
        }
        
        return relatorio
    
    except Exception as e:
        print(f'Erro ao buscar relatorio: {e}')
    
    finally:
        cursor.close()
        conn.close()
        