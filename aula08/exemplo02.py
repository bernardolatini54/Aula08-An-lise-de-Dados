produtos = []

for i in range(5):
    produto = input('Informe o nome do produto: ')
    produtos.append(produto) # adicionar lista de produtos

print(produtos)

# acesso ao elemento
n = int(input('Digite a posição do elemento a acessar: '))
print(produtos[-1])

# alterando uma lista "nome do elemento"
produtos[-1] = input(f'Informe o nome do elemento {n}: ')
print(produtos)

# remover da lista
produto_a_remover = input('Digite o nome do produto a remover: ')
if produto_a_remover in produtos:
    produtos.remove(produto_a_remover)
print(produtos)