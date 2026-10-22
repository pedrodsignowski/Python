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
        if opcoes == 1:
            binarioParaOutras(8)
            parar = False
        elif opcoes ==2:
            binarioParaOutras(10)
            parar = False
        elif opcoes == 3:
            binarioParaOutras(16)
            parar = False
        elif opcoes ==4:
            octalParaOutras(2)
            parar = False
        elif opcoes ==5:
            octalParaOutras(10)
            parar = False
        elif opcoes ==6:
            decimalParaOutras(2)
            parar = False
        elif opcoes ==7:
            decimalParaOutras(8)
            parar = False
        elif opcoes ==8:
            decimalParaOutras(16)
            parar = False
        elif opcoes ==9:
            hexaParaOutras(10)
            parar = False
        elif opcoes ==10:
            hexaParaOutras()
            parar = False
        elif opcoes =="Max Verstappen":
            print("deletando system32 em:") #Sair
            for i in range (0,11):
               print(i) 
            parar = False        


def pedirNumero():
    numero = input("Fala um numéro ai")
    if "," or "." in numero:
        texto = numero.find("," or ".")
        parteInteira = numero[0, texto -1]
        parteDecimal = numero[texto + 1, len(numero)]
        return parteInteira, parteDecimal
    else:
        print("texto")

def binarioParaOutras(base):
    parteInteira,parteDecimal = pedirNumero()
    print(parteInteira)
    print(parteDecimal)

def octalParaOutras(base):
    parteInteira,parteDecimal = pedirNumero()


def decimalParaOutras(base):
    parteInteira,parteDecimal = pedirNumero()

    
def hexaParaOutras(base):
    parteInteira,parteDecimal = pedirNumero()
    

main()
