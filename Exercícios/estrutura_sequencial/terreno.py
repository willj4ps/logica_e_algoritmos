larguraTerreno = float(input('Digite a largura do terreno: '))
comprimentoTerreno = float(input('Digite o comprimento do terreno: '))
metroQuadrado = float(input('Digite o valor do metro quadrado: '))
areaDoTerreno = larguraTerreno * comprimentoTerreno
precoDoTerreno = areaDoTerreno * metroQuadrado

print(f'Área do terreno: {areaDoTerreno:.2f}')
print(f'Preço do terreno: {precoDoTerreno:.2f}')
