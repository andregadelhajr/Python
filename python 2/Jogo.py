print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")


Minha_Idade = 21

print("")
chute_str = input("Digite a provável idade: ")
print("")
print("Você digitou: " , chute_str)
print("")
chute = int(chute_str)

acertou = chute == Minha_Idade
maior = chute > Minha_Idade
menor = chute < Minha_Idade

if(acertou):
    print("Parabéns! Você acertou!")
else:
    if(maior):
        print("O seu chute foi maior do que o número secreto!")
    elif(menor):
        print("O seu chute foi menor do que o número secreto!")

print("")
print("Fim do jogo")
