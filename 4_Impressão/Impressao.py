from typing import Protocol

class Imprimivel(Protocol):
    def imprimir(self) -> None:
        ...

class Boleto:
    def __init__(self, codigo, valor):
        self.codigo = codigo
        self.valor = valor
        
    def imprimir(self) -> None:
        return f"Boleto - Codigo: {self.codigo} | Valor: R${self.valor}"

class Etiqueta:
    def __init__(self, destinatario, endereco):
        self.destinatario = destinatario
        self.endereco = endereco

    def imprimir(self) -> None:
        return f"Etiqueta - Destinatario: {self.destinatario} | Endereço: {self.endereco}"

class RelatorioSimples:
    def __init__(self, titulo):
        self.titulo = titulo

    def imprimir(self) -> None:
        return f"Relatorio Simples - Titulo: {self.titulo}"
    
def processar_impressao(item: Imprimivel) -> None:
    print(item.imprimir())
