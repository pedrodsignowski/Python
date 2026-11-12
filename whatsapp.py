
# Número de pontos da vírgula

def main():  # Função principal do programa
    menuOpcoes()  # Chama o menu de opções


def menuOpcoes():  # Função responsável pelo menu
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

    while True:  # Mantém o menu funcionando
        print(texto)  # Exibe o menu
        opcoes = input("Escolha uma opção: ").strip()  # Recebe a opção

        if opcoes in ["1", "2", "3"]:  # Verifica as opções binárias
            binarioParaOutras(opcoes)  # Chama a função correspondente

        elif opcoes in ["4", "5"]:  # Verifica as opções octais
            octalParaOutras(opcoes)  # Chama a função correspondente

        elif opcoes in ["6", "7", "8"]:  # Verifica as opções decimais
            decimalParaOutras(opcoes)  # Chama a função correspondente

        elif opcoes in ["9", "10"]:  # Verifica as opções hexadecimais
            hexaParaOutras(opcoes)  # Chama a função correspondente

        elif opcoes == "Max Verstappen":  # Verifica se deseja sair
            print("Saindo do programa...")  # Exibe mensagem de saída
            break  # Encerra o programa

        else:  # Caso a opção não exista
            print("Opção inválida!")  # Informa o erro


def pedirNumero(base):  # Função para receber e validar o número
    digitos = "0123456789ABCDEF"  # Define os caracteres possíveis

    while True:  # Repete até receber um número válido
        numero = input("Fala um número aí: ").replace(",", ".").upper()  # Recebe o número

        if numero.count(".") > 1:  # Verifica se existem vários pontos
            print("Número inválido!")  # Informa o erro
            continue  # Solicita novamente

        if not numero or numero == ".":  # Verifica se está vazio
            print("Número inválido!")  # Informa o erro
            continue  # Solicita novamente

        numeroVerificar = numero.lstrip("-")  # Remove o sinal negativo para validar

        if not numeroVerificar:  # Verifica se existe apenas o sinal
            print("Número inválido!")  # Informa o erro
            continue  # Solicita novamente

        if any(c not in digitos[:base] and c != "." for c in numeroVerificar):  # Verifica os dígitos
            print("Número inválido para essa base!")  # Informa o erro
            continue  # Solicita novamente

        if numero.endswith("."):  # Verifica se termina com ponto
            print("Número inválido!")  # Informa o erro
            continue  # Solicita novamente

        return numero  # Retorna o número validado


def binarioParaOutras(opcoes):  # Conversões que começam em binário
    if opcoes == "1":  # Binário para octal
        base = 8  # Define a base de destino
    elif opcoes == "2":  # Binário para decimal
        base = 10  # Define a base de destino
    else:  # Binário para hexadecimal
        base = 16  # Define a base de destino

    funcaoQueConverte(2, base)  # Executa a conversão


def octalParaOutras(opcoes):  # Conversões que começam em octal
    if opcoes == "4":  # Octal para binário
        base = 2  # Define a base de destino
    else:  # Octal para decimal
        base = 10  # Define a base de destino

    funcaoQueConverte(8, base)  # Executa a conversão


def decimalParaOutras(opcoes):  # Conversões que começam em decimal
    if opcoes == "6":  # Decimal para binário
        base = 2  # Define a base de destino
    elif opcoes == "7":  # Decimal para octal
        base = 8  # Define a base de destino
    else:  # Decimal para hexadecimal
        base = 16  # Define a base de destino

    funcaoQueConverte(10, base)  # Executa a conversão


def hexaParaOutras(opcoes):  # Conversões que começam em hexadecimal
    if opcoes == "9":  # Hexadecimal para binário
        base = 2  # Define a base de destino
    else:  # Hexadecimal para decimal
        base = 10  # Define a base de destino

    funcaoQueConverte(16, base)  # Executa a conversão


def funcaoQueConverte(baseOrigem, baseDestino):  # Função principal de conversão
    numero = pedirNumero(baseOrigem)  # Recebe o número na base de origem

    digitos = "0123456789ABCDEF"  # Define os caracteres das bases

    sinal = ""  # Inicializa o sinal

    if numero.startswith("-"):  # Verifica se o número é negativo
        sinal = "-"  # Guarda o sinal negativo
        numero = numero[1:]  # Remove o sinal do número

    partes = numero.split(".")  # Separa a parte inteira da decimal

    parteInteira = partes[0]  # Guarda a parte inteira

    if len(partes) == 2:  # Verifica se existe parte decimal
        parteDecimal = partes[1]  # Guarda a parte decimal
    else:  # Caso não exista parte decimal
        parteDecimal = ""  # Define a parte decimal como vazia

    # Começa a parte que converte a parte inteira

    valorInteiro = int(parteInteira, baseOrigem)  # Converte a parte inteira para decimal

    resto = []  # Cria uma lista para armazenar os restos

    if valorInteiro == 0:  # Verifica se o número é zero
        resto.append("0")  # Adiciona zero ao resultado

    while valorInteiro >= baseDestino:  # Repete enquanto o valor for maior que a base
        resto.append(digitos[valorInteiro % baseDestino])  # Armazena o resto
        valorInteiro //= baseDestino  # Divide o valor pela base

    if valorInteiro > 0:  # Verifica se ainda existe um valor
        resto.append(digitos[valorInteiro])  # Adiciona o último dígito

    resto = list(reversed(resto))  # Inverte a lista para obter a ordem correta

    # Fim da parte que converte a parte inteira

    # Começo da parte que converte depois da vírgula

    valorDecimal = 0  # Inicializa o valor decimal

    for i in range(len(parteDecimal)):  # Percorre os dígitos decimais
        valorDecimal += digitos.index(parteDecimal[i]) / (baseOrigem ** (i + 1))  # Calcula o valor decimal

    restoDepoisDaVirgula = []  # Cria uma lista para armazenar os dígitos decimais

    for i in range(5):  # Limita a conversão a cinco casas decimais
        valorDecimal *= baseDestino  # Multiplica pela base de destino
        digito = int(valorDecimal)  # Obtém a parte inteira
        restoDepoisDaVirgula.append(digitos[digito])  # Armazena o dígito convertido
        valorDecimal -= digito  # Remove a parte inteira

    # Fim da parte que converte depois da vírgula

    resultado = sinal + "".join(resto)  # Junta o sinal e a parte inteira

    if parteDecimal:  # Verifica se o número original tinha parte decimal
        resultado += "." + "".join(restoDepoisDaVirgula)  # Adiciona a parte decimal

    print("Resultado:", resultado)  # Exibe o resultado da conversão
    print("")


main()  # Inicia o programa


# Pedro e Gabriel 101 Info
