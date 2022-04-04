from conversor import *
from calculadora import *

simsim = True

while simsim == True:

    print(f"{'-'*35} BOM DIA {'-'*35}")

    print(f"\nDigite o numero da acao que gostaria de fazer: ")
    print(f"\n1 - Conversao de sistema numeral")
    print(f"\n2 - Soma ou subtracao de sistemas numerais")
    print(f"\n3 - Creditos")
    print(f"\n4 - Sair\n")
    i = int(input('Numero: '))
    print("\n"*1000)

    if i == 1:
        msgconv()
    elif i == 2:
        calculate()
    elif i == 3:
        print(f"Feito por:\n\nLeonardo Matthew Knight\nFelipe Augusto Dittert Noleto ")
    elif i == 4:
        simsim = False
        print(f"\nTchau :(")
    else:
        print('Digite uma opcao valida')
    
    input(f"\nAperte enter para continuar")
    print("\n"*1000)
         


