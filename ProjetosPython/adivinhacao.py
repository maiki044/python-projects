import random

numero = random.randint(1, 100)
tentativas = 0

while True :
    chute = int(input("Adivinhe o numero (1 a 100):"))
    tentativas += 1
    if chute == numero:
        print(f"Parabéns! Voce acertou em {tentativas} tentativas.")
        break
    elif chute < numero:
        print("Tente um numero maior")
    else :
        print("Tente um numero menor")