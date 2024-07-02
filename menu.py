# Importando o arquivo da classe Produto
from Produto import Produto, receber_produto, lista_estoque

# Criando o menu principal
menu_principal_string = """
==================
Menu Principal
==================
0 - Sair
1 - Cadastro
2 - Usuário
3 - Administrador
"""
# Criando a função principal que vai rodar no arquivo "main"
def menu_principal(): 
    while True:
        print(menu_principal_string)
        menu = input("Escolha: ")
        if menu == "0":
            break #sair
        elif menu == "1":
            pass #cadastro
        elif menu == "2":
            pass #usuário
        elif menu == "3":
            menu_administrador()
        else:
            # Caso o valor seja inválido, (continue) não quebra o loop
            input(f"Valor {menu} inválido, tente novamente (Enter) ")
            continue
       
       
       
############## Menu Cadastro

############## Menu Usuário



menu_administrador_string = """
==================
Menu do Administrador
==================
0 - Sair
1 - Visualizar Estoque
2 - Cadastrar Produto
"""

def menu_administrador():
    while True:
        print(menu_administrador_string)
        menu = input("Escolha: ")
        if menu == "0":
            break 
        elif menu == "1":
            for produto in lista_estoque:
                print(f"Nome: {produto.nome} \nCódigo: {produto.codigo} \n ----- ")
        elif menu == "2":
            menu_cadastro_produtos()
        else:
            input(f"Valor {menu} inválido, tente novamente (Enter) ")
            continue
'''
objeto = receber_produto("Água")
objeto.quantidade_recebida(int(input(f"Defina a quantidade desejada do produto {objeto.nome}: ")))
'''
menu_cadastro_produtos_string = """
==================
Menu Cadastro Produtos
==================
0 - Sair
1 - Água
2 - Pão
3 - Ração
"""

def menu_cadastro_produtos():
    while True:
        print(menu_cadastro_produtos_string)
        menu = input("Escolha: ")
        if menu == "0":
            break 
        elif menu == "1":
            objeto = receber_produto("Água")
            objeto.quantidade_recebida(int(input(f"Defina a quantidade desejada do produto {objeto.nome}: ")))
        elif menu == "2":
            objeto = receber_produto("Pão")
            objeto.quantidade_recebida(int(input(f"Defina a quantidade desejada do produto {objeto.nome}: ")))
        elif menu == "3":
            pass
        else:
            # Caso o valor seja inválido, (continue) não quebra o loop
            input(f"Valor {menu} inválido, tente novamente (Enter) ")
            continue