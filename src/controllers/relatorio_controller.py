from fastapi import APIRouter
from models.relatorio.relatorio import Relatorio
from usecases.cadastrar_relatorio_de_visita.cadastrar_relatorio_de_visita import cadastrar_relatorio
from usecases.visualizar_historico_de_relatorio_familiar.listar_historico_relatorio import buscar_historico_relatorios_familiar
from usecases.visualizar_historico_de_relatorios_do_agente.listar_historico_de_relatorios_do_agente import listar_historico_relatorios_por_agente
from usecases.visualizar_historico_de_visita_do_agente.listar_historico_de_visita_do_agente import listar_historico_visitas_agente
from usecases.cadastrar_relatorio_de_visita.cadastrar_relatorio_de_visita import TipoRelatorio;
from usecases.acessar_dados_relatorio_especifico.acessar_dados_relatorio import buscar_relatorio 

router = APIRouter()

@router.get("/historico-familia/{idFamilia}")
def historico_relatorio_familia(idFamilia: int):
    relatorio = buscar_historico_relatorios_familiar(idFamilia)
    return relatorio

@router.get("/historico-agente/{idagente}")
def historico_relatorio_agente(idagente: int):
    relatorio = listar_historico_relatorios_por_agente(idagente)
    return relatorio

@router.get("/historico-visitas-agente/{idagente}")
def historico_visitas_agente(idagente: int):
    visitas = listar_historico_visitas_agente(idagente)
    return {"visitas": visitas}

@router.get("/{idrelatorio}")
def acessar_relatorio(idrelatorio: int):
    relatorio = buscar_relatorio(idrelatorio)
    return {"relatorio": relatorio}

@router.post("/")
def cadastrar_relatorio_route(relatorio: TipoRelatorio):
    id_relatorio = cadastrar_relatorio(relatorio)
    
    return {"message": "Relatório de visita cadastrado com sucesso", "id_relatorio": id_relatorio, "relatorio": relatorio}