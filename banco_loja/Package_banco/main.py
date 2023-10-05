import sqlite3
from Clientes import Cliente
from menu import Menu
def conectar_banco():
    conexão_bd = sqlite3.connect('C:/Users/cauem/Documents/GitHub/Python_SQL/banco_loja/banco_loja.db')
    c = conexão_bd.cursor()
    return conexão_bd, c

# Função para estabelecer a conexão com o banco de dados
if __name__ == "__main__":
    # Conecte-se ao banco de dados
    conexão_bd, c = conectar_banco()

a = Menu()
while True:
    a.cabeçalho()

    try:
        escolha = int(input("Digite qual deseja: "))
        if escolha == 1:
                cliente = Cliente(conexão_bd, c)
                cliente.exibir_menu()
        elif escolha == 2:
                print("Escolheu 2")
                break
        elif escolha == 3:
                print("Escolheu 3")
                break
        elif escolha == 4:
                print("Escolheu 4")
                break
        elif escolha == 5:
                print("Escolheu 5")
                break
        elif escolha == 6:
            break
        else:
            print("Digite um valor valido entre 1 e 6")
    except(ValueError,TypeError):
        print("Digite um valor valido entre 1 e 6")
        continue

        


    


    