from packages.matrizes import Matriz
from packages.linhas import Linha

linha1 = Linha([0,1,1,0])
linha1.quantiade_termos()

linha2 = Linha([1,2,3,4,5,6,7])
linha2.quantiade_termos()

print('')


matriz1 = Matriz()

matriz1.adicionar_linha(linha1)
matriz1.adicionar_linha(linha2)


print('')

matriz1.print_matriz()
