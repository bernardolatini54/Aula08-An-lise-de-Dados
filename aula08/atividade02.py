numeros = []

while True:
    num = int(input('Informe um número inteiro: '))
    numeros.append(num)
    resposta = input('\nDeseja continuar [S/N]: ').upper()

    if resposta == 'N':
        break

print(numeros)

quantidade = len(numeros)

print(f'\nA quantidade de números digitados: {quantidade}')