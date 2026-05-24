def executar_salvamento_formal(armazenador: Armazenador, dado) -> None:
    # [UI] Mensagem de apresentação visual no terminal
    print(f"Tentando salvamento formal para: {type(armazenador).__name__}")
    
    # [SERVICE] Lógica de verificação/regra de negócio da validação ABC
    if isinstance(armazenador, Armazenador):
        armazenador.salvar(dado)
    else:
        # [UI] Mensagem de feedback de erro visual para o usuário
        print(f"Erro: {type(armazenador).__name__} não pertence à hierarquia formal (ABC)")

def executar_salvamento_flexivel(objeto: Salvavel, dado) -> None:
    # [UI] Mensagem de apresentação visual no terminal
    print(f"Tentando flexível para: {type(objeto).__name__}")
    
    # [SERVICE] Lógica de validação da estrutura do objeto usando o Protocol
    if isinstance(objeto, Salvavel):
        objeto.salvar(dado)
    else:
        # [UI] Mensagem de feedback de erro visual para o usuário
        print(f"Erro Estrutural: {type(objeto).__name__} não possui a estrutura necessária")
