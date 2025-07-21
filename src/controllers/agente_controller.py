from fastapi import APIRouter
from models.agente_visita.agente_visita import AgenteVisita
from models.familia_beneficio.familia_beneficio import FamiliaBeneficio
from models.visita.visita import Visita
from usecases.gerenciar_agentes_de_visita.criar_agente_de_visita import criar_agente
from usecases.gerenciar_agentes_de_visita.atualizar_agente_de_visita import editar_agente
from usecases.gerenciar_agentes_de_visita.excluir_agente_de_visita import deletar_agente_por_id
from usecases.acessar_dados_pessoa_especifica.dados_especifico_pessoa import buscar_pessoa_por_nis
from usecases.visualizar_agentes.listar_agentes import listar_agente
from usecases.conceder_beneficio.conceder_beneficio import conceder_beneficio_a_familia
from usecases.remover_beneficio.remover_beneficio import remover_beneficio_da_familia
from usecases.agendar_visita.agendar_visita import cadastrar_visita

router = APIRouter()

@router.get("/")
def listar_agentes_route():
    agentes = listar_agente()
    return {"agentes": agentes}

@router.get("/buscar-pessoa/{nis}")
def buscar_pessoa_route(nis: str):
    pessoa = buscar_pessoa_por_nis(nis)
    return pessoa

@router.post("/")
def cadastrar_agente_route(agente: AgenteVisita):
    novo_agente = criar_agente(agente)
    return {"message": "Agente cadastrado com sucesso", "agente": novo_agente}

@router.put("/{id}")
def atualizar_agente_route(id: int, agente: AgenteVisita):
    editar_agente(agente, id)
    return {"message": "Agente atualizado com sucesso"}

@router.delete("/{id}")
def excluir_agente_route(id: int):
    deletar_agente_por_id(id)
    return {"message": "Agente excluído com sucesso"}

@router.post("/conceder-beneficio")
def conceder_beneficio(fb: FamiliaBeneficio):
    conceder_beneficio_a_familia(fb.id_beneficio, fb.id_familia)
    return {"message": "Benefício concedido com sucesso", "familia_beneficio": fb}

@router.delete("/remover-beneficio/{idBeneficio}/{idFamilia}")  
def remover_beneficio(idBeneficio: int, idFamilia: int):    
    remover_beneficio_da_familia(idBeneficio, idFamilia)
    return {"message": "Benefício removido da família com sucesso"} 

@router.post("/agendar-visita")
def agendar_visita_route(visita: Visita): 
    cadastrar_visita(visita)
    return {"message": "Visita agendada com sucesso", "visita": visita}