class TextoNarrado(Midia):
    def __init__(self, titulo, duracao, idioma):
        super().__init__(titulo, duracao)

        self.idioma = idioma

    def reproduzir(self):
        return f"Reproduzindo o texto narrado {self.titulo} com duração de {self.duracao} no idioma {self.idioma}"
