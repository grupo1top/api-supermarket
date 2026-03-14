# as funções ficaram armazenadas aqui #

from fastapi import FastAPI
import os
import csv
from pydantic import BaseModel
from datetime import date  # tipo data

app = FastAPI()
# ---------------------------------------------------------------------------------- #
                # FUNÇÕES PARA VERIFICAR O CSV (SE JÁ ESTÁ CRIADO / CRIAR) #

def verificar_csv_clientes():

    file_path = "Clientes.csv"

    if not os.path.exists(file_path):
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            data = [
                ["ID", "NOME", "SOBRENOME", "DATA_DE_NASCIMENTO", "CPF"]
            ]
            writer = csv.writer(file)
            writer.writerows(data)

    else:
        print("O arquivo já existe!")


def verificar_csv_produtos():

    file_path = "Produtos.csv"

    if not os.path.exists(file_path):
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            data = [
                ["ID", "NOME", "FORNECEDOR", "QUANTIDADE"]
            ]
            writer = csv.writer(file)
            writer.writerows(data)

    else:
        print("O arquivo já existe!")


def verificar_csv_ordemdevendas():

    file_path = "OrdemDeVendas.csv"

    if not os.path.exists(file_path):
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            data = [
                ["ID", "CLIENTE", "PRODUTO"]
            ]
            writer = csv.writer(file)
            writer.writerows(data)

    else:
        print("O arquivo já existe!")

                # FUNÇÕES PARA VERIFICAR O CSV (SE JÁ ESTÁ CRIADO / CRIAR) #
# ---------------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------------- #
                # FUNÇÕES PARA LER O CSV E PULAR O CABEÇALHO #

def ler_clientes_csv():

    file_path = "Clientes.csv"
    data = [["ID", "NOME", "SOBRENOME", "DATA_DE_NASCIMENTO", "CPF"]]

    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)

        for row in reader:
            if row[0] == 'ID':
                continue
            data.append(row)

    return data


def ler_produtos_csv():

    file_path = "Produtos.csv"
    data = [["ID", "NOME", "FORNECEDOR", "QUANTIDADE"]]

    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)

        for row in reader:
            if row[0] == 'ID':
                continue
            data.append(row)

    return data

def ler_ordemdevendas_csv():

    file_path = "OrdemDeVendas.csv"
    data = [["ID", "CLIENTE", "PRODUTO"]]

    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)

        for row in reader:
            if row[0] == 'ID':
                continue
            data.append(row)

    return data

                # FUNÇÕES PARA LER O CSV E PULAR O CABEÇALHO #
# ---------------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------------- #
                # ADICIONAR NOVOS CLIENTES, ORDEM, PRODUTOS #

def adicionar_cliente(data, Cliente):
    novo = [Cliente.id, Cliente.nome, Cliente.sobrenome, Cliente.data_de_nascimento, Cliente.cpf ]
    data.append(novo)
    return data

def adicionar_produto(data, Produtos):
    novo = [Produtos.id, Produtos.nome, Produtos.fornecedor, Produtos.quantidade]
    data.append(novo)
    return data

def adicionar_ordemdevendas(data, OrdemDeVendas):
    novo = [OrdemDeVendas.id, OrdemDeVendas.cliente, OrdemDeVendas.produto]
    data.append(novo)
    return data
                # ADICIONAR NOVOS CLIENTES, ORDEM, PRODUTOS #
# ---------------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------------- #
                # SALVAR ALTERAÇÕES NO CSV - APÓS ADICIONAR NOVOS #

def salvar_clientes_csv(data):

    file_path = "Clientes.csv"

    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)


def salvar_produtos_csv(data):

    file_path = "Produtos.csv"

    with open(file_path, mode="w",newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def salvar_ordemdevendas_csv(data):

    file_path = "OrdemDeVendas.csv"

    with open(file_path, mode="w",newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)

                # SALVAR ALTERAÇÕES NO CSV - APÓS ADICIONAR NOVOS #
# ---------------------------------------------------------------------------------- #


# ---------------------------------------------------------------------------------- #
                        # VERIFICAR SE UM ID JÁ EXISTE #  

def id_cliente_existe(data, Cliente_id):
    for row in data:
        if row[0] == Cliente_id:
            return True
    return False

def id_produto_existe(data, Produto_id):
    for row in data:
        if row[0] == Produto_id:
            return True
    return False

def id_ordemdevenda_existe(data, OrdemDeVenda_id):
    for row in data:
        if row[0] == OrdemDeVenda_id:
            return True
    return False 

                        # VERIFICAR SE UM ID JÁ EXISTE #
# ---------------------------------------------------------------------------------- #





