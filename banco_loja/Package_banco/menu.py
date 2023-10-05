from cores import cores
class Menu():
    def cabeçalho (self):
        escolher = cores()
        print('\033[34m-'*40)
        print('|',end='')
        print('LOJA PODS'.center(38),end ='|\n')
        print('-'*40, '\033[m')
        print(escolher.amarelo('[1] Clientes'))
        print(escolher.amarelo('[2] Produto'))
        print(escolher.amarelo('[3] Pedido'))
        print(escolher.amarelo('[4] Item Pedido'))
        print(escolher.amarelo('[5] Estoque'))
