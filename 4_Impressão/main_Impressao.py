from questao4 import Imprimivel, Boleto, Etiqueta, RelatorioSimples, processar_impressao

boleto1 = Boleto("111111", 150.00)
etiqueta1 = Etiqueta("Isabely", "Rua das Tulipas")
relatorio1 = RelatorioSimples("Relatorio Parcial PIBIC")

processar_impressao(boleto1)
processar_impressao(etiqueta1)
processar_impressao(relatorio1)

"""
Onde está o contrato nesse caso?
R = O contrato está na classe Imprimivel, que herda de Protocol

Por que as classes podem funcionar sem herdar explicitamente do protocolo?
R = Porque o Protocol utiliza o conceito de subtipagem estrutural, diferente da herança tradicional, o ecossistema do Python não se importa com o "nome da família" 
da classe, mas sim com a sua anatomia. Como as classes "Boleto", "Etiqueta" e "RelatorioSimples" implementam o método imprimir exatamente com a assinatura exigida, 
elas passam a cumprir o contrato automaticamente, por compatibilidade de estrutura.

Esse caso se aproxima mais de ABC ou de ducktyping?
R = Se aproxima mais de duck typing, a regra básica do duck typing diz: "Se caminha como um pato e quaca como um pato, então é um pato". Se as suas classes contêm o 
método esperado, elas são aceitas pelo protocolo sem a necessidade de amarras formais.

Qual a principal diferença entre esse caso e o da Questão 1?
R = Na questão 1 o acoplamento é explícito e obrigatório por herança, para que a classe "Video" seja considerada um tipo válido de Midia, ela precisa declarar 
nominalmente na sua assinatura que herda dela (class Video(Midia)). Já na questão 4 o acoplamento é implícito e livre. As classes não sabem da existência de 
"Imprimivel" e não herdam nada dela, mantendo-se totalmente independentes.
"""
