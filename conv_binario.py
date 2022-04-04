from adicional import switch_hex

#TA PRONTO TOTALMENTE FUNCIONAL SHOW DE BOLA

def binario(n, s):
    res = 0
    bin = [int(i) for i in n]
    bin = bin[::-1]
    if s == 5:
        h = 4
    else:
        h = 3
    if s == 2 or s == 5:
        res = []
        res2 = []
        res3 = 0
        for i in range(len(bin)):
            res.append(bin[i])
            if len(res) == h or (i+1) == len(bin):
                for z in range(len(res)):
                    res3 += res[z] * (2**z)
                res2.append(res3)
                res = []
                res3 = 0
        if s == 5:
            return res2[::-1]
        else:
            res2 = [str(i) for i in res2[::-1]]
            res = ''.join(res2)
            return int(res)

    elif s == 3:
        for i in range(len(bin)):
            res += (bin[i] * (2**i))
        return res
            
    elif s == 4:
        res = binario(n, 5)
        res2 = []
        for i in range(len(res)):
            res2.append(switch_hex(res[i], 2))
        return ''.join(res2)
    else:
        return "error"
