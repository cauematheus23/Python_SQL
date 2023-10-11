from tkinter import *
from Tela import Interface

class Menu_Principal:
    def __init__(self, menu):
        self.menu = menu
        self.menu.protocol("WM_DELETE_WINDOW", self.fechar_janela)
        self.criar_menu()
        self.botoes()

    def criar_menu(self):
        self.menu.title('Menu Principal')
        self.menu.geometry('800x600')

    def abrir_interface_clientes(self):
        self.interface_clientes = Toplevel(self.menu)
        interface = Interface(self.interface_clientes)

    def fechar_janela(self):
        self.menu.destroy()

    def botoes(self):
        clientes_bd = Button(self.menu, text='Clientes', command=self.abrir_interface_clientes)
        clientes_bd.place(relx=0.1, rely=0.3, relwidth=0.3, relheight=0.3)

menu = Tk()
menu_principal = Menu_Principal(menu)
menu.mainloop()
