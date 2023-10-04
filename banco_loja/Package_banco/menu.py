from cores import cores
class Menu():
    def cabeçalho (self):
        print('\033[34m-'*40)
        print('LOJA PODS'.center(40))
        print('-'*40)
        print('\033[m')
        escolher = cores()
        print(escolher.amarelo('[1] Clientes'))
        print(escolher.amarelo('[2] Produto'))
        print(escolher.amarelo('[3] Pedido'))
        print(escolher.amarelo('[4] Item Pedido'))
        print(escolher.amarelo('[5] Estoque'))
