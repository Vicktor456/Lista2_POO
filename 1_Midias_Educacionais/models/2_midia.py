class Midia(ABC):
    def __init__(self, titulo, duracao):

        self.titulo = titulo
        self.duracao = duracao

    def mostrar_info(self):
        return f"O titulo é {self.titulo} e tem duração de {self.duracao}"

    @abstractmethod
    def reproduzir(self):
        pass
