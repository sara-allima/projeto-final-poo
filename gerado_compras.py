import random
import json
from datetime import datetime, timedelta

# Função para gerar uma data aleatória dentro de um intervalo
def gerar_data_aleatoria(inicio, fim):
    return inicio + timedelta(days=random.randint(0, (fim - inicio).days))

# Função para gerar compras aleatórias
def gerar_compras(quantidade):
    # Produtos possíveis
    produtos = [
        "Produto A", "Produto B", "Produto C", "Produto D", "Produto E",
        "Produto F", "Produto G", "Produto H", "Produto I", "Produto J"
    ]
    
    # Intervalo de datas (do ano passado até hoje)
    data_fim = datetime.today()
    data_inicio = datetime(data_fim.year - 1, 1, 1)
    
    compras = []
    
    for _ in range(quantidade):
        data_emissao = gerar_data_aleatoria(data_inicio, data_fim).strftime("%d/%m/%Y")
        hora_emissao = f"{random.randint(0, 23):02}:{random.randint(0, 59):02}"
        numero = random.randint(100000, 999999)
        serie = random.randint(1, 5)
        
        # Gerar produtos aleatórios
        num_produtos = random.randint(1, 5)
        produtos_da_compra = []
        for _ in range(num_produtos):
            nome_produto = random.choice(produtos)
            valor_produto = round(random.uniform(10, 500), 2)
            quantidade_produto = random.randint(1, 10)
            produtos_da_compra.append({
                "nome": nome_produto,
                "valor": valor_produto,
                "quantidade": quantidade_produto
            })
        
        # Adicionar a compra à lista
        compras.append({
            "data_emissao": data_emissao,
            "hora_emissao": hora_emissao,
            "numero": numero,
            "serie": serie,
            "produtos": produtos_da_compra
        })
    
    return compras

# Gerar 100 compras aleatórias e salvar em um arquivo JSON
compras = gerar_compras(100)

# Salvar no arquivo JSON
with open("notas_fiscais_geradas.json", "w", encoding="utf-8") as f:
    json.dump(compras, f, indent=4, ensure_ascii=False)

print("Arquivo JSON com 100 compras geradas com sucesso!")
