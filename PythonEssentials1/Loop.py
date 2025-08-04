largest_number = -999999999

number = int(input("me informe um numero: "))

while number != -1:
    if number > largest_number:
        largest_number = number
    number = int(input("DIGITE outro numero (-1 para sair): "))

print("O maior numero informado foi:", largest_number)

odd_numbers = 0
even_numbers = 0

number = int(input("Digite um numero ou digite 0 para parar o programa:"))

while number != 0:
    
    if number % 2 == 1:
        odd_numbers += 1
    else :
        even_numbers += 1
    number = int(input("Digite outro numero ou digite 0 para sair do programa:"))
    
print("Numeros impares:",odd_numbers)
print("Numeros pares:",even_numbers)

counter = 5
while counter != 0:
    print("Dentro do laço.",counter)
    counter -= 1
print("Fora do circuito.",counter)

print(
    """
    +===================================+
    |   Bem                             |
    |   Vindo ao Programa de Loop       |
    |   Este programa demonstra o uso de|
    |   loops em Python.                |
    |                                   |
    |                                   |
    |                                   |
    |                                   |
    +===================================+
    """
)
power = 1
for expo in range (16):
    print("2 a potencia de:", expo,"e",power)
    power *= 2
