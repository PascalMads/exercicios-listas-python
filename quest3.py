#rie um programa que receba duas listas e retorne uma terceira lista com a interseção dos elementos das duas listas.

lista1 = [1, 3, 5, 7, 9]    
lista2 = [2, 4, 6, 8, 10]
lista3 = []

for items in lista1:
    lista3.append(items)

for items in lista2:
    lista3.append(items)
    
lista3.sort()

print(lista3)