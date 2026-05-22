class NotificadorEmail(Notificador):
    def notificar(self, mensagem):
        return f"E-mail: {mensagem}"
