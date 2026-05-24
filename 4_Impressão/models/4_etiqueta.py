class Etiqueta:
    def __init__(self, destinatario, endereco):
        self.destinatario = destinatario
        self.endereco = endereco

    def imprimir(self) -> None:
        return f"Etiqueta - Destinatario: {self.destinatario} | Endereço: {self.endereco}"
