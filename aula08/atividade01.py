vendas = []

for i in range(10):
    venda = float(input('Informe o valor da venda: R$ '))
    vendas.append(venda)

print(vendas)

total = sum(vendas)

print(f'Total: R$ {total}')