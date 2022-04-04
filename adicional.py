def switch(n):
    escolhas = {
        1: 'binario',
        2: 'octal',
        3: 'decimal',
        4: 'hexadecimal',
    }
    return escolhas.get(n)


def switch_hex(n, e):
    if e == 1:
        escolhas = {
            'f': 15,
            'e': 14,
            'd': 13,
            'c': 12,
            'b': 11,
            'a': 10,
        }
    else:
        escolhas = {
            15: 'F',
            14: 'E',
            13: 'D',
            12: 'C',
            11: 'B',
            10: 'A',
        }            
    if n in ['a', 'b', 'c', 'd', 'e', 'f']:
        return escolhas.get(n)
    elif e != 1:
        if n > 9:
            return escolhas.get(n)
        else:
            return str(n)
    else: 
        return int(n)