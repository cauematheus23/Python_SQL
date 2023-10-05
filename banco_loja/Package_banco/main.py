import sqlite3
from Clientes import Cliente
from menu import Menu
import tkinter as tk
def conectar_banco():
    conexão_bd = sqlite3.connect('C:/Users/cauem/Documents/GitHub/Python_SQL/banco_loja/banco_loja.db')
    c = conexão_bd.cursor()
    return conexão_bd, c



def escolher_opção(opção):
    if opção == 1:
        cliente = Cliente(conexão_bd, c)
        cliente.exibir_menu()
    elif opção == 2:
        print("Escolheu 2")
    elif opção == 3:
        print("Escolheu 3")
    elif opção == 4:
        print("Escolheu 4")
    elif opção == 5:
        print("Escolheu 5")
    elif opção == 6:
        root.quit()
    else:
        print("Opção inválida")

if __name__ == "__main__":
    # Conecte-se ao banco de dados
    conexão_bd, c = conectar_banco()

    # Crie a janela principal
    root = tk.Tk()
    root.title("Menu Principal")

    # Botão para abrir o menu de cliente
    botão_cliente = tk.Button(root, text="Clientes", command=lambda: escolher_opção(1))
    botão_cliente.pack()

    # Outros botões para as opções 2 a 6
    for opção in range(2, 7):
        botão = tk.Button(root, text=f"Opção {opção}", command=lambda op=opção: escolher_opção(op))
        botão.pack()

    root.mainloop()

        


    


    