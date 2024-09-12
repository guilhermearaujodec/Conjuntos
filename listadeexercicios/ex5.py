# Exercício 5: Diferença Entre Conjuntos 
# 1. Dado um conjunto de alunos que frequentam um curso de Python e outro conjunto de 
# alunos que frequentam um curso de Java, encontre: 
# o Os alunos que frequentam apenas o curso de Python. 
# o Os alunos que frequentam apenas o curso de Java. 
# o Os alunos que frequentam ambos os cursos. 
# o Os alunos que frequentam pelo menos um dos cursos.

python = {'ana', 'joao', 'pedro', 'paulo'}
java = {'ana', 'pedro', 'marcelo', 'carolina'}
print(python - java)        # diferenca
print(java - python)        # diferenca
print(java & python)        # interseção
print(java | python)        # união