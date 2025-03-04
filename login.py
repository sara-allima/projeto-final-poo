from carregar_e_salvar_usuarios import *

# Funções 
def pedir_email():
    email = str(input('Digite seu email: '))
    return email
def pedir_senha():
    senha = str(input('Digite sua senha: '))
    return senha

def condicoes_de_validacao(email, senha):
    if email in usuarios_cadastrados:
        if senha == usuarios_cadastrados[email]:
            print('Usuário logado com sucesso!')
            return True
        else:
            print('Senha incorreta! Tente novamente.')
            return False
    else:
        print(f'E-mail inválido!\nTente se cadastrar')
        return False

# Classe para fazer login
class Login:
    def __init__(self, email : str, senha : str):
        self.__email = email
        self.__senha = senha

    # Getters
    def get_email(self):
        return self.__email
    def get_senha(self):
        return self.__senha

    def validar_usuario(self):
        email_para_validar = self.get_email()
        senha_para_validar = self.get_senha()
        condicoes_de_validacao(email_para_validar, senha_para_validar)