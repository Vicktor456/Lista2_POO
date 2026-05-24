class RelatorioSimples:
    def __init__(self, titulo):
        self.titulo = titulo

    def imprimir(self) -> None:
        return f"Relatorio Simples - Titulo: {self.titulo}"
