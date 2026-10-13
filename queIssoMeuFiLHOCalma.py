import os
def menuOpcoes():
    condicao = False
    while condicao != True:
        print("Você quer converter de: ")
        print("1 -- Decimal para outras bases")
        print("2 -- Outras bases para decimal")
        opcoes = int(input(" "))
        if opcoes == 1:
            decimalParaOutras()
            condicao = True
        elif opcoes == 2:
            outrasParaDecimal()
            condicao = True
        else:
            print("Opção inválida, tente novamente")
            condicao = False
    
    
 
def outrasParaDecimal():
    ...


def decimalParaOutras():
    print("Suas opções são")
    print("1 -- Decimal para binário")
    print("2 -- Decimal para octal")
    print("3 -- Decimal para hexadecimal")
    opcoes = int(input("Escolha uma das opções através dos seus respectivos números "))
    if opcoes == 1:
        ...
    elif opcoes == 2:
        ...
    elif opcoes == 3:
        ...


def converterBinario(): ## Converte de decimal para binário
    decimal = None
    binario = input("Manda  um número em binário ")
    compriBinario = len(binario)## Usar no for  
    try:     
        for i in range(0, compriBinario):
            decimal = binario[i]
            decimal = int(decimal)*2**i
        print(decimal)
    except ValueError:
        print("Número inválido")


def converterOctal(): ## Converte de decimal para octal
    ...
def converterHexa(): ## Converte de decimal para hexadecimal
    ...