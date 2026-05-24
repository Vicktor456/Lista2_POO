class Armazenador(ABC):
    @abstractmethod
    def salvar(self, dado):
        pass
