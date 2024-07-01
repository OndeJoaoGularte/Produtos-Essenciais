lista_estoque = ["oi"]


class Produto:
    def __init__(self, codigo, nome, preco):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        
class Agua(Produto):
    def __init__(self, codigo, nome, preco, ml, gaseificada):
        super().__init__(codigo, nome, preco)
        self.ml = ml
        self.gaseificada = gaseificada #booleano
        
class Pao(Produto):
    def __init__(self, codigo, nome, preco, salgado, integral):
        super().__init__(codigo, nome, preco)
        self.salgado = salgado #booleano
        self.integral = integral #booleano
        
class Racao(Produto):
    def __init__(self, codigo, nome, preco, tipo_animal):
        super().__init__(codigo, nome, preco)
        self.tipo_animal = tipo_animal
        
# Simula o rebebimento do produto pelo mercado
def receber_produto(self, prod ):
    if prod == 1:
        cod = 1010
        nome = "Água"
        ml = input("500 ou 1000 Ml? ")
        gaseificada = input("Com ou sem gás? ")
        if ml == "500":
            preco = self.preco
        elif ml == "1000":
            preco = self.preco + 2.0
        agua = Agua(cod, nome, preco, ml, gaseificada)
        return lista_estoque.append(agua)
    else:
        print("OH yeah")
        
        
def imprimir_lista():
    print(lista_estoque)
        
# def cadastrar_produto(self, produto):
#     if produto == "Água":
        

def atualizar_preco(self, novo_preco):
    if novo_preco <= 0:
        print("O preço do produto não pode ser negativo.")
    else:
        self.preco = float(novo_preco)


######################################################

    def __str__(self):
        texto = "\nCódigo: " + str(self.codigo) + "\n"
        texto += "Nome: " + self.nome + "\n"
        texto += "Preço: " + str(self.preco) + "\n"
        texto += "Quantidade_estoque: " + str(self.quantidade) + "\n"
        return texto

    def imprimir(self):  
        print(self)  
