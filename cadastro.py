from carregar_e_salvar_usuarios import *
class Cadastro:
    def __init__(self, nome : str, senha : str, cpf : int, data_nascimento : int, local_residencia : str, num_telefone : int, email : str):
        self.__nome = nome
        self.__senha = senha
        self.__cpf = cpf
        self.__data_nascimento = data_nascimento
        self.__local_residencia = local_residencia
        self.__num_telefone = num_telefone
        self.__email = email
    
    # Getters
    def get_nome(self):
        return self.__nome
    def get_senha(self):
        return self.__senha
    def get_cpf(self):
        return self.__cpf
    def get_data_nascimento(self):
        return self.__data_nascimento
    def get_local_residencia(self):
        return self.__local_residencia
    def get_num_telefone(self):
        return self.__num_telefone
    def get_email(self):
        return self.__email
    
    # Métodos
    def cadastrar_usuario(self):
        email = self.get_email()
        senha = self.get_senha()
        if email in usuarios_cadastrados:
            print('Este e-mail já foi cadastrado. Tente fazer o login.')
        else:
            usuarios_cadastrados[email] = senha
            salvar_usuarios(usuarios_cadastrados)