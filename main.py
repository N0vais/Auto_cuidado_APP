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

janela = tk.Tk()
janela.geometry("300x400")

titulo = tk.Label(text="Autocuidado e Redução da ansiedade")
titulo.pack()

#   Adiquirindo escalas de ansiedade 
escalaLabel =tk.Label(text="Nivel de ansiedade (0-10): ")
escalaLabel.pack()
escalaAnsiedade = tk.Scale(orient= "horizontal", from_= 0, to= 10)
escalaAnsiedade.pack()

# colocando caixa de texto 
pensamentosLabel = tk.Label(text="pensamentos e emoçoes: ")
pensamentosLabel.pack()
textoPensamentos = tk.Text(height=10)
textoPensamentos.pack()

botaoRegistrar = tk.Button(text="Registrar seu sintomas", command = registrondoSintomas)
botaoRegistrar.pack()

janela.mainloop()