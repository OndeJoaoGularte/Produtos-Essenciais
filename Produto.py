lista_estoque = []


class Produto:
    def __init__(self, codigo, nome, preco):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        
    def quantidade_recebida(self, quantidade):
        for x in range (quantidade):
            lista_estoque.append(self)
    
        
class Agua(Produto):
    def __init__(self, codigo, nome, preco, ml):
        super().__init__(codigo, nome, preco)
        self.ml = ml
    
class Pao(Produto):
    def __init__(self, codigo, nome, preco, salgado):
        super().__init__(codigo, nome, preco)
        self.salgado = salgado 
        
class Racao(Produto):
    def __init__(self, codigo, nome, preco, tipo_animal):
        super().__init__(codigo, nome, preco)
        self.tipo_animal = tipo_animal
        
        
def receber_produto( prod ):
        if prod == "Água":
            ml = input("Preferência de 500 ou 1000 Ml? \n500 ML = 1 \n1000 Ml = 2 \nEscolha: ")
            if ml == "1":
                nome = "Água 500Ml"
                cod = 1010
                preco = 5.0
            elif ml == "2":
                nome = "Água 1000Ml"
                cod = 2020
                preco = 10.0
            agua = Agua(cod, nome, preco, ml)
            return agua
        elif prod == "Pão":
            sal = input("Preferência de Pão doce ou salgado? \nSalgado = 1 \nDoce = 2 \nEscolha: ")
            if sal == "1":
                nome = "Pão Salgado"
                cod = 1415
                preco = 2.0
            elif sal == "2":
                nome = "Pão Doce"
                cod = 1515
                preco = 3.0
            pao = Pao(cod, nome, preco, sal)
            return pao
        else:
            print("Produto Inválido!")
        ## Outros produtos
        
    
    




# def atualizar_preco(self, novo_preco):
#     if novo_preco <= 0:
#         print("O preço do produto não pode ser negativo.")
#     else:
#         self.preco = float(novo_preco)

    # def __str__(self):
    #     texto = "\nCódigo: " + str(self.codigo) + "\n"
    #     texto += "Nome: " + self.nome + "\n"
    #     texto += "Preço: " + str(self.preco) + "\n"
    #     return texto

    # def imprimir(self):  
    #     print(self)  
