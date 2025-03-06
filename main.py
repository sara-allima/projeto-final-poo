import cadastro
import login
from nota_fiscal import adicionar_nota_manual
import importacao
from datetime import datetime, timedelta
import json

def cadastrar_usuario():
    print("Cadastro de Usuário")
    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")
    cpf = input("Digite seu CPF: ")
    data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")
    local_residencia = input("Digite seu local de residência: ")
    num_telefone = input("Digite seu número de telefone: ")
    email = input("Digite seu e-mail: ")

    # Cria uma instância da classe Cadastro e salva no arquivo JSON
    usuario = cadastro.Cadastro(nome, senha, cpf, data_nascimento, local_residencia, num_telefone, email)
    usuario.salvar_em_json()
    print("Cadastro realizado com sucesso!\n")

def realizar_login():
    print("Login")
    email = input("Digite seu e-mail: ")  # Pedir o e-mail ao invés do nome de usuário
    senha = input("Digite sua senha: ")

    # Criar o objeto Login com e-mail e senha
    login_obj = login.Login(email, senha)
    
    # Validar o login
    if login_obj.validar_usuario():
        print("Login bem-sucedido!\n")
    else:
        print("E-mail ou senha incorretos.\n")
        return False
    return True

def importar_nota():
    arquivo_importado = input("Digite o caminho do arquivo da nota fiscal (em formato JSON): ")
    importacao.importar_nota_json(arquivo_importado)
    print("Nota fiscal importada com sucesso!\n")

def carregar_compras(arquivo="notas_fiscais.json"):
    """Carregar as compras do arquivo JSON."""
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
def consultar_compras_por_data():
    """Consulta as compras realizadas em uma data específica ou intervalo de datas."""
    compras = carregar_compras()  # Carregar as compras do arquivo JSON
    tipo_consulta = input("Deseja consultar compras por data (única) ou intervalo de datas? (data/intervalo): ").lower()

    if tipo_consulta == "data":
        data_str = input("Digite a data para consulta (dd/mm/aaaa): ")
        try:
            data_consulta = datetime.strptime(data_str, "%d/%m/%Y")
            compras_filtradas = [compra for compra in compras if datetime.strptime(compra["data_emissao"], "%d/%m/%Y") == data_consulta]
            print(f"Consultando compras para o dia {data_consulta.strftime('%d/%m/%Y')}...\n")
        except ValueError:
            print("Formato de data inválido. Por favor, use dd/mm/aaaa.\n")
            return
        
    elif tipo_consulta == "intervalo":
        data_inicio_str = input("Digite a data de início no formato dd/mm/aaaa: ")
        data_fim_str = input("Digite a data de fim no formato dd/mm/aaaa: ")
        
        try:
            data_inicio = datetime.strptime(data_inicio_str, "%d/%m/%Y")
            data_fim = datetime.strptime(data_fim_str, "%d/%m/%Y")
            compras_filtradas = [compra for compra in compras if data_inicio <= datetime.strptime(compra["data_emissao"], "%d/%m/%Y") <= data_fim]
            print(f"Consultando compras entre {data_inicio.strftime('%d/%m/%Y')} e {data_fim.strftime('%d/%m/%Y')}...\n")
        except ValueError:
            print("Formato de data inválido. Por favor, use dd/mm/aaaa.\n")
            return
    else:
        print("Opção inválida. Escolha 'data' ou 'intervalo'.\n")
        return
    
    # Exibir compras encontradas
    if compras_filtradas:
        for compra in compras_filtradas:
            print(f"Data da compra: {compra['data_emissao']}")
            print(f"Hora da compra: {compra['hora_emissao']}")
            print("Produtos comprados:")
            for produto in compra["produtos"]:
                print(f"- {produto['nome']} | R${produto['valor']} | Quantidade: {produto['quantidade']}")
            print("\n")
    else:
        print("Nenhuma compra encontrada para o período informado.\n")

def comparar_compras():
    """Compara as compras em diferentes períodos (mês, semana, ano)."""
    periodo = input("Deseja comparar compras de qual período? (mês/semana/ano): ").lower()
    
    data_atual = datetime.now()
    compras = carregar_compras()  # Carregar as compras do arquivo JSON

    compras_mes_atual = []
    compras_mes_anterior = []
    compras_ano_atual = []
    compras_ano_anterior = []

    if periodo == "mês":
        primeiro_dia_mes_atual = data_atual.replace(day=1)
        primeiro_dia_mes_anterior = primeiro_dia_mes_atual.replace(month=data_atual.month-1 if data_atual.month > 1 else 12)
        compras_mes_atual = [compra for compra in compras if datetime.strptime(compra["data_emissao"], "%d/%m/%Y").month == data_atual.month]
        compras_mes_anterior = [compra for compra in compras if datetime.strptime(compra["data_emissao"], "%d/%m/%Y").month == primeiro_dia_mes_anterior.month]
        print(f"Comparando compras do mês {data_atual.strftime('%m/%Y')} com o mês anterior...\n")
    elif periodo == "semana":
        # Lógica para comparar compras da semana atual e semana anterior
        pass
    elif periodo == "ano":
        compras_ano_atual = [compra for compra in compras if datetime.strptime(compra["data_emissao"], "%d/%m/%Y").year == data_atual.year]
        compras_ano_anterior = [compra for compra in compras if datetime.strptime(compra["data_emissao"], "%d/%m/%Y").year == data_atual.year - 1]
        print(f"Comparando compras de {data_atual.year} com o ano anterior...\n")
    else:
        print("Período inválido. Escolha entre 'mês', 'semana' ou 'ano'.\n")
        return
    
    # Calcular total de compras
    total_mes_atual = sum(sum(produto["valor"] * produto["quantidade"] for produto in compra["produtos"]) for compra in compras_mes_atual)
    total_mes_anterior = sum(sum(produto["valor"] * produto["quantidade"] for produto in compra["produtos"]) for compra in compras_mes_anterior)
    total_ano_atual = sum(sum(produto["valor"] * produto["quantidade"] for produto in compra["produtos"]) for compra in compras_ano_atual)
    total_ano_anterior = sum(sum(produto["valor"] * produto["quantidade"] for produto in compra["produtos"]) for compra in compras_ano_anterior)
    
    # Exibir resultados
    if periodo == "mês":
        print(f"Total de compras no mês atual: R${total_mes_atual:.2f}")
        print(f"Total de compras no mês anterior: R${total_mes_anterior:.2f}\n")
    elif periodo == "ano":
        print(f"Total de compras no ano atual: R${total_ano_atual:.2f}")
        print(f"Total de compras no ano anterior: R${total_ano_anterior:.2f}\n")


def menu_principal():
    while True:
        print("1. Realizar Cadastro")
        print("2. Realizar Login")
        print("3. Importar Nota Fiscal")
        print("4. Consultar Compras por Data")
        print("5. Comparar Compras de Períodos")
        print("6. Adicionar Nota Fiscal Manualmente")
        print("7. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            if realizar_login():
                print("Login realizado com sucesso!\n")
            else:
                print("Falha no login.\n")
        elif opcao == "3":
            importar_nota()
        elif opcao == "4":
            consultar_compras_por_data()
        elif opcao == "5":
            comparar_compras()
        elif opcao == "6":
            adicionar_nota_manual()  # Chama a função importada de nota_fiscal.py
        elif opcao == "7":
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

if __name__ == "__main__":
    menu_principal()

