class Produtos:
    def __init__(self, codigo, nome, preco, quantidade):
        self.codigo = codigo
        self.nome = nome 
        self.preco = preco 
        self.quantidade = quantidade

    def atualizar_preco(self, novo_preco):
        if novo_preco <= 0:
            print("O preço do produto não pode ser negativo.")
        else:
            self.preco = float(novo_preco)
           
    def atualizar_quant(self, nova_quant):
        if self.quantidade + nova_quant < 0:
            print("A quantidade não pode ser menor do que zero.")
        elif self.quantidade + nova_quant > 500:
            print("A quntidade não pode passar do limite do estoque.")
        elif self.quantidade + nova_quant > 0 and self.quantidade + nova_quant < 500:
            soma = self.quantidade + nova_quant
            self.quantidade = soma

    def __str__(self):
        texto = "\nCódigo: " + str(self.codigo) + "\n"
        texto += "Nome: " + self.nome + "\n"
        texto += "Preço: " + str(self.preco) + "\n"
        texto += "Quantidade_estoque: " + str(self.quantidade) + "\n"
        return texto

    def imprimir(self):  
        print(self)  

class Pedido:
    def __init__(self,codigo, produto, quant):
        self.codigo = codigo
        self.produto = produto
        self.quantidade = quant
        
"DEF -- PRODU1, QUANT1, PRODU2, QUANT2, PRODU3, QUANT3"

##################- MAIN -########################

produ1 = Produtos(333, "agua", 18.0, 30)
produ1.imprimir()