#Nunero de po is d a vi r gu la
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
    while True:
        try:
            numero = input("Fala um numéro ai ").replace(",",".") 
            if  "." in numero:        
                texto = numero.find(".")
                parteInteira = numero[0 :texto ]
                parteDecimal = numero[texto + 1: len(numero)]
                tamanhoParteInteira = len(parteInteira)
                tamanhoParteDecimal = len(parteDecimal)
                parteDecimal=int(parteDecimal)
                parteDecimal /=1000
                return int(parteInteira), parteDecimal, tamanhoParteInteira, tamanhoParteDecimal
                break
            else:
                parteInteira = numero[0:len(numero)]
                return int(parteInteira),0,0,tamanhoParteDecimal # Retorno padrão para caso não tiver virgula o programa não quebrar
        except:
            return 0,0,0,0
            print("Fale um numéro aí ")
            break


def binarioParaOutras(opcoes):
    if opcoes =="1":
        base = 8
        funcaoQueConverte(base)
    elif opcoes =="2":
        base = 10
        funcaoQueConverte(base)
    else:
        base = 16
        funcaoQueConverte(base)


def octalParaOutras(opcoes):
    if opcoes == "4":
        base = 2
        funcaoQueConverte(base)
        funcaoQueConverte(base)
    elif opcoes == "5":
        base = 10
        funcaoQueConverte(base)
    


def decimalParaOutras(opcoes):
    if opcoes == "6":
        base = 2
        funcaoQueConverte(base)
    elif opcoes == "7":
        base = 8
        funcaoQueConverte(base)
    else:
        base = 16
        funcaoQueConverte(base)



def hexaParaOutras(opcoes):
    if opcoes == "9":
        base = 2
        funcaoQueConverte(base)
    else:
        base = 10
        funcaoQueConverte(base)



def funcaoQueConverte(base):
    parteInteira,parteDecimal,tamanhoParteInteira, tamanhoParteDecimal = pedirNumero()
    #Começa a parte que converte a parte inteira
    resto = []
    while parteInteira>= base:
        resto.append(parteInteira % base) # Obtém o resto
        parteInteira //= base # Obtém o quociente

    
    resto.append(parteInteira)
    resto = reversed(resto)
    resto = list(resto)
    #Fim da parte que converte a parte inteira
    #Começo da parte que converte depois da virgula
    restoDepoisDaVirgula = []
    
    quocienteDepoisDaVirgula = parteDecimal
    #Fique longe, zona do código radioativa

    for i in range(0,5):   
        parteDecimal = parteDecimal*base 
        if parteDecimal >1:
            restoDepoisDaVirgula.append(1)
            parteDecimal -=1
        else:
            restoDepoisDaVirgula.append(0)
    print(*resto ,  "", *restoDepoisDaVirgula)              

main()
