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

class Produto:
    def __init__(self, id, nome, preco, quantidade):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def __str__(self):
        return f"{self.nome} - R${self.preco:.2f}"

class Estoque:
    def __init__(self):
        self.produtos = {
            1: Produto(1, "Água", 2.50, 500),
            2: Produto(2, "Arroz", 8.00, 300),
            3: Produto(3, "Feijão", 10.00, 200)
        }

    def listar_estoque_user(self):
        print("Estoque atual:")
        for produto in self.produtos.values():
            print(f"ID: {produto.id} - {produto}")
            
    def listar_estoque_adm(self):
        print("Estoque atual:")
        for produto in self.produtos.values():
            print(f"ID: {produto.id} - {produto} - Quantidade: {produto.quantidade}")

    def atualizar_quantidade(self, produto_id, quantidade):
        if produto_id in self.produtos:
            self.produtos[produto_id].quantidade += quantidade
            return True
        return False

class Pedido:
    def __init__(self, estoque):
        self.estoque = estoque
        self.itens_pedido = []

    def adicionar_produto(self, produto_id, quantidade):
        if quantidade > 10:
            print("Você só pode comprar até 10 unidades de cada produto.")
            return

        if produto_id in self.estoque.produtos:
            produto = self.estoque.produtos[produto_id]
            if produto.quantidade >= quantidade:
                produto.quantidade -= quantidade
                self.itens_pedido.append({'produto': produto, 'quantidade': quantidade})
                print(f"{quantidade} unidades de {produto.nome} adicionadas ao pedido.")
            else:
                print("Quantidade insuficiente no estoque.")
        else:
            print("Produto não encontrado.")

    def adicionar_produto_ong(self, produto_id, quantidade):
        if produto_id in self.estoque.produtos:
            produto = self.estoque.produtos[produto_id]
            if produto.quantidade >= quantidade:
                produto.quantidade -= quantidade
                self.itens_pedido.append({'produto': produto, 'quantidade': quantidade})
                print(f"{quantidade} unidades de {produto.nome} adicionadas ao pedido.")
            else:
                print("Quantidade insuficiente no estoque.")
        else:
            print("Produto não encontrado.")

    def remover_produto(self, produto_id, quantidade):
        for item in self.itens_pedido:
            if item['produto'].id == produto_id:
                if item['quantidade'] >= quantidade:
                    item['quantidade'] -= quantidade
                    self.estoque.atualizar_quantidade(produto_id, quantidade)
                    if item['quantidade'] == 0:
                        self.itens_pedido.remove(item)
                    print(f"{quantidade} unidades de {item['produto'].nome} removidas do pedido.")
                    return
        print("Produto não encontrado no pedido ou quantidade insuficiente.")

    def listar_pedido(self):
        if not self.itens_pedido:
            print("Nenhum produto no pedido.")
            return
        print("Produtos no pedido:")
        for item in self.itens_pedido:
            produto = item['produto']
            quantidade = item['quantidade']
            print(f"{produto} - Quantidade: {quantidade}")

cadastro = Cadastro()
estoque = Estoque()
pedido = Pedido(estoque)

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
    print("1 - Registrar")
    print("2 - Entrar")

def menu_pedido():
    print("==================")
    print("Menu de Pedido")
    print("==================")
    print("0 - Sair")
    print("1 - Adicionar Produto")
    print("2 - Remover Produto")
    print("3 - Visualizar Pedido")

def menu_administrador():
    print("==================")
    print("Menu de Administrador")
    print("==================")
    print("0 - Sair")
    print("1 - Visualizar Estoque")
    print("2 - Catalogar Produto")
    print("3 - Realizar Pedido")

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
                    menu_pedido()
                    opcao_pedido = input("Escolha: ")
                    if opcao_pedido == "0":
                        break
                    elif opcao_pedido == "1":
                        estoque.listar_estoque_user()
                        produto_id = int(input("ID do produto: "))
                        quantidade = int(input("Quantidade (máximo 10): "))
                        pedido.adicionar_produto(produto_id, quantidade)
                    elif opcao_pedido == "2":
                        produto_id = int(input("ID do produto: "))
                        quantidade = int(input("Quantidade: "))
                        pedido.remover_produto(produto_id, quantidade)
                    elif opcao_pedido == "3":
                        pedido.listar_pedido()
                    else:
                        input(f"Valor {opcao_pedido} inválido, tente novamente (Enter) ")
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
                elif opcao_administrador == "1":
                    estoque.listar_estoque_adm()
                elif opcao_administrador == "2":
                    nome = input("Nome do produto: ")
                    preco = float(input("Preço do produto: "))
                    quantidade = int(input("Quantidade: "))
                    novo_id = max(estoque.produtos.keys()) + 1
                    novo_produto = Produto(novo_id, nome, preco, quantidade)
                    estoque.produtos[novo_id] = novo_produto
                    print(f"Produto {nome} adicionado ao estoque.")
                elif opcao_administrador == "3":
                    while True:
                        menu_pedido()
                        opcao_pedido = input("Escolha: ")
                        if opcao_pedido == "0":
                            break
                        elif opcao_pedido == "1":
                            estoque.listar_estoque_adm()
                            produto_id = int(input("ID do produto: "))
                            quantidade = int(input("Quantidade: "))
                            pedido.adicionar_produto_ong(produto_id, quantidade)
                        elif opcao_pedido == "2":
                            produto_id = int(input("ID do produto: "))
                            quantidade = int(input("Quantidade: "))
                            pedido.remover_produto(produto_id, quantidade)
                        elif opcao_pedido == "3":
                            pedido.listar_pedido()
                        else:
                            input(f"Valor {opcao_pedido} inválido, tente novamente (Enter) ")
                            continue
                else:
                    input(f"Valor {opcao_administrador} inválido, tente novamente (Enter) ")
                    continue
        else:
            input("Tente novamente (Enter) ")
    else:
        input(f"Valor {opcao} inválido, tente novamente (Enter) ")
        continue