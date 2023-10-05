from tabulate import tabulate
from cores import cores
import random
import string


class Cliente:
    def __init__(self, conexão_bd, c):
        self.conexão_bd = conexão_bd
        self.c = c
    
    def exibir_menu(self):
        while True:
            escolher = cores()

            try:
                print('[1] Consultar Cliente\n[2] Inserir Cliente\n[3] Atualizar Cliente\n[4] Deletar Cliente\n[5] Voltar')
                opção = int(input("Escolha uma opção: "))

                if opção == 1:
                    (self.view_cliente())
                elif opção == 2:
                    self.inserir_cliente()
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
            # Define the SQL query to insert data into the CLIENTE table
            sql = "INSERT INTO CLIENTE (CPF, Nome, Email, Endereco, Telefone) VALUES (?, ?, ?, ?, ?)"

            # Prompt the user for input data
            cpf = input("Digite o CPF: ")
            nome = input("Digite o nome: ")
            email = input("Digite o Email: ")
            endereco = input("Digite o Endereço: ")
            telefone = input("Digite o Telefone: ")

            # Create a tuple with the input values
            valores = (cpf, nome, email, endereco, telefone)

            # Execute the SQL query with the input values
            self.c.execute(sql, valores)

            # Commit the changes to the database
            self.conexão_bd.commit()

            print(self.c.rowcount, "record inserted.")
        except Exception as e:
            # Handle exceptions and print the error message
            print("Erro ao inserir dados:", str(e))


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