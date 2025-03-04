# Este arquivo tem funções para ler e escrever o arquivo .json que tem os usuários
import json

arquivo_json = "usuarios.json" # Caminho para o arquivo .json

# Carregar usuarios do arquivo
def carregar_usuarios():
    try:
        with open(arquivo_json, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {} # Lista vazia é retornada se o arquivo não for encontrado
    except json.JSONDecodeError:
        return {}

    
# Salvar Usuários no arquivo
def salvar_usuarios(usuarios):
    with open(arquivo_json, 'w') as f:
        json.dump(usuarios, f, indent=4)

usuarios_cadastrados = carregar_usuarios()