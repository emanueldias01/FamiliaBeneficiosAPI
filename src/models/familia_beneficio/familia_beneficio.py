from pydantic import BaseModel
from datetime import date

class FamiliaBeneficio(BaseModel):
    id_familia : int
    id_beneficio : int
    data_inicio : date