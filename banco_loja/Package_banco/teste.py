import tkinter as tk

janela = tk.Tk()
janela.title("teste")
janela.geometry('800x600')

teste_label = tk.Label(janela, text = 'Escolha uma opção abaixo')
teste_label.grid(column=0, row = 0, padx= 300, pady =300)

janela.mainloop()