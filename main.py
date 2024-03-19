import tkinter as tk
from datetime import datetime

escalaAnsieade = [9]

#crinado uma função
def registrondoSintomas():

    data = datetime.today().strftime("%d/%m/%y")
    ansiedade = int (escalaAnsiedade.get())
    pensando = textoPensamentos.get("1.0", "end-1c")

    with open("Sintomas.txt", "a") as f:
        f.write ("f {data},{ansiedade}, {pensando}\n")

#criando uma função para apresentar uma mensagem de sucesso#
def mostrar_mensagen():
    janela_mensagem = tk.Toplevel()
    janela_mensagem.geometry()
    janela_mensagem.title("Mensagem")

    #criação da mensagen
    texto_mensagem = tk.Label(janela_mensagem, text="Cadastrado com sucesso, pode continuar...")
    texto_mensagem.pack()

    #criando um botao para fechar a janela
    botao_fecha = tk.Button(janela_mensagem, text="Fechar", command=janela)
    botao_fecha.pack()

    #fim da função 

janela = tk.Tk()
janela.title("Autocuidado a Ansiedade")
janela.geometry("600x700")

titulo = tk.Label(text="Autocuidado e Redução da ansiedade")
titulo.pack()

#   Adiquirindo escalas de ansiedade 
escalaLabel =tk.Label(text="Nivel de ansiedade (0-10): ")
escalaLabel.pack()
escalaAnsiedade = tk.Scale(orient= "horizontal", from_= 0, to= 10)
escalaAnsiedade.pack()

# colocando caixa de texto 
pensamentosLabel = tk.Label(text="pensamentos e emoçoes: ")
pensamentosLabel.pack(pady=20)
textoPensamentos = tk.Text(height=10)
textoPensamentos.pack(pady=20)

botaoRegistrar = tk.Button(janela, text="Registrar seu sintomas", command =  mostrar_mensagen)
botaoRegistrar.pack()

janela.mainloop()