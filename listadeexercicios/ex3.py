# Exercício 3: Contar Elementos Únicos 
# Dada  uma  lista  com  vários  elementos  (alguns  podem  ser  duplicados),  crie  um  set  a 
# partir dessa lista e conte a quantidade de elementos únicos.

lista = [5, 6, 5, 8, 6, 9, 1, 2]
lista = list(set(lista))
print(lista)
print(len(lista))