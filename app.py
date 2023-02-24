def converterBinario():
    textoDigitado = int( input("Digite um numero\n") )
    valorA = textoDigitado
    codigoBi = []

    while valorA != 0:
        codigoBi.append(str(valorA % 2))
        valorA = int( valorA  / 2 )

    codigoBiString = "".join(codigoBi)
    print("O numero " + str(textoDigitado) + " em binario fica " + str(codigoBiString))

def converterDecimal():
    codigoDigitado = input("Digite o seu Codigo binario\n\n")
    codigoDigitado = codigoDigitado[::-1]
    codigoDecimal = []
    numcaractere = 0
    for i in range(len(codigoDigitado)):
        resposta = int(codigoDigitado[i]) * (2**numcaractere)
        codigoDecimal.append(resposta)
        numcaractere = numcaractere + 1

    resposta = 0

    for j in codigoDecimal:
        resposta += j
    
    print("Seu codigo binario em decimal é: " + str(resposta))

def inicio():
    acao = input("Digite qual o meu metodo de conversão\n\n1- decimal para binario\n2- binario para decimal\n\n")

    if acao != "1" and acao != "2":
        inicio()

    if acao == "1":
        converterBinario()
    
    if acao == "2":
        converterDecimal()

inicio()