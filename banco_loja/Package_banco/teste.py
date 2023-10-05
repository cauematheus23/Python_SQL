import tkinter as tk

def inserir_dados():
    cpf = entrada_cpf.get()
    nome = entrada_nome.get()
    email = entrada_email.get()
    endereco = entrada_endereco.get()
    telefone = entrada_telefone.get()

    # Adicione aqui a lógica para inserir os dados no banco de dados

# Crie uma janela principal e defina seu tamanho
janela = tk.Tk()
janela.title("Inserir Dados de Cliente")
janela.geometry("400x300")  # Largura x Altura

# Crie e posicione os rótulos e campos de entrada
label_cpf = tk.Label(janela, text="CPF:")
label_cpf.pack()
entrada_cpf = tk.Entry(janela)
entrada_cpf.pack()

label_nome = tk.Label(janela, text="Nome:")
label_nome.pack()
entrada_nome = tk.Entry(janela)
entrada_nome.pack()

label_email = tk.Label(janela, text="Email:")
label_email.pack()
entrada_email = tk.Entry(janela)
entrada_email.pack()

label_endereco = tk.Label(janela, text="Endereço:")
label_endereco.pack()
entrada_endereco = tk.Entry(janela)
entrada_endereco.pack()

label_telefone = tk.Label(janela, text="Telefone:")
label_telefone.pack()
entrada_telefone = tk.Entry(janela)
entrada_telefone.pack()

# Crie um botão para inserir os dados e defina seu tamanho
botao_inserir = tk.Button(janela, text="Inserir Dados", command=inserir_dados, width=20, height=2)
botao_inserir.pack()

janela.mainloop()
