import sqlite3
from menu import Menu

a = Menu()
while True:
    
    a.cabeçalho()
    try:
        escolha = int(input("Digite qual deseja: "))
    
        if escolha == 1:
                print("escolheu 1")
                break
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

    


    
    