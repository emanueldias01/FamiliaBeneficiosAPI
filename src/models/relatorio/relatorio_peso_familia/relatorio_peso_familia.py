from pydantic import BaseModel

class RelatorioPesoFamilia(BaseModel):
    id_relatorio : int
    peso_familia : float