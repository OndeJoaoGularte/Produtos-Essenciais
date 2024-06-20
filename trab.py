class Produtos:
    def __init__(self, codigo, nome, preco, quantidade):
        self.codigo = codigo
        self.nome = nome 
        self.preco = preco 
        self.quantidade = quantidade

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

#################################################

produ1 = Produtos(333, "agua", 18.0, 30)

produ1.imprimir()
produ1.atualizar_quant(-40)
produ1.imprimir()