from tabulate import tabulate

class Cliente:
    def __init__(self, conexão_bd, c):
        self.conexão_bd = conexão_bd
        self.c = c

    def insert_cliente(self):
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
