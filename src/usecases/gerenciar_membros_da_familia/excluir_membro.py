from db.connection import get_cursor_and_connection

def deletar_pessoa_por_nis(nis : str):
    cursor, conn = get_cursor_and_connection()

    try:
        # 1. Buscar a renda e o id da família da pessoa
        cursor.execute('SELECT renda, idfamilia FROM pessoa WHERE nis = %s', (nis,))
        result = cursor.fetchone()
        
        if not result:
            print("Pessoa não encontrada.")
            return
        
        renda_pessoa, id_familia = result

        # 2. Subtrair a renda da pessoa da família (se houver)
        if renda_pessoa is not None:
            cursor.execute('''
                UPDATE familia
                SET renda = renda - %s
                WHERE idfamilia = %s
            ''', (renda_pessoa, id_familia))

        # 3. Reduzir o número de membros da família
        cursor.execute('''
            UPDATE familia
            SET numeroMembros = GREATEST(COALESCE(numeroMembros, 1) - 1, 0)
            WHERE idfamilia = %s
        ''', (id_familia,))

        # 4. Excluir a pessoa
        cursor.execute('DELETE FROM pessoa WHERE nis = %s', (nis,))

        conn.commit()

    except Exception as e:
        conn.rollback()
        print(f"Erro ao excluir membro: {e}")
    finally:
        cursor.close()
        conn.close()