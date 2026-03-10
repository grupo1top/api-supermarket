from pydantic import BaseModel
from datetime import date # tipo data

# classe base cliente 
class Cliente(BaseModel):
    id: int
    nome: str
    Sobrenome: str 
    data_de_nascimento: date
    cpf: str


class Produtos(BaseModel):
    id: int
    nome: str 
    fornecedor: str
    quantidade: int


class ordemVendas(BaseModel):
    id: int
    cliente: Cliente.id
    produto: Produtos.id 