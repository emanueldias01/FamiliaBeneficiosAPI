from fastapi import FastAPI
from controllers import familia_controller
from controllers import beneficio_controller
from controllers import agente_controller
from controllers import relatorio_controller

app = FastAPI(
    title = "GFSV API",
    description = "API para o gerenciamento de famílias em situação de vulnerabilidade"
)

app.include_router(familia_controller.router, prefix="/api/v1/familia", tags=["Família"])
app.include_router(beneficio_controller.router, prefix="/api/v1/beneficio", tags=["Benefício"])
app.include_router(agente_controller.router, prefix="/api/v1/agente", tags=["Agente"])
app.include_router(relatorio_controller.router, prefix="/api/v1/relatorio", tags=["Relatório"])

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API GFSV!"}