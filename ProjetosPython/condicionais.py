idade = int(input("Digite sua idade:"))

if idade >= 18:
    print("Permitido")
else:
    print("Bloqueado")

salario = float(input("Me informe o seu salario:"))

if salario <= 3000:
    print("Programador Junior")
elif salario > 3000 and salario <= 6000:
    print("Programador Pleno")
elif salario > 6000:
    print("Programador Senior")
else :
    print("Gerente de projetos")

lista_numeros = [1,2,3]

print(lista_numeros[0])
print(lista_numeros[1])
print(lista_numeros[2])

notas = []

for x in range (3):
    codigo_aluno = input("RM:")
    nota = float(input("Nota: "))
    resultado = [codigo_aluno,nota]
    notas.append(resultado)

print("quantidade de notas",len(notas))

for n in notas:
    codigo_aluno = n[0]
    nota = n[1]
    print("O RM",codigo_aluno,"tirou nota:",nota)