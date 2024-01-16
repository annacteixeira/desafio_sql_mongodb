from pymongo import MongoClient


# Conectar ao MongoDB Atlas


client = MongoClient("sua-string-de-conexao-do-mongodb-atlas")


# Criar um banco de dados


banco_de_dados = client["nome-do-seu-banco"]


# Criar uma coleção


colecao = banco_de_dados["bank"]


# Inserir documentos


documento_cliente1 = {
    "id": 1,
    "nome": "Cliente 1",
    "cpf": "123456789",
    "endereco": "Endereco 1",
    "contas": [
        {
            "id": b'1',
            "tipo": "Corrente",
            "agencia": "001",
            "num": 123,
            "saldo": 1000.00
        }
    ]
}


colecao.insert_one(documento_cliente1)


# Recuperar informações


resultado = colecao.find_one({"nome": "Cliente 1"})
print("Cliente 1:")
print(f"ID: {resultado['id']}, Nome: {resultado['nome']}, CPF: {resultado['cpf']}")


contas_cliente1 = resultado['contas']
print("\nContas:")
for conta in contas_cliente1:
    print(f"ID: {conta['id']}, Tipo: {conta['tipo']}, Agência: {conta['agencia']}, Número: {conta['num']}, Saldo: {conta['saldo']}")
