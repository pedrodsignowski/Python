def main():
    menuOpcoes()
    

def menuOpcoes():
    texto = """Você quer converter de:
1 -- Binário para octal
2 -- Binário para decimal
3 -- Binário para hexadecimal
4 -- Octal para binário 
5 -- Octal para decimal 
6 -- Decimal para binário
7 -- Decimal para octal
8 -- Decimal para hexadecimal 
9 -- Hexadecimal para binário
10 -- Hexadecimal para decimal 
Max Verstappen -- Sair """        
    print(texto)
    opcoes = input(" ")
    parar = True
    while  parar == True:
        if ("1" or "2" or "3") in opcoes:
            int(opcoes)
            binarioParaOutras(opcoes)
            parar = False
        elif ("4" or "5") in opcoes:
            int(opcoes)
            octalParaOutras(opcoes)
            parar = False
        elif ("6" or "7" or "8") in opcoes:
            int(opcoes)
            decimalParaOutras(opcoes)
            parar = False
        elif ("9" or "10") in opcoes:
            int(opcoes)
            hexaParaOutras(opcoes)
            parar = False
        elif opcoes =="Max Verstappen":
            print("deletando system32 em:") #Sair
            for i in range (0,11):
               print(i) 
            parar = False        


def pedirNumero():
    numero = input("Fala um numéro ai ")
    if "," or "." in numero:
        texto = numero.find("," or ".")
        parteInteira = numero[0: texto -1]
        parteDecimal = numero[texto + 1: len(numero)]
        try:
            tamanhoParteInteira = len(parteInteira)
            tamanhoParteDecimal = len(parteDecimal)
            return int(parteInteira), int(parteDecimal), tamanhoParteInteira, tamanhoParteDecimal
        except:
            print("Abobrinha")
    else:
        print("texto")

def binarioParaOutras(opcoes):
    if opcoes =="1":
        base = 8
    elif opcoes =="2":
        base = 10
    else:
        base = 16
    parteInteira,parteDecimal = pedirNumero()


def octalParaOutras(opcoes):
    if opcoes == "4":
        base = 2
    elif opcoes == "5":
        base = "10"
    parteInteira,parteDecimal = pedirNumero()


def decimalParaOutras(opcoes):
    if opcoes == "6":
        base = 2
    elif opcoes == "7":
        base = 8
    else:
        base = 16
    parteInteira,parteDecimal,tamanhoParteInteira, tamanhoParteDecimal = pedirNumero()
    nConvertido=[None]
    for i in range(0, tamanhoParteInteira):
        nConvertido.append(parteInteira % base)
    nConvertido.remove(None)
    print(nConvertido)
    
def hexaParaOutras(opcoes):
    if opcoes == "9":
        base = 2
    else:
        base = 10
    parteInteira,parteDecimal = pedirNumero()
    

main()
