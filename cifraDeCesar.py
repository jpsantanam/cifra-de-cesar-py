def cifra(mensagem, deslocamento, direcao):
    mensagemFinal = ""
    if direcao == "descriptografar":
        deslocamento = -deslocamento
    for letra in mensagem:
        if letra in alfabeto:
            indiceLetra = alfabeto.index(letra)
            indiceRotacao = (indiceLetra + deslocamento) % 26
            mensagemFinal += alfabeto[indiceRotacao]
        else:
            mensagemFinal += letra
    print(f"A mensagem final é {mensagemFinal}")


alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
            "r", "s", "t", "u", "v", "w", "x", "y", "z"]
deveContinuar = True

while deveContinuar:
    direcaoUsuario = input("Você deseja criptografar ou descriptografar uma mensagem? ")
    while direcaoUsuario not in ["criptografar", "descriptografar"]:
        direcaoUsuario = input("Digite apenas 'criptografar' ou 'descriptografar': ")
    mensagemUsuario = input(f"Qual mensagem você deseja {direcaoUsuario}? ").lower()
    deslocamentoUsuario = int(input("Qual é o número de deslocamento? "))

    cifra(mensagemUsuario, deslocamentoUsuario, direcaoUsuario)
    deveContinuar = input("Deseja continuar? ").lower() == "sim"
