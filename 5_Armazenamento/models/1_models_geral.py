class Armazenador(ABC):
    @abstractmethod
    def salvar(self, dado):
        pass

class ArmazenadorArquivo(Armazenador):
    def salvar(self, dado):
        return f"Arquivo - Salvando dados: {dado}"
        
class ArmazenadorBanco(Armazenador):
    def salvar(self, dado):
        return f"Banco de dados - Salvando dados: {dado}"

@runtime_checkable
class Salvavel(Protocol):
    def salvar(self, dado) -> None:
        ...

class ArmazenadorNuvem:
    def salvar(self, dado):
        return f"Nuvem - Salvando dados: {dado}"
