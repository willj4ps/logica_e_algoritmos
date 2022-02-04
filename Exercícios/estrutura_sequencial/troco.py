precoProduto = float(input('Preço unitário do produto: '))
qtdCompra = int(input('Quantidade comprada: '))
dinheiro = float(input('Dinheiro recebido: '))

totalCompra = precoProduto * qtdCompra
troco = dinheiro - totalCompra

print(f'Troco = R$ {troco:.2f}')
