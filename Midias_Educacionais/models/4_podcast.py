class Podcast(Midia):
    def __init__(self, titulo, duracao, apresentador):
        super().__init__(titulo, duracao)

        self.apresentador = apresentador

    def reproduzir(self):
        return f"Reproduzindo o podcast {self.titulo} com duração de {self.duracao} sendo apresentado por {self.apresentador}"
