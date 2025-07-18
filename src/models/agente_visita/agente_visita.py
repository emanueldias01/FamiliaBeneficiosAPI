from pydantic import BaseModel

class AgenteVisita(BaseModel):
    id_agente : int
    nome : str
    contato : str
    login : str
    senha : str