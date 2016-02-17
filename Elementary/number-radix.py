def checkio(str_number, radix):
    radixStr = '0123456789abcdefghijklmnopqrstuvwxyz'
    
    result = 0
    for base, item in  enumerate(str_number[::-1]):
        if radixStr.index(item.lower()) >= radix:
            return -1
        result += int(radixStr.index(item.lower())) * radix**base
    return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("AF", 16) == 175, "Hex"
    assert checkio("101", 2) == 5, "Bin"
    assert checkio("101", 5) == 26, "5 base"
    assert checkio("Z", 36) == 35, "Z base"
    assert checkio("AB", 10) == -1, "B > A > 10"
