# Exercício 2: Remover Duplicatas 
# Dada  uma  lista  com  alguns  elementos  duplicados,  converta  a  lista  em  um  set  para 
# remover duplicatas e depois converta de volta para uma lista.

lista = [5, 6, 5, 8, 6, 9, 1, 2]
lista = list(set(lista))
print(lista)