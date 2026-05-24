class Boleto:
    def __init__(self, codigo, valor):
        self.codigo = codigo
        self.valor = valor
        
    def imprimir(self) -> None:
        return f"Boleto - Codigo: {self.codigo} | Valor: R${self.valor}"
