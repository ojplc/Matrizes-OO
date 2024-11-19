#arquivo para testar a funcionalidade de criar uma matriz com uma lista aninhada

from packages.matrizes import Matriz
from packages.linhas import Linha

matriz_basica = [[0,3,1],[15,92,73,550,1209,34259],[11],[99,73,5,7,8]]

matriz1 = Matriz(matriz_basica)
matriz1.print_matriz()