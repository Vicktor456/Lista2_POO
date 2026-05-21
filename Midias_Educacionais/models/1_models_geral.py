from abc import ABC, abstractmethod 

class Midia(ABC):
    def __init__(self, titulo, duracao):

        self.titulo = titulo
        self.duracao = duracao

    def mostrar_info(self):
        return f"O titulo é {self.titulo} e tem duração de {self.duracao}"

    @abstractmethod
    def reproduzir(self):
        pass

class Video(Midia):
    def __init__(self, titulo, duracao, resolucao):
        super().__init__(titulo, duracao)

        self.resolucao = resolucao

    def reproduzir(self):
        return f"Reproduzindo o video {self.titulo} com duração de {self.duracao} na resolução de {self.resolucao}" 
                                                                
class Podcast(Midia):
    def __init__(self, titulo, duracao, apresentador):
        super().__init__(titulo, duracao)

        self.apresentador = apresentador

    def reproduzir(self):
        return f"Reproduzindo o podcast {self.titulo} com duração de {self.duracao} sendo apresentado por {self.apresentador}"

class TextoNarrado(Midia):
    def __init__(self, titulo, duracao, idioma):
        super().__init__(titulo, duracao)

        self.idioma = idioma

    def reproduzir(self):
        return f"Reproduzindo o texto narrado {self.titulo} com duração de {self.duracao} no idioma {self.idioma}"

class Plataforma:
    def __init__(self, nome):

        self.nome = nome
        self.lista_midia = []

    def adicionar_midia(self, midia):
        self.lista_midia.append(midia)

    def listar_midias(self):
        print(f"\n=== Midias da Plataforma {self.nome} ===")
        for i in self.lista_midia:
            print(i.mostrar_info())

    def reproduzir_todas(self):
        print(f"\n--- Iniciando {self.nome} ---")
        if not self.lista_midia:
            print("Nenhuma midia disponivel para reprodução.")
        else:
            for j in self.lista_midia:
                print(j.reproduzir())
