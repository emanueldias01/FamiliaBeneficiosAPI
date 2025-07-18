from pydantic import BaseModel

class RelatorioVacinacaoFamilia(BaseModel):
    id_relatorio : int
    vacinacao_familia : str