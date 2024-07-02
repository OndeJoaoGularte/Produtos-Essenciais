class Usuario:
    def __init__(self, cpf, email, senha):
        self.cpf = cpf
        self.email = email
        self.senha = senha

class Administrador:
    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha

class Cadastro:
    def __init__(self):
        self.usuarios = [
            Usuario("12345", "email@gmail.com", "senha123"),
            ]
        self.administradores = [
            Administrador("admin", "admin")
        ]

    def registrar_usuario(self):
        cpf = input("Digite seu CPF: ")
        email = input("Digite seu Email: ")
        senha = input("Digite sua Senha: ")
        confirmar_senha = input("Confirmar Senha: ")

        if senha != confirmar_senha:
            print("\nAs senhas não coincidem. Tente novamente\n")
            return
        
        novo_usuario = Usuario(cpf, email, senha)
        self.usuarios.append(novo_usuario)
        print("\nUsuário registrado\n")

    def entrar_usuario(self):
        cpf_ou_email = input("Digite seu CPF ou Email: ")
        senha = input("Digite sua Senha: ")
        
        for usuario in self.usuarios:
            if (usuario.cpf == cpf_ou_email or usuario.email == cpf_ou_email) and usuario.senha == senha:
                print(f"\nEntrou como {usuario.email}\n")
                return True
        print("\nUsuário ou senha incorretos\n")
        return False
    
    def validar_administrador(self):
        usuario = input("Digite o usuário: ")
        senha = input("Digite a senha: ")

        for admin in self.administradores:
            if admin.usuario == usuario and admin.senha == senha:
                print("\nEntrou como administrador\n")
                return True
        print("\nUsuário ou senha incorretos\n")
        return False

cadastro = Cadastro()

def menu_principal():
    print("==================")
    print("Menu Principal")
    print("==================")
    print("0 - Sair")
    print("1 - Usuário")
    print("2 - Administrador")

def menu_cadastro():
    print("==================")
    print("Cadastro")
    print("==================")
    print("0 - Sair")
    print("1 - Registrar") #realizar cadastro
    print("2 - Entrar") #informar cadastro

def menu_usuario():
    print("==================")
    print("Menu de Usuário")
    print("==================")
    print("0 - Sair")
    print("1 - Adicionar Produto")
    print("2 - Remover Produto")
    print("3 - Listar Pedido")

def menu_administrador():
    print("==================")
    print("Menu de Administrador")
    print("==================")
    print("0 - Sair")
    print("1 - Visualizar Estoque")
    print("2 - Catalogar Produto")

while True:
    menu_principal()
    opcao = input("Escolha: ")

    if opcao == "0":
        break
    elif opcao == "1":
        menu_cadastro()
        opcao_cadastro = input("Escolha: ")

        if opcao_cadastro == "0":
            break
        elif opcao_cadastro == "1":
            cadastro.registrar_usuario()
        elif opcao_cadastro == "2":
            if cadastro.entrar_usuario():
                while True:
                    menu_usuario()
                    opcao_usuario = input("Escolha: ")
                    if opcao_usuario == "0":
                        break
                    elif opcao_usuario == "1":
                        break #adicionar_prod
                    elif opcao_usuario == "2":
                        break #remover_prod
                    elif opcao_usuario == "3":
                        break #listar_ped
                    else:
                        input(f"Valor {opcao_usuario} inválido, tente novamente (Enter) ")
                        continue
            else:
                input("Tente novamente (Enter) ")
        else:
                input(f"Valor {opcao_cadastro} inválido, tente novamente (Enter) ")
    elif opcao == "2":
        if cadastro.validar_administrador():
            while True:
                menu_administrador()
                opcao_administrador = input("Escolha: ")
                if opcao_administrador == "0":
                    break
                elif opcao_usuario == "1":
                    break #visualizar estoque
                elif opcao_usuario == "2":
                    break #catalogar produto
                else:
                    input(f"Valor {opcao_administrador} inválido, tente novamente (Enter) ")
                    continue
        else:
            input("Tente novamente (Enter) ")
    else:
        input(f"Valor {opcao} inválido, tente novamente (Enter) ")
        continue




"""""
class Pedido:
    def __init__(self, codigo, quantidade):
        self.codigo = codigo
        self.quantidade = quantidade
"""""
"""""
    def adicionar_prod
    def remover_prod
    def listar_ped

"""""