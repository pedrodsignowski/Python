a = 200
AoA = 0
terrainAhead = None
def retard ():
    global a 
    for i in range(13):
        if a > 100:
            print(a)
            a -= 100
        elif a <= 100 and a >= 10:
            print(a)
            a -= 10
        else:
            print("Retard")
            print("Retard")
def changeAoA():
    global AoA
    AoA = int(input("Mude o AoA de 1 em 1 "))
def alphaProt():
     global AoA
     if(AoA >=10):
            AoA = 10
            print("Alpha Prot ativado")
            print("Não pode exceder 10° de inclinação")
def alphaFloor():
    if(terrainAhead== True):
        print("Sistema alphaProt desativado")
def pullUp():
    global AoA
    global terrainAhead
    terrainAhead = True
    for AoA in range(5):
        if(AoA >= 0 and AoA < 3):
            changeAoA()
            print("Terrain ahead")
            print("Pull up")
            if(AoA >= 10):
                alphaProt() 
retard()