class Plataforma:
    def __init__(self, nome):
        self.nome = nome
        # [REPOSITÓRIO]: Armazenamento local dos dados em memória
        self.lista_midia = []

    # [SERVICES / REPOSITÓRIO]: Lógica para manipular os dados (salvar na lista)
    def adicionar_midia(self, midia):
        self.lista_midia.append(midia)

    # [SERVICES + UI]: Comanda a lista e usa o print para exibir na tela
    def listar_midias(self):
        print(f"\n=== Midias da Plataforma {self.nome} ===")
        for i in self.lista_midia:
            print(i.mostrar_info())

    # [SERVICES + UI]: Comanda o fluxo de execução e exibe mensagens de erro e sucesso
    def reproduzir_todas(self):
        print(f"\n--- Iniciando {self.nome} ---")
        if not self.lista_midia:
            print("Nenhuma midia disponivel para reprodução.")
        else:
            for j in self.lista_midia:
                print(j.reproduzir())
