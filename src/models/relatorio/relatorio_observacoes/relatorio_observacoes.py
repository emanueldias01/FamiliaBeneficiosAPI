from pydantic import BaseModel

class RelatorioObservacoes(BaseModel):
    id_relatorio : int
    observacoes : str