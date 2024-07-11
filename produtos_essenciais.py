# GRUPO: jOÃO GULARTE, KAUAN MAGNABOSCO e GUILHERME FONTOURA

# Classes principais do código, que serão manipuladas posteriormente
class Usuario:
    def __init__(self, cpf, email, senha):
        self.cpf = cpf
        self.email = email
        self.senha = senha

class Administrador:
    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha

class Produto:
    def __init__(self, id, nome, preco, quantidade):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    # Representação de como o objeto será visualizado
    def __str__(self):
        return f"{self.nome} - R${self.preco:.2f}"

# Gerencia o cadastro de usuários e de um administrador
class Cadastro:
    # Adicionados tanto um usuário genérico como um administrador
    def __init__(self):
        self.usuarios = [
            Usuario("12345", "email@gmail.com", "senha123"),
        ]
        self.administradores = [
            Administrador("admin", "admin")
        ]

    # Registro de novos usuários, com uma verificação de senha e adicionando o usuário cadastrado a lista de usuários
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

    # Login para usuários já cadastrados, verifica se há um registro anterior dos dados colocados e informa qual usuário foi logado
    def entrar_usuario(self):
        cpf_ou_email = input("Digite seu Usuário (CPF ou Email): ")
        senha = input("Digite sua Senha: ")
        
        for usuario in self.usuarios:
            if (usuario.cpf == cpf_ou_email or usuario.email == cpf_ou_email) and usuario.senha == senha:
                print(f"\nEntrou como {usuario.email}\n")
                return True
        print("\nUsuário ou senha incorretos\n")
        return False
    
    # Login para administradores
    def validar_administrador(self):
        usuario = input("Digite o usuário: ")
        senha = input("Digite a senha: ")

        for admin in self.administradores:
            if admin.usuario == usuario and admin.senha == senha:
                print("\nEntrou como administrador\n")
                return True
        print("\nUsuário ou senha incorretos\n")
        return False

# Gerencia o estoque de produtos, adicionados produtos genéricos já catalogados
class Estoque:
    def __init__(self):
        self.produtos = {
            1: Produto(1, "Água", 2.50, 500),
            2: Produto(2, "Arroz", 8.00, 300),
            3: Produto(3, "Feijão", 10.00, 200)
        }

    # Apresenta o estoque atual de cada produto, o método para administradores mostra também a quantidade
    def listar_estoque_user(self):
        print("Estoque atual:")
        for produto in self.produtos.values():
            print(f"ID: {produto.id} - {produto}")
            
    def listar_estoque_adm(self):
        print("Estoque atual:")
        for produto in self.produtos.values():
            print(f"ID: {produto.id} - {produto} - Quantidade: {produto.quantidade}")

    # Atualiza a quantidade do produto após ser manipulado durante a realização do pedido
    def atualizar_quantidade(self, produto_id, quantidade):
        if produto_id in self.produtos:
            self.produtos[produto_id].quantidade += quantidade
            return True
        return False

# Classe responsável pela realização dos pedidos, irá retirar da quantidade dos produtos listados em estoque, o qual é representado pelo método "atualizar_quantidade"
class Pedido:
    def __init__(self, estoque):
        self.estoque = estoque
        self.itens_pedido = [] # Lista que será populada

    # Adiciona produtos ao pedido, apenas após verificar a existência e possibilidade de retirada a quantia do estoque
    def adicionar_produto(self, produto_id, quantidade):
        # Compras limitadas devido ao momento de calamidade para usuários únicos
        if quantidade > 10:
            print("\nVocê só pode comprar até 10 unidades de cada produto.\n")
            return

        if produto_id in self.estoque.produtos:
            produto = self.estoque.produtos[produto_id]
            if produto.quantidade >= quantidade:
                produto.quantidade -= quantidade
                self.itens_pedido.append({'produto': produto, 'quantidade': quantidade})
                print(f"\n{quantidade} unidades de {produto.nome} adicionadas ao pedido.\n")
            else:
                print("\nQuantidade insuficiente no estoque.\n")
        else:
            print("\nProduto não encontrado.\n")

    # Diferentemente do método anterior, não há limitação de compra, mas esse método só é chamado pelo painel de administrador
    def adicionar_produto_ong(self, produto_id, quantidade):
        if produto_id in self.estoque.produtos:
            produto = self.estoque.produtos[produto_id]
            if produto.quantidade >= quantidade:
                produto.quantidade -= quantidade
                self.itens_pedido.append({'produto': produto, 'quantidade': quantidade})
                print(f"\n{quantidade} unidades de {produto.nome} adicionadas ao pedido.\n")
            else:
                print("\nQuantidade insuficiente no estoque.\n")
        else:
            print("\nProduto não encontrado.\n")

    # Remove produtos adicionados anteriormente ao pedido, verifica se há a quantidade à ser removida
    def remover_produto(self, produto_id, quantidade):
        for item in self.itens_pedido:
            if item['produto'].id == produto_id:
                if item['quantidade'] >= quantidade:
                    item['quantidade'] -= quantidade
                    self.estoque.atualizar_quantidade(produto_id, quantidade)
                    if item['quantidade'] == 0:
                        self.itens_pedido.remove(item)
                    print(f"\n{quantidade} unidades de {item['produto'].nome} removidas do pedido.\n")
                    return
        print("\nProduto não encontrado no pedido ou quantidade insuficiente.\n")

    # Listagem dos produtos adicionados ao pedido
    def listar_pedido(self):
        if not self.itens_pedido:
            print("\nNenhum produto no pedido.\n")
            return
        print("\nProdutos no pedido:\n")
        for item in self.itens_pedido:
            produto = item['produto']
            quantidade = item['quantidade']
            print(f"{produto} - Quantidade: {quantidade}")

    # Finaliza o pedido e retorna o valor final
    def finalizar_pedido(self):
        if not self.itens_pedido:
            print("\nNenhum produto no pedido para finalizar.\n")
            return
        # Soma o preço de cada item para obtermos o valor total
        total = sum(item['produto'].preco * item['quantidade'] for item in self.itens_pedido)
        print(f"\nValor total do pedido: R${total:.2f}")
        
        # Limpa a lista para que possamos prosseguir para o próximo pedido
        self.itens_pedido = []
        print("\nPedido finalizado com sucesso.\n")

# Instâncias responsáveis pelo funcionamento do programa, com estoque sendo utilizado como argumento pois o objeto pedido precisa de acesso ao objeto estoque para funcionar corretamente
cadastro = Cadastro()
estoque = Estoque()
pedido = Pedido(estoque)

# Menus
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
    print("Pedido")
    print("==================")
    print("0 - Sair")
    print("1 - Adicionar Produto")
    print("2 - Remover Produto")
    print("3 - Visualizar Pedido")
    print("4 - Finalizar Pedido")

def menu_administrador():
    print("==================")
    print("Menu de Administrador")
    print("==================")
    print("0 - Sair")
    print("1 - Visualizar Estoque")
    print("2 - Catalogar Produto")
    print("3 - Realizar Pedido")

# Loop principal do programa
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
                    elif opcao_pedido == "4":
                        pedido.finalizar_pedido()
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
                    novo_id = max(estoque.produtos.keys()) + 1 # Garante que cada produto adicionado terá um ID maior que o anterior
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
                        elif opcao_pedido == "4":
                           pedido.finalizar_pedido()
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