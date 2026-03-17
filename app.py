from functions import *
from classes import *


# -------------------------------------------- CLIENTES -------------------------------------------------------- #
verificar_csv_clientes()


#get clientes

@app.get("/clientes")
def listar_clientes():
    D_clientes = {}

    file_path = "Clientes.csv"

    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)

        for row in reader:
            if row[0] == 'ID' or cliente_foi_apagado(row):
                continue
            else:
                D_clientes[row[0]] = [row[1], row[2], row[3], row[4]]

    return D_clientes



# post clientes
@app.post("/clientes")
async def criar_cliente(cliente: Cliente):
    D_clientes = {}
    data = ler_clientes_csv()


    cliente = Cliente(
        id=gerar_proximo_id(data),
        nome=cliente.nome,
        sobrenome=cliente.sobrenome,
        data_de_nascimento=cliente.data_de_nascimento,
        cpf=cliente.cpf
    )

    data = adicionar_cliente(data, cliente)
    salvar_clientes_csv(data)

    file_path = "Clientes.csv"

    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)

        for row in reader:
            if row[0] == 'ID' or cliente_foi_apagado(row):
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
            if row[0] == 'ID' or cliente_foi_apagado(row):
                continue
            else:
                D_clientes[row[0]] = [row[1], row[2], row[3], row[4]]

    return D_clientes

# delete clientes
@app.delete("/clientes/{id}")
async def deletar_cliente(id: int):
    data = [
        ["ID", "NOME", "SOBRENOME", "DATA_DE_NASCIMENTO", "CPF"]
    ]

    D_clientes = {}
    file_path = "Clientes.csv"

    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == 'ID':
                continue
            else:
                data.append(row)

    cont = False
    for linha in data:
        if linha[0] == str(id):
            # manter o id e limpar os dados para ele não ser reutilizado
            linha[1] = "Cliente não existe mais!"
            linha[2] = "Cliente não existe mais!"
            linha[3] = "Cliente não existe mais!"
            linha[4] = "Cliente não existe mais!"
            cont = True

    if cont != True:
        return {"ERRO":"ID informado não existe"}

    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == 'ID' or cliente_foi_apagado(row):
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
            if row[0] == 'ID' or produto_foi_apagado(row):
                continue
            else:
                D_produtos[row[0]] = [row[1], row[2], row[3]]

    return D_produtos

# post produtos
@app.post("/produtos")
async def criar_produto(produto: Produtos):
    D_produtos = {}
    data = ler_produtos_csv()

    # gerar o id
    produto = Produtos(
        id=gerar_proximo_id(data),
        nome=produto.nome,
        fornecedor=produto.fornecedor,
        quantidade=produto.quantidade
    )

    data = adicionar_produto(data, produto)
    salvar_produtos_csv(data)

    file_path = "Produtos.csv"

    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)

        for row in reader:
            if row[0] == 'ID' or produto_foi_apagado(row):
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
            if row[0] == 'ID' or produto_foi_apagado(row):
                continue
            else:
                D_produtos[row[0]] = [row[1], row[2], row[3]]

    return D_produtos

# delete produtos
@app.delete("/produtos/{id}")
async def deletar_produto(id: int):
    data = [
        ["ID", "NOME", "FORNECEDOR", "QUANTIDADE"]
    ]

    D_produtos = {}
    file_path = "Produtos.csv"

    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == 'ID':
                continue
            else:
                data.append(row)

    cont = False
    for linha in data:
        if linha[0] == str(id):
            # manter o id e limpar os dados para ele não ser reutilizado
            linha[1] = ""
            linha[2] = ""
            linha[3] = ""
            cont = True

    if cont != True:
        return {"ERRO":"ID informado não existe"}

    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == 'ID' or produto_foi_apagado(row):
                continue
            else:
                D_produtos[row[0]] = [row[1], row[2], row[3]]

    return D_produtos


# ------------------------------------------------------------------- ORDEM DE VENDAS -------------------------------------------------------------

verificar_csv_ordemdevendas()


#get ordens

@app.get("/ordens")
def listar_ordens():
    D_ordensVendas = {}

    file_path = "OrdemDeVendas.csv"

    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)

        for row in reader:
            if row[0] == 'ID' or ordem_foi_apagada(row):
                continue
            else:
                D_ordensVendas[row[0]] = [row[1], row[2]]

    return D_ordensVendas

# post ordens
@app.post("/ordens")
async def criar_ordemVendas(ordemVendas: OrdemDeVendas):

    clientes = ler_clientes_csv()
    produtos = ler_produtos_csv()

    D_ordensVendas = {}
    data = ler_ordemdevendas_csv()

    #gerar id 
    ordemVendas = OrdemDeVendas(
        id=gerar_proximo_id(data),
        cliente=ordemVendas.cliente,
        produto=ordemVendas.produto
    )

    id_cliente = False
    id_produto = False

    for cliente in clientes: # verificaÃ§Ã£o se o cliente informado existe
        if cliente[0] == str(ordemVendas.cliente):
            id_cliente = True
            break
    if id_cliente == False:
        return {"ERRO" : "ID DO CLIENTE NÃO EXISTE"}

    for produto in produtos: # verificaÃ§Ã£o se o produto informado existe
        if produto[0] == str(ordemVendas.produto):
            id_produto = True
            break
    if id_produto != True:
        return {"ERRO" : "ID DO PRODUTO NÃO EXISTE"}

    data = adicionar_ordemdevendas(data, ordemVendas)
    salvar_ordemdevendas_csv(data)

    file_path = "OrdemDeVendas.csv"
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)

        for row in reader:
            if row[0] == 'ID' or ordem_foi_apagada(row):
                continue
            else:
                D_ordensVendas[row[0]] = [row[1], row[2]]

    return D_ordensVendas



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

            for cliente in clientes: # verificaÃ§Ã£o se o cliente informado existe
                if cliente[0] == str(ordemVendas.cliente):
                    id_cliente = True
                    linha[1] = str(ordemVendas.cliente)
                    break
            if id_cliente == False:         
                print(cliente)
                return {"ERRO" : "ID DO CLIENTE NÃO EXISTE"}
                        
            for produto in produtos: # verificaÃ§Ã£o se o produto informado existe
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
            if row[0] == 'ID' or ordem_foi_apagada(row):
                continue
            else:
                D_ordensVendas[row[0]] = [row[1], row[2]]

    return D_ordensVendas

# delete ordens
@app.delete("/ordens/{id}")
async def deletar_ordemVendas(id: int):
    data = [
        ["ID", "CLIENTE", "PRODUTO"]
    ]

    D_ordensVendas = {}
    file_path = "OrdemDeVendas.csv"

    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == 'ID':
                continue
            else:
                data.append(row)

    cont = False
    for linha in data:
        if linha[0] == str(id):
            # manter o id e limpar os dados para ele não ser reutilizado
            linha[1] = ""
            linha[2] = ""
            cont = True

    if cont != True:
        return {"ERRO":"ID informado não existe"}

    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == 'ID' or ordem_foi_apagada(row):
                continue
            else:
                D_ordensVendas[row[0]] = [row[1], row[2]]

    return D_ordensVendas





