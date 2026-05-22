from questao2 import Funcionario, FuncionarioAssalariado, FuncionarioHorista ,FuncionarioComissionado, Empresa

empresa1 = Empresa("Bemol")

funcionario1 = FuncionarioAssalariado("Vicktor Eduardo", "044.896.972-60", 2500)
funcionario2 = FuncionarioHorista("Davi Vitor", "000.000.000-00", 60, 18)
funcionario3 = FuncionarioComissionado("Isabely Berça", "035.466.612-65", 40000, 35)

empresa1.adicionar_funcionario(funcionario1)
empresa1.adicionar_funcionario(funcionario2)
empresa1.adicionar_funcionario(funcionario3)

empresa1.listar_funcionarios()
empresa1.mostrar_folha_pagamento()

"""
Qual é a superclasse da hierarquia?
R = A superclasse é "Funcionario"

Quais são as subclasses?
R = As subclasses são: "FuncionarioAssalariado", "FuncionarioHorista" e "FuncionarioComissionado"

Onde ocorre sobrescrita?
R = No método calcular_pagamento, este método é declarado como abstrato na superclasse e é sobrescrito dentro de cada uma das três
subclasses para realizar o cálculo específico de cada tipo de funcionario.

Onde ocorre polimorfismo?
R = O polimorfismo acontece dentro da classe "Empresa", especificamente no método mostrar_folha_pagamento (pagamento = i.calcular_pagamento())

Qual a vantagem de usar ABC nesse caso?
R = Garantia de um contrato, pois ao marcar calcular_pagamento com @abstractmethod, o Python obriga qualquer desenvolvedor que criar uma nova subclasse
de Funcionario a implementar esse método, se alguém esquecer de criá-lo, o código quebrará imediatamente, evitando erros em produção quando a classe
Empresa tentar rodar a folha de pagamento.

"""
