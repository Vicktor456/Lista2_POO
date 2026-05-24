class ArmazenadorBanco(Armazenador):
    def salvar(self, dado):
        return f"Banco de dados - Salvando dados: {dado}"
