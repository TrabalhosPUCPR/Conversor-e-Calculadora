from conv_binario import *
from conv_decimal import *
from conv_hexadecimal import *
from conv_octal import *
from adicional import switch

def msgconv():
    
    print(f"{'-'*35} CONVERSOR {'-'*35}\n")

    print(f'1 - Sistema binario\n')
    print(f'2 - Sistema octal\n')
    print(f'3 - Sistema decimal\n')
    print(f'4 - Sistema hexadecimal\n')

    sistema = int(input('Escolha sistema do numero que gostaria de converter: '))
    numero = input('Digite o numero que deseja converter: ')
    convert = input('Escolha o sistema que gostaria de converter o numero escolhido (deixe vazio para converter para todos os sistemas): ')

    print("\n"*1000)
    if convert != '':
        resu = converter(numero, sistema, int(convert))
        print(f'{"-"*35}RESULTADO{"-"*35}\n \n Convertendo o numero {switch(sistema)} {numero} para {switch(convert)} o resultado é {resu}\n \n{"-"*80}\n')
    else:
        resu = []
        for i in range(1, 5):
            if i != sistema:
                resu.append(converter(numero, sistema, i))
            else:
                resu.append(numero)


        print(f'{"-"*35}RESULTADO{"-"*35}\n \n Convertendo o numero {switch(sistema)} {numero} o resultado é:')
        print(f'- Binario: {resu[0]}')
        print(f'- Octal: {resu[1]}')
        print(f'- Decimal: {resu[2]}')
        print(f'- Hexadecimal: {resu[3]}')

def converter(numero, sistema, convert):

    if sistema == 1:
        res = binario(numero, convert)
    elif sistema == 2:
        res = octal(numero, convert)
    elif sistema == 3:
        res = decimalconv(numero, convert)
    elif sistema == 4:
        res = hexadecimal(numero, convert)
    else:
        print('Digite um numero valido')
        res = "erro"

    return res
