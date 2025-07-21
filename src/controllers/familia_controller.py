from fastapi import APIRouter
from models.familia.familia import Familia
from usecases.gerenciar_familias.cadastrar_familia import criar_familia
from usecases.visualizar_familias.listar_familias import lista_familias_cadastradas
from usecases.gerenciar_familias.atualizar_familia import edita_familia
from usecases.gerenciar_familias.excluir_familia import deletar_familia_por_id
from usecases.acessar_dados_familia_especifica.dados_especifico_familia import busca_familia_por_id
from usecases.filtrar_familias_regiao_renda_beneficio.filtar_familias import filtar_familias_beneficios
from usecases.visualizar_beneficios_recebidos.listar_beneficios_rebebidos import vizualizar_beneficios_recebidos_por_familia_id
from usecases.visualizar_membros_da_familia.listar_membros_da_familia import listar_membros_familia
from usecases.gerenciar_membros_da_familia.cadastrar_membro import cria_pessoa_membro_familia
from models.pessoa.pessoa import Pessoa
from usecases.filtrar_familias_regiao_renda_beneficio.filtar_familias import FiltroFamilia

router = APIRouter()

@router.get("/")
def familia():
    familias = lista_familias_cadastradas()
    return {"familias": familias}  

@router.get("/{id}")
def familia(id : int):
    familia = busca_familia_por_id(id)
    return familia  

@router.post("/")
def familia(f : Familia):
    familia = criar_familia(f)
    return {"message": "Família cadastrada com sucesso", "familia": familia}  

@router.put("/{id}")
def familia(id : int, f : Familia):
    edita_familia(f, id)
    return {"message": "Família atualizada com sucesso"} 

@router.delete("/{id}")
def familia(id : int):
    deletar_familia_por_id(id)
    return {"message": "Família deletada com sucesso"} 

@router.get("/filtrar")
def filtrar_familias(filtro : FiltroFamilia):
    familias = filtar_familias_beneficios(filtro)
    return {"familias": familias}
    
@router.get("/beneficios/{id}")
def beneficios_recebidos(id: int):
    beneficios = vizualizar_beneficios_recebidos_por_familia_id(id)
    return {"beneficios": beneficios}

@router.get("/membros/{id}")
def membros_familia(id: int):
    membros = listar_membros_familia(id)
    return {"membros": membros}

@router.post("/cadastrarMembro/{idFamilia}")
def cadastrar_membro_familia(idFamilia : int, p : Pessoa):
    cria_pessoa_membro_familia(p, idFamilia)
    return {"message" : "pessoa cadastrada com sucesso!"}