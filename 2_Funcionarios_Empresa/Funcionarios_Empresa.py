from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def mostrar_dados(self):
        return f"Nome: {self.nome} | CPF: {self.cpf}"
    
    @abstractmethod
    def calcular_pagamento(self):
        pass

class FuncionarioAssalariado(Funcionario):
    def __init__(self, nome, cpf, salario_mensal):
        super().__init__(nome, cpf)

        self.salario_mensal = salario_mensal

    def calcular_pagamento(self):
        return self.salario_mensal
    
class FuncionarioHorista(Funcionario):
    def __init__(self, nome, cpf, horas_trabalhadas, valor_hora):
        super().__init__(nome, cpf)

        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora

    def calcular_pagamento(self):
        return self.horas_trabalhadas * self.valor_hora
    
class FuncionarioComissionado(Funcionario):
    def __init__(self, nome, cpf, total_vendas, percentual_comissao):
        super().__init__(nome, cpf)

        self.total_vendas = total_vendas
        self.percentual_comissao = percentual_comissao

    def calcular_pagamento(self):
        return self.total_vendas * (self.percentual_comissao / 100)

class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.lista_funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.lista_funcionarios.append(funcionario)

    def listar_funcionarios(self):
        print(f"\n=== Funcionarios da Empresa {self.nome} ===")
        for i in self.lista_funcionarios:
            print(i.mostrar_dados())

    def mostrar_folha_pagamento(self):
        print(f"\n=== Folha de Pagamento da Empresa {self.nome} ===")

        valor_total = 0

        for i in self.lista_funcionarios:
            pagamento = i.calcular_pagamento()
            print(f"Funcionario: {i.nome} | Pagamento: R${pagamento:.2f}")
            valor_total += pagamento

        print(f"--- Valor total da folha de pagamento: R${valor_total:.2f} ---")
