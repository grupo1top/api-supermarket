from fastapi import FastAPI
import os
import csv

app = FastAPI

file_path = "Clientes.csv"
file_path = "Produtos.csv"
file_path = "OrdemDeVendas"

if not os.path.exists(file_path):    
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        data = [
            ["ID", "NOME"]
        ]
        writer = csv.writer(file)
        writer.writerows(data)
else:
    print('O arquivo já existe!')

