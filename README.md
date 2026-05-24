# Lista2_POO

# Padrões de Arquitetura: Models, Services, Repository & UI

O foco principal desse repositorio é demonstrar a separação de conceitos (*Separation of Concerns*) dividindo o código em quatro pilares essenciais: **Models**, **Services**, **Repository** e **UI**, além de explorar conceitos avançados de Orientação a Objetos como Classes Abstratas (`ABC`), Polimorfismo e Protocolos (`Duck Typing`).

---

## 📌 O que cada camada faz?

* **Models:** Representa as entidades de dados puras e as regras de negócio essenciais do objeto. Não exibe dados diretamente (sem `print`) e não sabe de onde os dados vêm.
* **Repository:** Camada de infraestrutura responsável única e exclusivamente por salvar, buscar e manipular coleções de dados (seja em memória, arquivos ou bancos de dados).
* **Services:** O "cérebro" do sistema. Orquestra o fluxo de dados, aplica validações globais e conecta a interface de usuário ao repositório correspondente.
* **UI (User Interface):** A camada de apresentação. É a única autorizada a interagir diretamente com o usuário por meio de entradas (`input`) e saídas (`print`).

## Pré-requisitos

Para rodar qualquer um dos códigos deste repositório, você precisará apenas do Python instalado em sua máquina. Versão do Python recomendada: Python 3.8 ou superior (necessário devido ao suporte nativo para typing.Protocol e @runtime_checkable).

## Como Executar e Reproduzir os Testes

Em cada pasta de questão tem o arquivo de código completo, nomeado com o mesmo nome da pasta, pode ser feito o download do arquivo ou apenas pode copiá-lo para ser feita a execução com IDE de sua preferencia. Para testa o fluxo de execução do código, basta baixar o arquivo main_"Nome da questao" do arquivo que deseja executar.
