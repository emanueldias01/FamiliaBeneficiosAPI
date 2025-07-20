from fastapi import APIRouter
from models.relatorio.relatorio import Relatorio
from usecases.cadastrar_relatorio_de_visita.cadastrar_relatorio_de_visita import cadastrar_relatorio
from usecases.visualizar_historico_de_relatorio_familiar.listar_historico_relatorio import buscar_historico_relatorios_familiar
from usecases.visualizar_historico_de_relatorios_do_agente import listar_historico_de_relatorios_do_agente
from usecases.visualizar_historico_de_visita_do_agente import listar_historico_de_visita_do_agente


router = APIRouter()

@router.get("/historico-familia/{idFamilia}")
def historico_relatorio_familia(idFamilia: int):
    relatorios = buscar_historico_relatorios_familiar(idFamilia)
    return {"relatorios": relatorios}

@router.get("/historico-agente/{idAgente}")
def historico_relatorio_agente(idAgente: int):
    relatorios = listar_historico_de_relatorios_do_agente(idAgente)
    return {"relatorios": relatorios}

@router.get("/historico-visitas-agente/{idAgente}")
def historico_visitas_agente(idAgente: int):
    visitas = listar_historico_de_visita_do_agente(idAgente)
    return {"visitas": visitas}

@router.post("/")
def cadastrar_relatorio_route(relatorio: Relatorio):
    cadastrar_relatorio(relatorio)
    return {"message": "Relatório de visita cadastrado com sucesso", "relatorio": relatorio}