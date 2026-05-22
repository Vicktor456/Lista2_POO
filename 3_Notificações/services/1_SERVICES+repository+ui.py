class CentralNotificacoes():
    def __init__(self):
        # [REPOSITÓRIO]: Armazenamento em memória
        self.lista_notificadores = []

    # [SERVICES / REPOSITÓRIO]: Lógica para salvar um novo meio de envio
    def adicionar_notificador(self, notificador):
        self.lista_notificadores.append(notificador)

    # [SERVICES + UI]: Comanda o envio e exibe os resultados na tela
    def enviar_para_todos(self, mensagem):
        for i in self.lista_notificadores:
            print(i.notificar(mensagem))
