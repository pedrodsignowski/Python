def main():
    menuOpcoes()


def menuOpcoes():
    condicao = False
    while condicao != True:
        print("Você quer converter de: ")
        print("1 -- Decimal para outras bases")
        print("2 -- Outras bases para decimal")
        opcoes = int(input(" "))
        while condicao != True:
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
    array = ["Suas opções são","1 -- Binário para decimal","2 -- Octal para decimal","3 -- Hexadecimal para decimal"]
    condicao = False
    while condicao != True:
        for i in range(0,len(array)):
            print(array[i]) 
        opcoes = int(input("Escolha uma das opções através dos seus respectivos números "))
        if opcoes not in  (1, 2, 3):
            print("Opção inválida, tente novamente!")
            condicao = False
        else:
            condicao = True
            if opcoes == 1:
                converterBinarioDecimal()
                    
            elif opcoes == 2:
                converterOctalDecimal()
            elif opcoes == 3:
                converterOctalDecimal()
                

def decimalParaOutras():
    array = ["Suas opções são:","1 -- Decimal para binário","2 -- Decimal para octal","3 -- Decimal para hexadecimal"]
    condicao = False
    while condicao != True:
        for i in range(0,len(array)):
            print(array[i])
        opcoes = int(input("Escolha uma das opções através dos seus respectivos números "))
        if opcoes not in (1, 2, 3):
            print("Opção inválida, tente novamente!")
            condicao = False
        else:
            condicao = True
            condicao1 = False
            while condicao1 != True:
                if opcoes == 1:
                    converterDecimalBinario()
                    condicao1 = True
            
                elif opcoes == 2:
                    converterDecimalOctal()
                    condicao1 = True
                
                elif opcoes == 3:
                    converterDecimalHexa()
                    condicao1 = True
            
            
    
def converterDecimalBinario(): ## Converte de decimal para binário
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


def converterDecimalOctal(): ## Converte de decimal para octal
    ...
def converterDecimalHexa(): ## Converte de decimal para hexadecimal
    ...
def converterBinarioDecimal():
    ...
def converterOctalDecimal():
    ...
def converterOctalDecimal():
    ...


main()