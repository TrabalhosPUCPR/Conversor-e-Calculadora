from conversor import converter

def calculate():

    print(f"{'-'*35} CALCULADORA {'-'*35}")
    

    print(f"\n(Use apenas + ou -) ")
    print(f"(Digite apos o numero entre parenteses a base do numero, sem base sera considerado decimal): ")
    print(f"Exemplo: A6D(16) + 5155(8) - 1011(2) - 327\n")

    i = input(f"Digite a equacao: ")

    res = calculo(i)

    print("\n"*1000)
    print(f'{"-"*35}RESULTADO{"-"*35}\n \n A equacao {i} tem como resultado:\n')
    print(f"Em binario: {converter(res, 3, 1)}")
    print(f"Em octal: {converter(res, 3, 2)}")
    print(f"Em decimal: {res}")
    print(f"Em hexadecimal: {converter(res, 3, 4)}")
    print(f'\n{"-"*80}')

def calculo(n):
    form = ['']
    z = 0
    for i in n:
        if i == "+" or i == "-":
            form.append(i)
            form.append('')
            z += 2
        elif i == "(":
            form.append(i)
            z += 1
        elif i != " ":
            form[z] += i

    convertpara = ''
    convertido = []
    operacao = ''
    resul = 0
    z = 0

    for i in range(len(form)):

        if form[i].startswith("(") or i+1 == len(form):
            if form[i] == "(2)":
                #binario
                convertido.append(converter(convertpara, 1, 3)) 
            elif form[i] == "(8)":
                #octal
                convertido.append(converter(convertpara, 2, 3))
            elif form[i] == "(16)":
                #hexadecimal
                convertido.append(converter(convertpara, 4, 3))
            elif i+1 == len(form):
                #decimal caso for o ultimo
                convertido.append(int(form[i]))
            else:
                #decimal
                convertido.append(int(convertpara))
            convertpara = ''

        elif form[i] == '+' or form[i] == '-':
            if convertpara == form[i-1]:
                convertido.append(int(convertpara))
                if len(convertido) > 1:
                    convertido, operacao = soma_sub(form, i, operacao, convertido)
            if form[i] == '+':
                operacao = '+'
            else:
                operacao = '-'
        else:
            convertpara = form[i]

        convertido, operacao = soma_sub(form, i, operacao, convertido)

    return convertido[0]

def soma_sub(form, i, operacao, convertido):
    if (len(convertido) > 1 or (i+1)==len(form)) and operacao == '+':
        convertido[0] += convertido[1]
        convertido.pop(1)
        operacao = ''
    elif  (len(convertido) > 1 or (i+1)==len(form)) and operacao == '-':
        convertido[0] -= convertido[1]
        convertido.pop(1)
        operacao = ''
    return convertido, operacao

