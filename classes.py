from functions import *

class Cliente(BaseModel):
    id: int
    nome: str
    sobrenome: str 
    data_de_nascimento: date
    cpf: str


class Produtos(BaseModel):
    id: int
    nome: str 
    fornecedor: str
    quantidade: int


class OrdemDeVendas(BaseModel):
    id: int
    cliente: Cliente.id
    produto: Produtos.id 