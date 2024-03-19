import random
import time


def frases_sequenciais():
    frases = ["Acredite  que a mudança está em você em sua capacidade.",
              "Cada passo, por tão simples que seja,ja é uma conquista.",
              "Não se entregue ao desespero, sempre que puder relaxe.",
              "Evite fazer coisas que lhe decepicione, para não desencadear desesperos momentaneos."
              "Seja paciente comcigo mesmo, que tudo isso vai passar.",
              "Você é forte e capaz de superar isso.",
              "Um descanso pode fazer você se sentir melhor."]
    
    return random.choice(frases)

def exercicios_respirar():
    exercicios = ["##Respiração diafragmáita: ## \n1° Sente-se em uma posição confortável.\n2° Coloque uma mão no peito e a outra na barriga.\n3° Respire fundo puxando o ar pelo nariz, fazendo com que a barriga se expanda.\n4° solte o ar lentamente pela boca, fazendo com que a barriga se contraia. \n5° faça esse procedimento por volta de 5 a 10 minutos. ",
                  "##Respiração quadrada: ## \n 1° sente-se em uma posição confortável. \n2° Respire fundo puxando o ar pelo nariz. \n3° Prenda a respiração e conte mentalmente até 4. \n4° solte a respiração pela boca contando até 4. \n5° aguarde 4 contagens antes de inspirar novamente. \n6° repita esse proscesso por 5 a 10 minutos.",
                  "##Respiração alternando narinas: ## \n1° Sente-se ou dete-se em uma posição confortavel. \n2° Feche os olhos e use o polegar direitopara tapar a narina direita. \n3° Inspire fundo pela outra narina. \n4° Feche a narina esquerda com o dedo anelar direito e expire pela narina direita. \n5° Inspire pela narina direita e expire pela narina esquerda. \n6° Continue alternado as narinas por 5 a 10 minutos."]
    return random.choice(exercicios)

def dicas_relaxar():
    dicas = ["##Faça um tipo de exercicio como alongamentos, caminhar, correr ou yoga.##",
             "##ouvir musicas.##",
             "##Tome chás relaxantes como camomila, lavanda,entro outros.##",
             "##tome um banho frio e relaxante.##",
             "##Procure fazer coisas que lhe tire da rotina, 'usando o bom senso', para se destrair. "]
    
    return random.choice(dicas)

while True:
    print("## Escolha uma das alternativas! ##")
    print("1° Buscar uma frase de motivação...")
    print("2° Exercicios de respiração...")
    print("3° Dicas para relaxar...")
    print("4° Sair")

    opcao = int (input("Digite uma opção, ex: 1, 2, 3 ou 4.\n"))

    if opcao == 1:
        frase = frases_sequenciais()
        print (f"\n{frase}\n")
    elif opcao == 2:
        exercicio = exercicios_respirar()
        print (f"\n{exercicio}\n")
    elif opcao == 3:
        dicas = dicas_relaxar()
        print (f"\n{dicas}\n")
    elif opcao == 4:
        print("Obrigado, estaremos a disposição! ")
        break
    else:
        print ("Opção inválida.")

        time.sleep(4)