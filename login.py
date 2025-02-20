class Login:
    def __init__(self, usuario, senha):
        self.__usuario = usuario
        self.__senha = senha

    # Getters
    def get_usuario(self):
        return self.__usuario
    def get_senha(self):
        return self.__senha

    def validar_usuario(self, usuario, senha):
        usuario_para_validar = self.get_usuario
        senha_para_validar = self.get_senha
        if usuario == usuario_para_validar and senha == senha_para_validar:
            return True
        else:
            return False
