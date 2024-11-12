from packages.linhas import Linha

class Matriz:
    def __init__(self, lista_de_linhas = None):
        if lista_de_linhas == None: #apenas cria uma matriz vazia
            self.linhas = []
            self.quantidade_linhas = 0
            self.quantidade_colunas = 0
        
        else:
        #adicionar uma condicional para ser possivel inserir uma lista aninhada
        #na hora de criar a matriz, podendo usar a classe caso a "matriz" já
        #exista            
            self.quantidade_colunas = len(max(lista_de_linhas))
            self.quantidade_linhas = len(lista_de_linhas)
            if len(max(lista_de_linhas)) != len(min(lista_de_linhas)):
                for index_linha in range(len(lista_de_linhas)):
                    if len(lista_de_linhas[index_linha]) < self.quantidade_colunas:
                        pass



        #criar função que alinhe as colunas para que seja reutilizada no código

    def _alinhar_matriz(self, lista):
        if len(lista) < self.quantidade_colunas:
            difereca_colunas = (self.quantidade_colunas - len(lista))
            lista += [0] * difereca_colunas
            self.linhas.append(lista)
            self.quantidade_linhas += 1 
            print(f"Adicionou-se {difereca_colunas} colunas à linha {self.linhas.index(lista) + 1} para manter a concisão da matriz.")

        elif len(lista) > self.quantidade_colunas:
            self.quantidade_colunas = len(lista)
            for x in range(len(self.linhas)):
                if len(self.linhas[x]) < self.quantidade_colunas:
                    difereca_colunas = (self.quantidade_colunas - len(self.linhas[x]))
                    self.linhas[x] += [0] * difereca_colunas
                    print(f"Adicionou-se {difereca_colunas} colunas à linha {x+1} para manter a concisão da matriz.")
            self.linhas.append(lista)
            self.quantidade_linhas += 1 
        
        elif len(lista) == self.quantidade_colunas:
            self.linhas.append(lista)
            self.quantidade_linhas += 1 


    def adicionar_linha(self, linha: Linha):  
        self._alinhar_matriz(linha.item)



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