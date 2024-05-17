#Crie um programa que receba uma lista de números e retorne o maior valor dessa lista
numeros = [1, 5, 7, 2, 6, 4]
print(f'lista: {numeros}')
maior = 0
for numero in numeros:
    if numero > maior:
        print("o número", numero, "é o maior agora.")
        maior = numero
        
    print(" o maior numero é", maior)
        
        