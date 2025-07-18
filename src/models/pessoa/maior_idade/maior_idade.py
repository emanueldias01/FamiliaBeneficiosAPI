from pydantic import BaseModel

class MaiorIdade(BaseModel):
    nis : str
    renda : float
    ocupacao : str