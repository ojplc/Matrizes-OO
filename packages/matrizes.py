from packages.linhas import Linha

class Matriz:
    def __init__(self, lista_de_linhas = None):
        if lista_de_linhas == None: #apenas cria uma matriz vazia
            self.linhas = []
            self.quantidade_linhas = 0
            self.quantidade_colunas = 0
        
        else:
        #ideia:
        #adicionar uma condicional para ser possivel inserir uma lista aninhada
        #na hora de criar a matriz, podendo usar a classe caso a "matriz" já
        #exista            
        ####done
            self.linhas = lista_de_linhas
            self.quantidade_colunas = len(max(self.linhas, key = len))
            self.quantidade_linhas = len(self.linhas)
            if len(max(self.linhas, key = len)) != len(min(self.linhas, key = len)):
                for index_linha in range(len(self.linhas)):
                    if len(self.linhas[index_linha]) < self.quantidade_colunas:
                        self._alinhar_matriz()


        #ideia:
        #criar função que alinhe as colunas para que seja reutilizada no código
        ###reescrever essa função para que ela olhe todos os termos e ajuste
        ###o tamamho, ao inves de ajustar ao adicionar o termo
        ###ou seja, ela será chamada sempre que houver a necessidade de alinhar a matriz
        ###ao inves dela propria decidir se é necessário alinhar ou não
        ##### done
    def _alinhar_matriz(self):
        while len(min(self.linhas, key = len)) != self.quantidade_colunas:
            difereca_colunas = self.quantidade_colunas - len(min(self.linhas, key = len))
            linha_ajusatada = self.linhas.index(min(self.linhas, key = len)) + 1
            index_menor_linha = self.linhas.index(min(self.linhas, key = len))
            self.linhas[index_menor_linha] += [0] * difereca_colunas
            print(f"Adicionou-se {difereca_colunas} colunas à linha {linha_ajusatada} para manter a concisão da matriz.")





    def adicionar_linha(self, linha: Linha):
        if len(linha.item) == self.quantidade_colunas:  
            self.linhas.append(linha.item)
            self.quantidade_linhas += 1
        elif len(linha.item) != self.quantidade_colunas:
            self.linhas.append(linha.item)
            self.quantidade_linhas += 1
            self.quantidade_colunas = len(max(self.linhas, key = len))
            self._alinhar_matriz()

    #ideia
    #há sugestões, de fazer com que quando se imprima a matriz ele
    #saia com cada termo um em cima do outro
    def print_matriz(self):
        if self.linhas == []:
            print("Sua matriz está vazia")
        else:
            print("Sua matriz:")
            for y in self.linhas:
                print(f"{y}")

    #ideia:
    #Criar função que transforme uma linha da matriz em um objeto Linha