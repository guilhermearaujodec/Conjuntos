"""
CONJUNTOS (SETS)
São usados para armazenar uma coleção de itens.

- Não permite itens repetidos.
- Não possuem uma ordem específica.
- Itens não podem ser acessados por índices ou chaves.
- Itens são delimitados por chaves { }
"""

conjunto = {1, 4, 'teste', 6.4, 6, 7 , 8, 1, 4}
print(conjunto)

# conjunto vazio
conjunto = set()
print(conjunto)

# inserir item
conjunto.add(5)
conjunto.add(7)
conjunto.add(10)
conjunto.add(5)
print(conjunto)

# remove um item (remove gera erro se item não existir)
conjunto.remove(5)
print(conjunto)

# remove um item (discard NÃO gera erro se item não existir)
conjunto.discard(5)
print(conjunto)

# remove um item (não é o mais utilizado)
conjunto = {1, 3, 4, 7, 8, 10}
item = conjunto.pop()
print(conjunto)
print(item)

# in (verifica se um item existe no conjunto)
conjunto = {4, 7, 1, 9, 1, 5, 3, 21}
if 4 in conjunto:
    print('Existe')
else:
    print('Não Existe')
    
# percorrer os itens do conjunto
for item in conjunto:
    print(item)
    
# tamanho do conjunto
print(conjunto)
print(f'Tamanho: {len(conjunto)}')


# ----------------------------------------------- OPERAÇÃO DE CONJUNTO

# união de conjuntos
c1 = {4, 6, 8, 10, 2}
c2 = {8, 4, 20, 12}
c3 = c1.union(c2)
print(c3)
c3 = c1 | c2
print(c3)

# interseção de conjuntos
c1 = {4, 6, 8, 10, 2}
c2 = {8, 4, 20, 12}
c3 = c1.intersection(c2)
print(c3)
c3 = c1 & c2
print(c3)

# diferença de conjuntos
c1 = {4, 6, 8, 10, 2}
c2 = {8, 4, 20, 12}
c3 = c1.difference(c2)
print(c3)
c3 = c1 - c2
print(c3)

# diferença simétrica
c1 = {4, 6, 8, 10, 2}
c2 = {8, 4, 20, 12}
c3 = c1.symmetric_difference(c2)
print(c3)
c3 = c1 ^ c2
print(c3)

# subconjunto
c1 = {4, 6, 8, 10, 2}
c2 = {4, 8}
print(c2.issubet(c1))


# REMOVER ITENS DE UMA LISTA

# convertendo para conjunto
lista = [5, 7, 5, 2, 1, 6, 5]
conjunto = set(lista)
lista = list(contjunto)
print(lista)

# sem conversão
lista = [5, 7, 5, 2, 1, 6, 5]
lista2 = []
for item in lista:
    if item not in lista2:
        lista2.append(item)
print(lista2)