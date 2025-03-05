import json

def importar_nota_json(arquivo_importado, arquivo_destino="notas_fiscais.json"):
    """ Lê uma nota fiscal de um arquivo JSON e a salva no banco de notas fiscais """
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

        # Adiciona a nova nota fiscal ao banco de notas existentes
        notas_existentes.append(nota)

        # Salva a lista atualizada no arquivo JSON
        with open(arquivo_destino, "w", encoding="utf-8") as f:
            json.dump(notas_existentes, f, indent=4, ensure_ascii=False)

        print(f"Nota fiscal {nota['numero']} importada com sucesso!")

    except Exception as e:
        print(f"Erro ao importar a nota fiscal: {e}")

    finally:
        # Fecha o arquivo importado
        f.close()