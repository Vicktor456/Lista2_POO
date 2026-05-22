class Funcionario(ABC):
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def mostrar_dados(self):
        return f"Nome: {self.nome} | CPF: {self.cpf}"
    
    @abstractmethod
    def calcular_pagamento(self):
        pass
