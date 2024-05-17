#Crie um programa que receba uma lista de números e retorne a soma de todos os valores.
numeros = [1, 5, 7, 2, 6, 4]
print(f'lista: {numeros}')
soma = 0

for numero in numeros:
    soma += numero
    
print(f'   somados da {soma}')