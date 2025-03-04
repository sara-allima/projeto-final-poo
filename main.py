from carregar_e_salvar_usuarios import *
from cadastro import *

user = Cadastro('Sara Maria Alves de Lima', '123rosa', 99988877765, 16052005, 'Antonio Martins', 99998888, 'sara@gmail.com')
user.cadastrar_usuario()

user2 = Cadastro('Lara Luiza Diniz Maniçoba', '7676be', 11122233345, 17052005, 'Alexandria', 44445555, 'lara@hotmail.com')
user2.cadastrar_usuario()
print(usuarios_cadastrados)