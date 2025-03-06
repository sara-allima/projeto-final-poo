import json

def importar_nota_json(arquivo_importado, arquivo_destino="notas_fiscais.json"):
    """ Lê uma nota fiscal de um arquivo JSON e a salva no banco de notas fiscais, se não for duplicada """
    try:
        # Lendo a nota fiscal do arquivo importado
        with open(arquivo_importado, "r", encoding="utf-8") as f:
            nota = json.load(f)  # Carrega a nota fiscal importada

        # Lendo o arquivo de destino para não sobrescrever os dados existentes
        try:
            with open(arquivo_destino, "r", encoding="utf-8") as f:
                notas_existentes = json.load(f)  # Carrega as notas já salvas
        except (FileNotFoundError, json.JSONDecodeError):
            notas_existentes = []  # Se o arquivo não existir, cria uma lista nova

        # Normalizando os dados (removendo espaços extras) e fazendo a comparação
        for nota_existente in notas_existentes:
            if (str(nota_existente.get("numero")).strip() == str(nota.get("numero")).strip() and
                str(nota_existente.get("serie")).strip() == str(nota.get("serie")).strip()):
                print(f"A nota fiscal número {nota['numero']} da série {nota['serie']} já foi importada anteriormente.")
                return  # Se a nota já foi importada, não a adiciona novamente

        # Se não encontrar a nota no arquivo, adiciona a nova nota fiscal
        notas_existentes.append(nota)

        # Salva a lista atualizada no arquivo JSON
        with open(arquivo_destino, "w", encoding="utf-8") as f:
            json.dump(notas_existentes, f, indent=4, ensure_ascii=False)

        print(f"Nota fiscal número {nota['numero']} da série {nota['serie']} importada com sucesso!")

    except Exception as e:
        print(f"Erro ao importar a nota fiscal: {e}")
