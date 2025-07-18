from pydantic import BaseModel

class Beneficio(BaseModel):
    id_beneficio : int
    nome : str
    descricao : str
    criterios : str
    tipo : str
    valor : float