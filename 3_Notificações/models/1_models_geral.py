class Notificador(ABC):
    @abstractmethod
    def notificar(self, mensagem):
        pass

class NotificadorEmail(Notificador):
    def notificar(self, mensagem):
        return f"E-mail: {mensagem}"

class NotificadorSMS(Notificador):
    def notificar(self, mensagem):
        return f"SMS: {mensagem}"

class NotificadorApp(Notificador):
    def notificar(self, mensagem):
        return f"App: {mensagem}"
