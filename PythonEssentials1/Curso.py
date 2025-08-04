largest_number = -999999999
number = int(input("me informe um numero:"))
if number == -1:
    print(largest_number)
    exit()
if number > largest_number:
    largest_number = number

name = input("me informe o nome de uma planta: ")

if name == "rosa":
    print("A rosa é uma planta muito bonita.")
elif name == "cacto":
    print("O cacto é uma planta resistente.")
else :
    print("Não conheço essa planta.")



