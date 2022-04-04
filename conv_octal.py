from conv_binario import *
from conv_decimal import *

def octal(n, s):
    res = 0
    bin = [int(i) for i in n]
    bin = bin[::-1]

    if s == 1:
        bin = bin[::-1]
        res2 = ''
        res = []
        for i in range(len(bin)):
            res.append(decimalconv(bin[i], 1))
            while len(str(res[i])) < 3:
                res[i] = str(res[i])
                res[i] = '0' + res[i]

        res2 = ''.join(str(i) for i in res)
        return res2

    elif s == 3:
        for i in range(len(bin)):
            res += (bin[i] * (8**i))
        return res
        
    elif s == 4:
        n = octal(n, 3)
        res = decimalconv(n, 4)
        return res
    else:   
        return "error"
