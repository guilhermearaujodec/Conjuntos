# Exercício 1: Criar e Manipular Sets 
# Crie  dois  sets,  um  com  números  pares  e  outro  com  números  ímpares.  Os  números 
# devem variar de 1 a 10. 
# o União: Obtenha a união dos dois sets. 
# o Interseção: Obtenha a interseção dos dois sets. 
# o Diferença: Obtenha a diferença dos sets (elementos que estão no primeiro set 
# e não no segundo).

pares = set()
impares = set()

for i in range(10):
    try:
        n = int(input('Número: '))
        if n % 2 == 0:
            pares.add(n)
        else:
            impares.add(n)
    except ValueError:
        print('O número deve ser inteiro')
print(pares)
print(impares)

uniao = pares | impares
intersecao = pares & impares
diferenca = pares - impares

print(f'União: {uniao}')
print(f'Interseção: {intersecao}')
print(f'Diferença: {diferenca}')
