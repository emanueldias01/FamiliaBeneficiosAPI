from fastapi import FastAPI
from controllers import familia_controller

app = FastAPI(
    title = "GFSV API",
    description = "API para o gerenciamento de famílias em situação de vulnerabilidade"
)

app.include_router(familia_controller.router, prefix="/api/v1/familia", tags=["Família"])