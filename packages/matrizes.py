from packages.linhas import Linha

class Matriz:
    def __init__(self):
        self.linhas = []
        self.quantidade_linhas = 0
        self.quantidade_colunas = 0

    def adicionar_linha(self, linha: Linha):
        self.linhas.append(linha.item)
        self.quantidade_linhas += 1 
        if self.quantidade_colunas < len(linha.item):
            self.quantidade_colunas = len(linha.item)
            for x in range(len(self.linhas)):
                if len(self.linhas[x]) < self.quantidade_colunas:
                    difereca_colunas = (self.quantidade_colunas - len(self.linhas[x]))
                    self.linhas[x] += [0] * difereca_colunas
                    print(f"Adicionou-se {difereca_colunas} colunas à linha {x+1} para manter a concisão da matriz.")




    def print_matriz(self):
        if self.linhas == []:
            print("Sua matriz está vazia")
        else:
            print("Sua matriz:")
            for y in self.linhas:
                print(f"{y}")

    
    def determinate(self):
        if self.quantidade_colunas == self.quantidade_linhas:
            pass 
            #programar determinante