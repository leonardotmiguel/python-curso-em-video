# Desafio 011
# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

l = float(input('Digite a largura da parede: '))
a = float(input('Digite a altura da parede: '))
area = l * a
tinta = area / 2
print(f'Sua parede tem a dimensão de {l}x{a} e sua área é de {area}m²\nPara pintar essa parede será necessário {tinta} litros de tinta')