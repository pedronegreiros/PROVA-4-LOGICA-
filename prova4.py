#PROVA 4 LOGICA DE PROGRAMAÇÃO #ALUNO: PEDRO NEGREIROS

# Inicialize variáveis para a contagem, soma e média

contagem = 0

total = 0



# Loop para ler números até que o usuário digite 0

while True:

    num = input(int("Digite um número (0 para encerrar): "))

    if num == 0:

        break

    total += num

    contagem += 1



# Calcula a média (a divisão por zero é tratada para evitar erros)

if contagem == 0:

    media = 0

else:

    media = total / contagem



# Exibe os resultados

print("Quantidade de números digitados:", contagem)

print("Soma dos números digitados:", total)

print("Média dos números digitados:", media)




