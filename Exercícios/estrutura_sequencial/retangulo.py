# área do retangulo = multiplicação da base pela altura
# A = b x h

# perímetro = soma de todos os seus lados
# P = 2(b x h)

# diagonal do retangulo =
# d² = b² + h²

baseDoRetangulo = float(input('Digite a base do retângulo: '))
alturaDoRetangulo = float(input('Digite a altura do retângulo: '))
areaDoRetangulo = baseDoRetangulo * alturaDoRetangulo
perimetro = 2 * (baseDoRetangulo + alturaDoRetangulo)
diagonalDoRetangulo = (baseDoRetangulo ** 2 + alturaDoRetangulo ** 2) ** 0.5

print(f'Área do retângulo: {areaDoRetangulo:.4f}')
print(f'Perímetro: {perimetro:.4f}')
print(f'Diagonal do retângulo: {diagonalDoRetangulo:.4f}')
