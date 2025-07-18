from pydantic import BaseModel

class Familia(BaseModel):
    id_familia : int
    nome : str
    rua : str
    bairro : str
    cidade : str
    telefone : str
    renda : float
    numero_membros : int