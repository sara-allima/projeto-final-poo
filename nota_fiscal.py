from datetime import datetime
class NotaFiscal:
    def __init__(self, data_emissao: str, hora_emissao: str, numero: int, serie : int):
        self.data_emissao = datetime.strptime(data_emissao, "%d/%m/%Y")
        self.hora_emissao = hora_emissao
        self.numero = numero
        self.serie = serie
        
    def adicionar_produto(self, nome: str, valor: float, quantidade: int):
        produto = {
            "nome": nome,
            "valor": valor,
            "quantidade": quantidade
        }
        self.produtos.append(produto)

    def obter_total(self):
        return sum(p["valor"] * p["quantidade"] for p in self.produtos)