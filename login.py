import json

class Login:
    def __init__(self, email: str, senha: str):
        self.__email = email
        self.__senha = senha

    def validar_usuario(self, arquivo="cadastros.json"):
        """Verifica se o e-mail e senha existem no arquivo JSON."""
        try:
            with open(arquivo, "r", encoding="utf-8") as f:
                cadastros = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return False  # Se o arquivo não existir ou estiver corrompido, login falha

        for usuario in cadastros:
            # Verifica e-mail e senha
            if usuario["email"] == self.__email and usuario["senha"] == self.__senha:
                return True  # E-mail e senha corretos

        return False  # E-mail ou senha incorretos
