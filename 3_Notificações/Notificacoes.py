from abc import ABC, abstractmethod

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

class CentralNotificacoes():
    def __init__(self):
        self.lista_notificadores = []

    def adicionar_notificador(self, notificador):
        self.lista_notificadores.append(notificador)

    def enviar_para_todos(self, mensagem):
        for i in self.lista_notificadores:
            print(i.notificar(mensagem))
