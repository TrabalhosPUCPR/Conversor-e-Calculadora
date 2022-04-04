from adicional import switch_hex

def decimalconv(n, s):
    res = ''
    n = int(n)

    if s == 2:
        res = []
        while n > 0:
            resto = n % 8
            n = n / 8 
            n = int(n)
            res.append(resto)
        res = ''.join(str(i) for i in res[::-1])
        return int(res)

    elif s == 1:
        while n/2 > 0:
            if n % 2 == 1:
                res += str('1')
                n -= 1
            else:
                res += str('0')
            n = round(n/2)
        return res[::-1]

    elif s == 4:
        res = []
        while n > 0:
            resto = n % 16
            n = n/16
            n = int(n)
            res.append(switch_hex(resto, 2))
        
        res = ''.join(str(i) for i in res[::-1])
        return res
    else:
        return "error"
