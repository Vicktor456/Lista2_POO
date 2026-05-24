from questao5 import Armazenador, ArmazenadorArquivo, ArmazenadorBanco, Salvavel, ArmazenadorNuvem, executar_salvamento_formal, executar_salvamento_flexivel

arquivo1 = ArmazenadorArquivo()
banco1 = ArmazenadorBanco()
nuvem1 = ArmazenadorNuvem()

print("\nTESTANDO ABORDAGEM FORMAL (ABC)\n")

executar_salvamento_formal(arquivo1, "Backup") # Funciona (herda de ABC)
executar_salvamento_formal(banco1, "Backup") # Funciona (herda de ABC)
executar_salvamento_formal(nuvem1, "Backup")  # Falha (não herda de ABC)

print("\nTESTANDO ABORDAGEM FLEXÍVEL (Protocol)\n")

executar_salvamento_flexivel(arquivo1, "Backup") # Funciona (tem o método salvar)
executar_salvamento_flexivel(banco1, "Backup") # Funciona (tem o método salvar)
executar_salvamento_flexivel(nuvem1, "Backup")   # Funciona (tem o método salvar)
