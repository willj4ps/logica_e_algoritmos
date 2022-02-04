# a) a área do quadrado que tem lado A
# b) a área do triângulo retângulo que base A e altura B
# c) a área do trapézio que tem bases A e B, e altura C

# area do quadrado = base * altura (como o quadrado tem lados iguais...
# apenas pegar a medida de um dos lados e elevar ao quadrado

# triangulo retangulo = base * altura / 2

# area do trapezio = (altura+base)/2 x altura

a = float(input('Digite a medida A: '))
b = float(input('Digite a medida B: '))
c = float(input('Digite a medida C: '))

quadrado = a ** 2
trianguloRetangulo = (a * b) / 2
trapezio = (a + b) / 2 * c

print(f'Área do Quadrado = {quadrado:.4f}')
print(f'Área do triangulo retangulo = {trianguloRetangulo:.4f}')
print(f'Área do trapézio = {trapezio:.4f}')
