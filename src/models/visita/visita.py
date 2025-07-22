from pydantic import BaseModel
from datetime import date

class Visita(BaseModel):
    id_agente : int
    id_familia : int
    id_relatorio : int
    data : date
    hora : str
    status : str