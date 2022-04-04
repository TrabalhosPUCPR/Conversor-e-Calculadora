from conv_decimal import decimalconv
from adicional import switch_hex

def hexadecimal(n, s):
    n = n.lower()
    res = 0
    bin = [char for char in n]
    for i in range(len(bin)):
        bin[i] = switch_hex(bin[i], 1)
    bin = bin[::-1]
        
    if s == 2:
        n = hexadecimal(n, 3)
        n = decimalconv(n, 2)
        return n

    elif s == 3:
        for i in range(len(bin)):
            res += (bin[i] * (16**i))
        return res

    elif s == 1:
        res = []
        for i in bin:
            res.append(decimalconv(i, 1))
        for i in range(len(res)):
            while len(str(res[i])) < 4:
                res[i] = '0' + res[i]
                
        res = res[::-1]
        return ''.join(res)
    else:
        return "error"
