from pydantic import BaseModel
from datetime import date

class Visita(BaseModel):
    id_agente : int
    data : date
    hora : str
    status : str