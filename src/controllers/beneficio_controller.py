from fastapi import APIRouter
from models.beneficio.beneficio import Beneficio
from models.familia_beneficio.familia_beneficio import FamiliaBeneficio
from usecases.gerenciar_beneficios.cadastrar_beneficio import criar_beneficio
from usecases.gerenciar_beneficios.atualizar_beneficio import editar_beneficio
from usecases.gerenciar_beneficios.excluir_beneficio import deletar_beneficio_por_id
from usecases.visualizar_beneficios.listar_beneficios import listar_beneficios
from usecases.acessa_dados_beneficio_especifico.dados_beneficio_especifico import busca_beneficio_por_id
from usecases.conceder_beneficio.conceder_beneficio import conceder_beneficio_a_familia
from usecases.remover_beneficio.remover_beneficio import remover_beneficio_da_familia

router = APIRouter()

router.get("/")
def listar_beneficios():
    beneficios = listar_beneficios()
    return {"beneficios": beneficios}

@router.get("/{id}")
def obter_beneficio(id: int):
    beneficio = busca_beneficio_por_id(id)
    return beneficio

@router.post("/")
def cadastrar_beneficio(b: Beneficio):
    criar_beneficio(b)
    return {"message": "Benefício cadastrado com sucesso", "beneficio": b}

@router.put("/{id}")
def atualizar_beneficio(id: int, b: Beneficio):
    editar_beneficio(b, id)
    return {"message": "Benefício atualizado com sucesso"}

@router.delete("/{id}") 
def excluir_beneficio(id: int):
    deletar_beneficio_por_id(id)
    return {"message": "Benefício deletado com sucesso"}