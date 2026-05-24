@runtime_checkable
class Salvavel(Protocol):
    def salvar(self, dado) -> None:
        ...
