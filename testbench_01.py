from packages.matrizes import Matriz
from packages.linhas import Linha

linha1 = Linha([0,1,1,0])
linha1.quantiade_termos()

linha2 = Linha([1,2,3,4,5,6,7])
linha2.quantiade_termos()

linha3 = Linha([4,1,6])
linha3.quantiade_termos()

linha4 = Linha([5,5,5,5,5])
print(f"A soma dos termos da linha 4 é {linha4.soma_termos()}")
print('')


matriz1 = Matriz()

matriz1.adicionar_linha(linha1)
matriz1.adicionar_linha(linha2)
matriz1.adicionar_linha(linha3)
matriz1.adicionar_linha(linha4)


print('')

matriz1.print_matriz()

linha5 = Linha([1,2])
matriz1.adicionar_linha(linha5)

matriz1.print_matriz()