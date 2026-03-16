from functions import *
from classes import *

# -------------------------------------------- CLIENTES -------------------------------------------------------- #
verificar_csv_clientes()



# post clientes
@app.post("/clientes")
async def criar_cliente(cliente: Cliente):
    D_clientes = {}
    data = ler_clientes_csv()

    if id_cliente_existe(data, str(cliente.id)):
        return {"ERRO" : "ID JÁ EXISTE"}

    data = adicionar_cliente(data, cliente)
    salvar_clientes_csv(data)

    file_path = "Clientes.csv"

    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)

        for row in reader:
            if row[0] == 'ID':
                continue
            else:
                D_clientes[row[0]] = [row[1], row[2], row[3], row[4]]

    return D_clientes

# put clientes 
@app.put("/clientes")
async def atualizar_cliente(cliente: Cliente):
    D_clientes = {}
    encontrar_id = False
    #abrir o arquivo em modo leitura
    data = ler_clientes_csv()
    #percorrer ele até achar o id informado 
    for linha in data:
        if linha[0] == str(cliente.id):
            encontrar_id = True
            #quando achar substituir o nome
            linha[1] = cliente.nome
            linha[2] = cliente.sobrenome
            linha[3] = str(cliente.data_de_nascimento)
            linha[4] = cliente.cpf
    if encontrar_id == False:
        return {"ERRO" : "ID NÃO ENCONTRADO"}
    # reescrever no arquivo 
    salvar_clientes_csv(data)
    # ler o arquivo dnv para retornar o novo dicionário

    file_path = "Clientes.csv"

    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)

        for row in reader:
            if row[0] == 'ID':
                continue
            else:
                D_clientes[row[0]] = [row[1], row[2], row[3], row[4]]

    return D_clientes

# delete clientes
@app.delete("/clientes/{id}")
async def deletar_cliente(id: int):
    D_clientes = {}
    encontrar_id = False

    #abrir o arquivo em modo leitura
    data = ler_clientes_csv()

    #percorrer ele até achar o id informado
    for linha in data:
        if linha[0] == str(id):
            encontrar_id = True
            data.remove(linha)
            break

    if encontrar_id == False:
        return {"ERRO" : "ID NÃO ENCONTRADO"}

    # reescrever no arquivo
    salvar_clientes_csv(data)

    # ler o arquivo dnv para retornar o novo dicionário
    file_path = "Clientes.csv"

    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)

        for row in reader:
            if row[0] == 'ID':
                continue
            else:
                D_clientes[row[0]] = [row[1], row[2], row[3], row[4]]

    return D_clientes






# ----------------------------------------------------- PRODUTOS -------------------------------------------------------------- #

verificar_csv_produtos()



#get produtos

@app.get("/produtos")
def listar_produtos():
    D_produtos = {}

    file_path = "Produtos.csv"

    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)

        for row in reader:
            if row[0] == 'ID':
                continue
            else:
                D_produtos[row[0]] = [row[1], row[2], row[3]]

    return D_produtos


# put produtos
@app.put("/produtos")
async def atualizar_produto(produto: Produtos):
    D_produtos = {}
    encontrar_id = False
    #abrir o arquivo em modo leitura
    data = ler_produtos_csv()
    #percorrer ele até achar o id informado 
    for linha in data:
        if linha[0] == str(produto.id):
            encontrar_id = True
            #quando achar substituir o nome
            linha[1] = produto.nome
            linha[2] = produto.fornecedor
            linha[3] = str(produto.quantidade)
    if encontrar_id == False:
        return {"ERRO" : "ID NÃO ENCONTRADO"}
    # reescrever no arquivo 
    salvar_produtos_csv(data)
    # ler o arquivo dnv para retornar o novo dicionário

    file_path = "Produtos.csv"

    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)

        for row in reader:
            if row[0] == 'ID':
                continue
            else:
                D_produtos[row[0]] = [row[1], row[2], row[3]]

    return D_produtos

# ------------------------------------------------------------------- ORDEM DE VENDAS -------------------------------------------------------------

verificar_csv_ordemdevendas()

@app.put("/ordens")
async def atualizar_ordemVendas(ordemVendas: OrdemDeVendas):

    clientes = ler_clientes_csv()
    produtos = ler_produtos_csv()

    D_ordensVendas = {}

    encontrar_id = False
    id_cliente = False
    id_produto = False

    #abrir o arquivo em modo leitura
    data = ler_ordemdevendas_csv()

    #percorrer ele até achar o id informado 
    for linha in data:
        if linha[0] == str(ordemVendas.id):
            print(linha)
            encontrar_id = True

            for cliente in clientes: # verificação se o cliente informado existe
                if cliente[0] == str(ordemVendas.cliente):
                    id_cliente = True
                    linha[1] = str(ordemVendas.cliente)
                    break
            if id_cliente == False:         
                print(cliente)
                return {"ERRO" : "ID DO CLIENTE NÃO EXISTE"}
                        
            for produto in produtos: # verificação se o produto informado existe
                if produto[0] == str(ordemVendas.produto):
                    id_produto = True
                    linha[2] = str(ordemVendas.produto)
                    break
            if id_produto != True:
                    return {"ERRO" : "ID DO PRODUTO NÃO EXISTE"}

    if encontrar_id == False:
        return {"ERRO" : "ID NÃO ENCONTRADO"}
    
    # reescrever no arquivo 
    salvar_ordemdevendas_csv(data)

    # ler o arquivo dnv para retornar o novo dicionário
    file_path = "OrdemDeVendas.csv"

    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)

        for row in reader:
            if row[0] == 'ID':
                continue
            else:
                D_ordensVendas[row[0]] = [row[1], row[2]]

    return D_ordensVendas

