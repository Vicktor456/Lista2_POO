class Video(Midia):
    def __init__(self, titulo, duracao, resolucao):
        super().__init__(titulo, duracao)

        self.resolucao = resolucao

    def reproduzir(self):
        return f"Reproduzindo o video {self.titulo} com duração de {self.duracao} na resolução de {self.resolucao}"
