# SETs 'conjunto'
# coleção mutável
# não garante ordem
# não aceita repetição


dias = set()
dias.add('terca')
dias.add('segunda')
print(dias)

# conjutos inicializados 
frutas = ['Maça', 'Uva', 'Pera', 'Laranja']
print(frutas)
print(type(frutas))

# remover 
frutas.remove('Uva')
print(frutas)
print(len(frutas))

lista = [1, 2, 3 ,4, 5, 6, 7]
conjunto_set = set(lista)
print(conjunto_set)

numeros = [1, 2, 3, 4, 5, 67, 8, 9,]
conjunto_numeros = set(lista)
print(conjunto_numeros)