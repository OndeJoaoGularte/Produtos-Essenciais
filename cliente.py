class Cliente:
    def __init__(self, nome):
        self.nome = nome
    def mostrar_cliente(self):
        print(f"Nome do cliente:{self.nome}")
class Pessoa(Cliente):
    def __init__(self, nome, cpf):
        super().__init__(nome)
        self.cpf = cpf
class Abrigo(Cliente):
    def __init__(self, nome, cod):
        super().__init__(nome)
        self.cod = cod        
pessoa1 = Pessoa("Guilherme", "73827481248")
pessoa1.mostrar_cliente()
