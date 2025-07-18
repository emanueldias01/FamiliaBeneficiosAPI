from pydantic import BaseModel
from enum import Enum
from datetime import date


class GeneroEnum(str, Enum):
    MASCULINO = "M"
    FEMININO = "F"
    OUTRO = "O"

class Pessoa(BaseModel):
    nis : str
    nome : str
    idade : int
    dataNascimento : date
    genero : GeneroEnum
    idFamilia : int