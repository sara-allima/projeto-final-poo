import json

class Cadastro:
    def __init__(self, nome, senha, cpf, data_nascimento, local_residencia, num_telefone, email):
        self.__nome = nome
        self.__senha = senha
        self.__cpf = cpf
        self.__data_nascimento = data_nascimento
        self.__local_residencia = local_residencia
        self.__num_telefone = num_telefone
        self.__email = email

    def to_dict(self):
        """Converte os dados do usuário para dicionário."""
        return {
            "nome": self.__nome,
            "senha": self.__senha,
            "cpf": self.__cpf,
            "data_nascimento": self.__data_nascimento,
            "local_residencia": self.__local_residencia,
            "num_telefone": self.__num_telefone,
            "email": self.__email  # Adicionando o e-mail ao dicionário
        }

    def salvar_em_json(self, arquivo="cadastros.json"):
        """Salva os dados do usuário em um arquivo JSON."""
        try:
            with open(arquivo, "r", encoding="utf-8") as f:
                cadastros = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            cadastros = []

        cadastros.append(self.to_dict())

        # Escreve os dados no arquivo, com encoding UTF-8
        with open(arquivo, "w", encoding="utf-8") as f:
            json.dump(cadastros, f, indent=4, ensure_ascii=False)

    @staticmethod
    def carregar_cadastros(arquivo="cadastros.json"):
        """Carrega os cadastros existentes do arquivo JSON."""
        try:
            with open(arquivo, "r", encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
