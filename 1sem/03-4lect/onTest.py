def fast_pow(base:int, exponent:int)->int:
    counter = exponent; _base = base; result = 1
    while(counter != 0):
        if counter % 2 == 0:
            counter //= 2
            _base *= _base
        else:
            counter -= 1
            result *= _base
    return result

