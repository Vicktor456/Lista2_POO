class NotificadorSMS(Notificador):
    def notificar(self, mensagem):
        return f"SMS: {mensagem}"
