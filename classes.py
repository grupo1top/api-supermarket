from functions import *

class Cliente(BaseModel):
    id: int = 0
    nome: str
    sobrenome: str 
    data_de_nascimento: date
    cpf: str


class Produtos(BaseModel):
    id: int = 0
    nome: str 
    fornecedor: str
    quantidade: int


class OrdemDeVendas(BaseModel):
    id: int = 0
    cliente: int
    produto: int
