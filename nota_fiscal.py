import json
from datetime import datetime

def adicionar_nota_manual():
    print("Adicionar Nota Fiscal Manualmente")

    # Solicitar dados da nota
    data_emissao = input("Digite a data de emissão da nota (dd/mm/aaaa): ")
    hora_emissao = input("Digite a hora de emissão da nota (hh:mm): ")
    numero = int(input("Digite o número da nota fiscal: "))
    serie = int(input("Digite a série da nota fiscal: "))

    produtos = []
    while True:
        nome_produto = input("Digite o nome do produto (ou 'fim' para terminar): ")
        if nome_produto.lower() == 'fim':
            break
        valor_produto = float(input("Digite o valor do produto: "))
        quantidade_produto = int(input("Digite a quantidade do produto: "))
        
        produtos.append({
            "nome": nome_produto,
            "valor": valor_produto,
            "quantidade": quantidade_produto
        })

    # Criar o dicionário para armazenar a nota fiscal
    nota_fiscal = {
        "data_emissao": data_emissao,
        "hora_emissao": hora_emissao,
        "numero": numero,
        "serie": serie,
        "produtos": produtos
    }

    # Carregar as compras já existentes
    compras = carregar_compras()  # Função que carrega as compras do arquivo JSON

    # Adicionar a nova nota fiscal à lista de compras
    compras.append(nota_fiscal)

    # Salvar as compras de volta no arquivo JSON
    with open("notas fiscais/notas_fiscais.json", "w", encoding="utf-8") as f:
        json.dump(compras, f, ensure_ascii=False, indent=4)

    print("Nota fiscal adicionada com sucesso!\n")

def carregar_compras(arquivo="notas fiscais/notas_fiscais.json"):
    """Carregar as compras do arquivo JSON."""
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
