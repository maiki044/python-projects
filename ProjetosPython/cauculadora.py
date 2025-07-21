numero1 = float(input("Me informe o numero 1:"))
numero2 = float(input("Me informe o numero 2:"))
operacao = str(input("Entre soma, subtracao,multiplicacao e divisao qual operacao deseja fazer:"))



if operacao == 'soma' :
    soma = numero1 + numero2
    print("soma:",soma)
elif operacao == 'subtracao' :
    subtracao = numero1 - numero2
    print("subtracao:",subtracao)
elif operacao == 'multiplicacao' :
    multiplicacao = numero1 * numero2
    print("multiplicacao:",multiplicacao)
elif operacao == 'divisao' :
    if numero2 != 0:
        print("Divisao:",numero1/numero2)
    else :
        print("Erro: divisão por zero")
else :
    print("Operacao invalida, Tente novamente")

def caucular (numero1, numero2, operacao):
    if operacao == 'soma' :
        soma = numero1 + numero2
        print("soma:",soma)
    elif operacao == 'subtracao' :
        subtracao = numero1 - numero2
        print("subtracao:",subtracao)
    elif operacao == 'multiplicacao' :
        multiplicacao = numero1 * numero2
        print("multiplicacao:",multiplicacao)
    elif operacao == 'divisao' :
        if numero2 != 0:
            print("Divisao:",numero1/numero2)
        else :
            print("Erro: divisão por zero")
    else :
        print("Operacao invalida, Tente novamente")
        
while True:
    try:
        numero1 = float(input("Informe o primeiro numero:"))
        numero2 = float(input("Informe o segundo numero:"))
        operacao = input("Digite a operacao (soma, subtracao, multiplicacao, ou divisao):").lower()
        
        resultado = caucular (numero1, numero2, operacao)
        print("Resultado:",resultado)
    except ValueError:
        print("Por favor, insira numeros validos!")
    repetir = input("Deseja fazer outra operacao? (s/n):").lower()
    if repetir != 's':
        print("Encerrando cauculadora.")
        break