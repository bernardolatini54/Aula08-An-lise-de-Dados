numeros = []

for i in range(12):
    num = int(input('Digite um número inteiro: '))
    numeros.append(num)

ordenada = sorted(numeros)

print(f'{ordenada}')