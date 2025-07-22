from fastapi import FastAPI
from controllers import familia_controller
from controllers import beneficio_controller
from controllers import agente_controller
from controllers import relatorio_controller
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title = "GFSV API",
    description = "API para o gerenciamento de famílias em situação de vulnerabilidade"
)

origins = [
    "*"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(familia_controller.router, prefix="/api/v1/familia", tags=["Família"])
app.include_router(beneficio_controller.router, prefix="/api/v1/beneficio", tags=["Benefício"])
app.include_router(agente_controller.router, prefix="/api/v1/agente", tags=["Agente"])
app.include_router(relatorio_controller.router, prefix="/api/v1/relatorio", tags=["Relatório"])

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API GFSV!"}