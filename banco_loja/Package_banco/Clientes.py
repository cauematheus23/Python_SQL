from tabulate import tabulate
from cores import cores
import random
import string
import tkinter as tk


class Cliente:
    def __init__(self, conexão_bd, c):
        self.conexão_bd = conexão_bd
        self.c = c
    
    def exibir_menu(self):
        janela = tk.Tk()
        janela.title("Inserir Dados de Cliente")
        janela.geometry("400x300")  # Largura x Altura

        while True:
            escolher = cores()

            try:
                print('[1] Consultar Cliente\n[2] Inserir Cliente\n[3] Atualizar Cliente\n[4] Deletar Cliente\n[5] Voltar')
                opção = int(input("Escolha uma opção: "))

                if opção == 1:
                    (self.view_cliente())
                elif opção == 2:
                    self.menuzinho()
                elif opção == 3:
                    self.atualizar_cliente()
                elif opção == 4:
                    self.deletar_cliente()
                elif opção == 5:
                    self.consultar_cliente()
                elif opção == 6:
                    break
                else:
                    print("Opção inválida")
            except (ValueError,TypeError):
                print("Por Favor, Digite um valor válido")
                continue

    def view_cliente(self):
        try:
            # Executa uma consulta SQL para recuperar os dados da tabela CLIENTE
            self.c.execute("SELECT * FROM CLIENTE")

            # Obtém todos os resultados da consulta
            resultados = self.c.fetchall()

            # Lista de cabeçalhos da tabela
            headers = [desc[0] for desc in self.c.description]

            # Use o tabulate para formatar e imprimir os resultados como uma tabela
            print(tabulate(resultados, headers, tablefmt="grid"))

        except Exception as e:
            print("Erro ao consultar dados:", str(e))
    def inserir_cliente(self):
        try:
            # Obtenha os valores dos campos de entrada
            cpf = self.entrada_cpf.get()
            nome = self.entrada_nome.get()
            email = self.entrada_email.get()
            endereco = self.entrada_endereco.get()
            telefone = self.entrada_telefone.get()

            # Define a consulta SQL para inserir dados na tabela CLIENTE
            sql = "INSERT INTO CLIENTE (CPF, Nome, Email, Endereco, Telefone) VALUES (?, ?, ?, ?, ?)"

            # Crie uma tupla com os valores de entrada
            valores = (cpf, nome, email, endereco, telefone)

            # Execute a consulta SQL com os valores de entrada
            self.c.execute(sql, valores)

            # Faça o commit das alterações no banco de dados
            self.conexao_bd.commit()

            print("Dados inseridos com sucesso.")
        except Exception as e:
            # Trate as exceções e imprima a mensagem de erro
            print("Erro ao inserir dados:", str(e))
    def menuzinho(self,janela):
        self.janela = janela
        self.janela.title("Inserir Dados de Cliente")

        self.label_cpf = tk.Label(janela, text="CPF:")
        self.label_cpf.pack()
        self.entrada_cpf = tk.Entry(janela)
        self.entrada_cpf.pack()

        self.label_nome = tk.Label(janela, text="Nome:")
        self.label_nome.pack()
        self.entrada_nome = tk.Entry(janela)
        self.entrada_nome.pack()

        self.label_email = tk.Label(janela, text="Email:")
        self.label_email.pack()
        self.entrada_email = tk.Entry(janela)
        self.entrada_email.pack()

        self.label_endereco = tk.Label(janela, text="Endereço:")
        self.label_endereco.pack()
        self.entrada_endereco = tk.Entry(janela)
        self.entrada_endereco.pack()

        self.label_telefone = tk.Label(janela, text="Telefone:")
        self.label_telefone.pack()
        self.entrada_telefone = tk.Entry(janela)
        self.entrada_telefone.pack()

        self.botao_inserir = tk.Button(janela, text="Inserir Dados", command=self.inserir_cliente)
        self.botao_inserir.pack()

       
        
    def atualizar_cliente(self):
        try:
            # SQL para atualizar todos os dados de um cliente com base no CPF
            sql = "UPDATE CLIENTE SET CPF = ?, Nome = ?, Email = ?, Endereco = ?, Telefone = ? WHERE CPF = ?"

            cpf_alvo = input("Digite o CPF do cliente que deseja atualizar: ")
            novo_cpf = input("Digite o novo CPF: ")
            novo_nome = input("Digite o novo nome: ")
            novo_email = input("Digite o novo email: ")
            novo_endereco = input("Digite o novo endereço: ")
            novo_telefone = input("Digite o novo telefone: ")
            
            # Valores a serem atualizados
            valores = (cpf_alvo,novo_cpf, novo_nome, novo_email, novo_endereco, novo_telefone)
            
            # Execute a instrução UPDATE
            self.c.execute(sql, valores)
            
            # Commit das mudanças
            self.conexão_bd.commit()
        except Exception as e:  
            print("Erro ao atualizar dados"+ e)

    def deletar_cliente(self):
        try:
            # Verifique se o cliente com o CPF especificado existe
            self.view_cliente()
            cpf = input("Digite o CPF do cliente que deseja excluir: ")
            self.c.execute("SELECT * FROM CLIENTE WHERE CPF=?", (cpf,))
            cliente = self.c.fetchone()
            if cliente is not None:
                # Se o cliente existe, execute a exclusão
                self.c.execute("DELETE FROM CLIENTE WHERE CPF=?", (cpf,))
                self.conexão_bd.commit()
                print(f"Cliente com CPF {cpf} foi excluído com sucesso.")
            else:
                print(f"Cliente com CPF {cpf} não encontrado.")

        except Exception as e:
            print("Erro ao excluir cliente:", str(e))
    def consultar_cliente(self):
        escolher = cores()
        try:
        # Solicite ao usuário o CPF do cliente a ser consultado
            cpf_alvo = input("Digite o CPF do cliente que deseja consultar: ")

            # Consulte os dados do cliente com base no CPF
            self.c.execute("SELECT * FROM CLIENTE WHERE CPF=?", (cpf_alvo,))
            cliente = self.c.fetchone()

            if cliente is not None:
                print("Informações do Cliente:")
                print((f"CPF: {escolher.verde(cliente[0])}"))
                print(f"Nome: {escolher.verde(cliente[1])}")
                print(f"Email: {escolher.verde(cliente[2])}")
                print(f"Endereço: {escolher.verde(cliente[3])}")
                print(f"Telefone: {escolher.verde(cliente[4])}")
            else:
                print(f"Cliente com CPF {cpf_alvo} não encontrado.")
        except Exception as e:
            print("Erro ao consultar cliente:", str(e))