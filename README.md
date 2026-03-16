# api-supermarket

API REST para gerenciamento de clientes, produtos e ordens de venda, desenvolvida com **FastAPI**. Os dados são armazenados em arquivos **CSV** locais.

---

## Como rodar

### Pré-requisitos

- Python 3.8+

### Instalar dependências

```bash
pip install fastapi pydantic uvicorn
```

### Iniciar a aplicação

```bash
uvicorn app:app --reload
```

A API estará disponível em `http://127.0.0.1:8000`.

A documentação interativa (Swagger) gerada automaticamente pelo FastAPI estará em `http://127.0.0.1:8000/docs`.

---

## Endpoints

### Clientes

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/clientes` | Lista todos os clientes |
| POST | `/clientes` | Adiciona um novo cliente |
| PUT | `/clientes` | Atualiza os dados de um cliente existente |
| DELETE | `/clientes/{id}` | Remove um cliente pelo ID |

### Produtos

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/produtos` | Lista todos os produtos |
| POST | `/produtos` | Adiciona um novo produto |
| PUT | `/produtos` | Atualiza os dados de um produto existente |
| DELETE | `/produtos/{id}` | Remove um produto pelo ID |

### Ordens de Venda

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/ordens` | Lista todas as ordens de venda |
| POST | `/ordens` | Cria uma nova ordem de venda |
| PUT | `/ordens` | Atualiza uma ordem de venda existente |
| DELETE | `/ordens/{id}` | Remove uma ordem de venda pelo ID |

---

## Armazenamento

Os dados são salvos nos seguintes arquivos CSV na raiz do projeto:

- `Clientes.csv`
- `Produtos.csv`
- `OrdemDeVendas.csv`

Os arquivos são criados automaticamente na primeira execução caso não existam.
