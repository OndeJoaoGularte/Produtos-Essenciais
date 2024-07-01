# Importando o arquivo da classe Produto
from Produto import Produto, receber_produto

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
            pass #visualisar estoque
        elif menu == "2":
            receber_produto(1)
        else:
            input(f"Valor {menu} inválido, tente novamente (Enter) ")
            continue
       