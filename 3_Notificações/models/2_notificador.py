class Notificador(ABC):
    @abstractmethod
    def notificar(self, mensagem):
        pass
