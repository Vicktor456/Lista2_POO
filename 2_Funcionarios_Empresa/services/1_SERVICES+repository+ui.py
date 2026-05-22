class Empresa:
    def __init__(self, nome):
        self.nome = nome
        # [REPOSITÓRIO]: Armazenamento local
        self.lista_funcionarios = []

    # [SERVICES / REPOSITÓRIO]: Lógica para salvar os dados na lista
    def adicionar_funcionario(self, funcionario):
        self.lista_funcionarios.append(funcionario)

    # [SERVICES + UI]: Comanda a busca e usa comandos de saída para o usuário
    def listar_funcionarios(self):
        print(f"\n=== Funcionarios da Empresa {self.nome} ===")
        for i in self.lista_funcionarios:
            print(i.mostrar_dados())

    # [SERVICES + UI]: Calcula a soma total e imprime o relatório formatado
    def mostrar_folha_pagamento(self):
        print(f"\n=== Folha de Pagamento da Empresa {self.nome} ===")

        # Lógica de negócio do Service (acumular valores)
        valor_total = 0

        for i in self.lista_funcionarios:
            pagamento = i.calcular_pagamento()
            print(f"Funcionario: {i.nome} | Pagamento: R${pagamento:.2f}")
            valor_total += pagamento
        print(f"--- Valor total da folha de pagamento: R${valor_total:.2f} ---")
