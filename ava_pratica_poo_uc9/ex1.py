class Pizza:
    def _init_(self, nome: str, tamanho: str):
        self.nome = nome
        self.tamanho = tamanho
        self.preco = 0

    def preco_final(self):
        tamanho = {
            'Pequena': 1.0,
            'Média': 2.0,
            'Grande': 3.0
        } 
        multi_preco = tamanho.get(self.tamanho, 1.0)
        self.preco = multi_preco

    def exibir_detalhes(self):
        preco_base = self.preco_final()
        return f'Nome: {self.nome}\nTamanho: {self.tamanho}\nPreço Base: R${self.preco:.2f}'
    
p = Pizza('s moda', 'P')
print(p.exibir_detalhes())
