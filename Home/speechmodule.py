FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):

    result = ''
    if len( str(number) ) == 3:
        result = FIRST_TEN[number//100 -1] + ' ' + HUNDRED
        CalNo = number % 100
        if CalNo == 0:
            pass
        elif 0 < CalNo < 10:
            result = result + ' ' + FIRST_TEN[CalNo - 1]
        elif CalNo < 20:
            result = result + ' ' + SECOND_TEN[CalNo%10]
        elif CalNo < 100 and CalNo%10 == 0:
            result = result + ' ' + OTHER_TENS[CalNo//10 - 2]
        else:
            result = result + ' ' + OTHER_TENS[CalNo//10 - 2] + ' ' + FIRST_TEN[(CalNo % 10) - 1]
    elif len( str(number) ) == 2:
        if number < 20:
            result = SECOND_TEN[number%10]
        elif number < 100 and number%10 == 0:
            result = OTHER_TENS[number//10 - 2]
        else:
            result = OTHER_TENS[number//10 - 2] + ' ' + FIRST_TEN[(number % 10) - 1]
    else:
        result = FIRST_TEN[number - 1]

    return result

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
