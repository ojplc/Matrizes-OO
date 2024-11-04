class Linha:
    def __init__(self, item):
        if isinstance(item, list):
            self.item = item
        else:
            self.item = [item]
    
    def quantiade_termos(self):
        print(f"Sua linha tem {len(self.item)} termos")

    def produto_termos(self):
        produto = 1
        for i in self.item:
            produto *= i
        return produto
    
    def soma_termos(self):
        soma = 0
        for z in self.item:
            soma += z
        return soma