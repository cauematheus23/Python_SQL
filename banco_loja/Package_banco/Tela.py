from tkinter import *
from tkinter import ttk
import sqlite3
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
import webbrowser
root = Tk()

class Relatorios():
    def printCliente(self):
        webbrowser.open("cliente.pdf")
    def geraRelatCliente(self):
        self.can = canvas.Canvas("cliente.pdf")

        self.idRel = self.id_entry.get()
        self.cpfRel = self.cpf_entry.get()
        self.telefoneRel = self.telefone_entry.get()
        self.cidadeRel = self.cidade_entry.get()
        self.emailRel = self.email_entry.get()

        self.can.setFont("Helvetica-Bold", 24)
        self.can.drawString(200, 790, 'Ficha do Cliente')
        self.can.setFont("Helvetica-Bold",18)
        self.can.drawString()
        self.can.showPage()
        self.can.save()
        self.printCliente()


class Funcs():
    def limpa_tela(self):
        self.cpf_entry.delete(0,END)
        self.nome_entry.delete(0,END)
        self.telefone_entry.delete(0,END)
        self.id_entry.delete(0,END)
        self.cidade_entry.delete(0,END)
        self.email_entry.delete(0,END)
    def conecta_banco(self):
        self.conexão_bd = sqlite3.connect('C:/Users/cauem/OneDrive/Documentos/MeusProjetos/Python_SQL/banco_loja/banco_loja.db')
        self.c = self.conexão_bd.cursor()

    def desconectar(self):
        self.conexão_bd.close()
    def add_cliente(self):
        self.variaveis()
        self.conecta_banco()

        sql = "INSERT INTO CLIENTE (CPF, Nome, Email, Cidade, Telefone) VALUES (?, ?, ?, ?, ?)"

            # Crie uma tupla com os valores de entrada
        valores = (self.cpf, self.nome, self.email, self.cidade, self.telefone)

            # Execute a consulta SQL com os valores de entrada
        self.c.execute(sql, valores)

            # Faça o commit das alterações no banco de dados
        self.conexão_bd.commit()
        self.desconectar()
        self.select_lista()
        self.limpa_tela()
    def select_lista(self):

        self.listacliente.delete(*self.listacliente.get_children())
        self.conecta_banco()
        lista = self.c.execute(""" SELECT id,CPF, Nome, Telefone, Email, cidade from cliente order by nome ASC;""")

        for i in lista: 
            self.listacliente.insert("", END,values = i)
    def variaveis(self):
        self.id = self.id_entry.get()
        self.cpf = self.cpf_entry.get()
        self.nome = self.nome_entry.get()
        self.telefone = self.telefone_entry.get()
        self.cidade = self.cidade_entry.get()
        self.email = self.email_entry.get()
    def OnDoubleClick(self,event):
        self.limpa_tela()
        self.listacliente.selection()

        for n in self.listacliente.selection():
            col1,col2,col3,col4,col5,col6 = self.listacliente.item(n,'values')
            self.id_entry.insert(END,col1)
            self.cpf_entry.insert(END,col2)
            self.nome_entry.insert(END,col3)
            self.telefone_entry.insert(END,col4)
            self.email_entry.insert(END,col5)
            self.cidade_entry.insert(END,col6)
    def deleta_cliente(self):

    
        self.variaveis()
        self.conecta_banco()
        self.c.execute("""DELETE FROM cliente WHERE id = ?""",(self.id))
        self.conexão_bd.commit()
        self.desconectar()
        self.limpa_tela()
        self.select_lista()
    def atualiza_cliente(self):
        self.variaveis()
        self.conecta_banco()
        sql = """UPDATE cliente set cpf = ?,Nome = ?, Telefone = ?, Email = ?, cidade = ? where id = ?"""
        valores =  (self.cpf, self.nome, self.telefone,self.email,self.cidade,self.id)
        self.c.execute(sql,valores)
        self.conexão_bd.commit()

        self.desconectar()
        self.select_lista()
        self.limpa_tela()
class Interface(Funcs,Relatorios):

    def __init__(self):
        self.root = root 
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.widgets_frame2()
        self.select_lista()
        self.Menus()
        root.mainloop()
    def tela(self):
        self.root.title("Cadastro de Clientes")
        self.root.configure(background= '#4682B4')
        self.root.geometry('700x500')
        self.root.resizable(True,True)
        self.root.maxsize(width=1200,height=720)
        self.root.minsize(width=500,height=400)
    def frames_da_tela(self):
        self.frame_1 =  Frame(self.root, bd = 4, bg = '#DCDCDC', highlightbackground= '#B0E0E6', highlightthickness=2)
        self.frame_1.place(relx= 0.02,rely= 0.02, relwidth= 0.96, relheight= 0.46)
        self.frame_2 =  Frame(self.root, bd = 4, bg = '#DCDCDC', highlightbackground= '#B0E0E6', highlightthickness=2)
        self.frame_2.place(relx= 0.02,rely= 0.5, relwidth= 0.96, relheight= 0.46)
    
    def widgets_frame1(self):
        ### Criação do botao limpar
        self.bt_limpar = Button(self.frame_1, text= 'Limpar', bd=2,bg = '#107db2', fg= 'white', font = ('verdana' , 8 , 'bold'),command=self.limpa_tela)
        self.bt_limpar.place(relx = 0.2, rely= 0.1, relwidth= 0.1, relheight= 0.15)
         ### Criação do botao Buscar
        self.bt_buscar = Button(self.frame_1, text= 'Buscar', bd=2,bg = '#107db2', fg= 'white', font = ('verdana' , 8 , 'bold'))
        self.bt_buscar.place(relx = 0.3, rely= 0.1, relwidth= 0.1, relheight= 0.15)
        ### Criação do botao Novo
        self.bt_novo = Button(self.frame_1, text= 'Novo', bd=2,bg = '#107db2', fg= 'white', font = ('verdana' , 8 , 'bold'), command=self.add_cliente)
        self.bt_novo.place(relx = 0.5, rely= 0.1, relwidth= 0.1, relheight= 0.15)
        ### Criação do botao Alterar
        self.bt_alterar = Button(self.frame_1, text= 'Alterar', bd=2,bg = '#107db2', fg= 'white', font = ('verdana' , 8 , 'bold'),command=self.atualiza_cliente)
        self.bt_alterar.place(relx = 0.6, rely= 0.1, relwidth= 0.1, relheight= 0.15)
        ### Criação do botao Buscar
        self.bt_apagar = Button(self.frame_1, text= 'Apagar', bd=2,bg = '#107db2', fg= 'white', font = ('verdana' , 8 , 'bold'),command=self.deleta_cliente)
        self.bt_apagar.place(relx = 0.7, rely= 0.1, relwidth= 0.1, relheight= 0.15)


        self.lb_id = Label(self.frame_1, text ='ID(deletar)', bg= '#DCDCDC')
        self.lb_id.place(relx=0.7,rely=0.75)

        self.id_entry = Entry(self.frame_1)
        self.id_entry.place(relx=0.7,rely=0.85,relwidth=0.15)
        
        #criação do label de cpf

        self.lb_cpf = Label(self.frame_1, text ='CPF', bg= '#DCDCDC')
        self.lb_cpf.place(relx=0.02,rely=0.05)
        
        #criação input cpf
        self.cpf_entry = Entry(self.frame_1)
        self.cpf_entry.place(relx=0.02,rely=0.15,relwidth=0.15)

        #criação do label de nome
        self.lb_nome = Label(self.frame_1, text ='Nome', bg= '#DCDCDC')
        self.lb_nome.place(relx=0.02,rely=0.25)
        
        #criação input nome
        self.nome_entry = Entry(self.frame_1, highlightbackground='blue')
        self.nome_entry.place(relx= 0.02,rely=0.35,relwidth=0.8,relheight=0.1)

               #criação do label de nome
        self.lb_telefone = Label(self.frame_1, text ='Telefone', bg = '#DCDCDC')
        self.lb_telefone.place(relx=0.02,rely=0.5)
        
        #criação input nome
        self.telefone_entry = Entry(self.frame_1) 
        self.telefone_entry.place(relx= 0.02,rely=0.6,relwidth=0.3,relheight=0.1)

        #criação do label de email
        self.lb_email = Label(self.frame_1, text ='Email', bg= '#DCDCDC')
        self.lb_email.place(relx=0.4,rely=0.5)
        
        #criação input email
        self.email_entry = Entry(self.frame_1)
        self.email_entry.place(relx= 0.4,rely=0.6,relwidth=0.45,relheight=0.1)

         #criação do label de email
        self.lb_cidade = Label(self.frame_1, text ='Cidade', bg= '#DCDCDC')
        self.lb_cidade.place(relx=0.02,rely=0.75)
        
        #criação input email
        self.cidade_entry = Entry(self.frame_1)
        self.cidade_entry.place(relx= 0.02,rely=0.85,relwidth=0.3,relheight=0.1)

    def widgets_frame2(self):
        self.listacliente = ttk.Treeview(self.frame_2, height = 3, columns= ('col1', 'col2', 'col3', 'col4','col5','col6'))
        self.listacliente.heading('#0', text = '')
        self.listacliente.heading('#1', text = 'id')
        self.listacliente.heading('#2', text = 'Cpf')
        self.listacliente.heading('#3', text = 'Nome')
        self.listacliente.heading('#4', text = 'Telefone')
        self.listacliente.heading('#5', text = 'Email')
        self.listacliente.heading('#6', text = 'Cidade')

        self.listacliente.column('#0', width=1)
        self.listacliente.column('#1', width=10)
        self.listacliente.column('#2', width=100)
        self.listacliente.column('#3', width=100)
        self.listacliente.column('#4', width=100)
        self.listacliente.column('#5', width=100)
        self.listacliente.column('#6', width=100)
        
        self.listacliente.place(relx=0.01,rely=0.1,relwidth=0.95,relheight=0.85)

        self.scrool = Scrollbar(self.frame_2, orient='vertical')
        self.listacliente.configure(yscroll= self.scrool.set)
        self.scrool.place(relx=0.96,rely=0.1,relwidth=0.04,relheight=0.85)
        self.listacliente.bind('<Double-1>', self.OnDoubleClick)

    def Menus(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)

        def quit() : self.root.destroy()

        menubar.add_cascade(label= "Opções", menu = filemenu)
        menubar.add_cascade(label= "Relatorios", menu = filemenu2)

        filemenu.add_command(label="Sair", command=quit)
        filemenu.add_command(label= "Limpar Cliente", command = self.limpa_tela)
        filemenu2.add_command(label= "Ficha do Cliente", command = self.geraRelatCliente)
#Interface()