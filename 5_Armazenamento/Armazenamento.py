from typing import Protocol, runtime_checkable
from abc import ABC, abstractmethod

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

def executar_salvamento_formal(armazenador: Armazenador, dado) -> None:
    print(f"Tentando salvamento formal para: {type(armazenador).__name__}")
    
    if isinstance(armazenador, Armazenador):
        armazenador.salvar(dado)
    else:
        print(f"Erro: {type(armazenador).__name__} não pertence à hierarquia formal (ABC)")

def executar_salvamento_flexivel(objeto: Salvavel, dado) -> None:
    print(f"Tentando salvamento flexível para: {type(objeto).__name__}")
    
    if isinstance(objeto, Salvavel):
        objeto.salvar(dado)
    else:
        print(f"Erro Estrutural: {type(objeto).__name__} não possui a estrutura necessária")
