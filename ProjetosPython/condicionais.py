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


# Cria uma lista vazia para armazenar as notas e os RMs dos alunos
notas = []

# Loop que repete 3 vezes para cadastrar 3 alunos
for x in range(3):
    # Solicita o código RM do aluno (identificação)
    codigo_aluno = input("RM: ")
    
    # Solicita a nota do aluno e converte para número decimal
    nota = float(input("Nota: "))
    
    # Cria uma lista com o RM e a nota do aluno
    resultado = [codigo_aluno, nota]
    
    # Adiciona essa lista à lista principal 'notas'
    notas.append(resultado)

# Exibe quantos alunos foram cadastrados (quantidade de listas dentro de 'notas')
print("Quantidade de notas:", len(notas))

# Percorre a lista de alunos e mostra os dados de cada um
for n in notas:
    # Pega o RM (posição 0 da sublista)
    codigo_aluno = n[0]
    
    # Pega a nota (posição 1 da sublista)
    nota = n[1]
    
    # Exibe o RM e a nota do aluno
    print("O RM", codigo_aluno, "tirou nota:", nota)

notas = []
contador = 1

while contador <= 5:
    codigo_aluno = input ("RM:")
    nota = float (input("nota: "))
    resultado = [codigo_aluno,nota]
    notas.append(resultado)

    #alternativa: contador += 1
    contador = contador + 1

print("quantidade de notas", len(notas))

