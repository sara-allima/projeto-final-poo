from time import sleep
from cadastro import *
from login import *

# Funções
def coletar_informacoes_cadastro_criar_usuario():
    nome = str(input('Digite seu nome: '))
    senha = str(input('Digite sua senha: ')) # Para criar o login, o usuário precisa de uma senha, que será guardada nessa variável.[...]
    confirm_senha = str(input('Digite a senha novamente: ')) #[...] Está segunda variável pede que o usuário repita a senha que ele acabou de criar. Essa confirmação é necessária para que o usuário tenha certeza que está colocando a senha correta

    while senha != confirm_senha: # Após confirmar a senha, o programa vai verificar se elas são diferentes. Se forem diferentes, o programa vai repetir a pergunta das senhas mais vezes
        print('Senhas não são iguais! Digite novamente!')
        senha = str(input('Digite sua senha: '))
        confirm_senha = str(input('Digite a senha novamente: '))

    if senha == confirm_senha: # Quando as senhas forem iguais, o resto das informações é pedida
        cpf = int(input('Digite seu CPF (Somente números): '))
        data_nascimento = int(input('Data Nascimento (Somente números): '))
        local_residencia = str(input('Local de Residencia: '))
        num_telefone = int(input('Número de telefone (Somente números): '))
        email = str(input('Seu melhor email: '))
    
    novo_usuario = Cadastro(nome, senha, cpf, data_nascimento, local_residencia, num_telefone, email) # Um novo usuário é criado com as informações concedidas
    novo_usuario.cadastrar_usuario() # Usuário é cadastrado se tudo estiver dentro dos conformes (Verificar arquivo "cadastro.py" para entender melhor os requisitos de cadastro)
def coletar_informacoes_login_verificar_usuario():
    email = pedir_email() # Função do arquivo "login" que pede o email do usuário
    senha = pedir_senha() # Função do arquivo "login" que pede senha do usuário
    usuario = Login(email, senha) # Cria o login para conseguirmos acessar seus métodos
    usuario.validar_usuario() # Método que verifica se o usuário já está cadastrado e se as credenciais que foram fornecidas por ele (email e senha) condizem com alguma do banco de dados

def mostrar_interface():
    controle = True # Variável de controle para mostrar a interface de opções do usuário

    while controle: # Enquanto a variável de controle for True, a interface continuará sendo mostrada
        print('Bem-Vindo(a) ao Scanner!\nFaça seu login ou crie uma nova conta')
        print('Selecione uma opção.\n1. Fazer Cadastro\n2. Entrar na Conta\n3. Sair')

        opcao = int(input())
        
        match opcao:
            case 1:
                coletar_informacoes_cadastro_criar_usuario() # Está função irá coletar todos os dados necessários para fazer o cadastro de um novo usuário
            case 2:
                coletar_informacoes_login_verificar_usuario() # Está função irá coletar todos os dados necessários para realizar o login do usuário, além de verificar se o login pode ser efetuado ou não
                # Ideia: criar nova interface para ser chamada somente quando o login for True??
            case 3: #opção para sair do programa
                print('Saindo...')
                sleep(1)
                controle = False
            case _:
                print('Opção Inválida!')

mostrar_interface()