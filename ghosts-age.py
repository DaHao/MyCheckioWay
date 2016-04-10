def checkio(opacity):
    minus = 10000 - opacity
    result, x0, x1 = 0, 1, 2
    while minus:
        result += 1
        if(result == x0):
            minus = minus - x0
            x0, x1 = x1, x0 + x1
        else:
            minus += 1
        
    return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"