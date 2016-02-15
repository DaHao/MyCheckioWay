def checkio(number):
    print()
    portion = []
    cost_portion = []
    #portion 
    temp = 0
    for index in range(1, number+1):
        index += temp
        temp = index
        portion.append(index)
    
    print(portion)
    temp = 0
    for cost in portion:
        cost += temp
        temp = cost
        cost_portion.append(cost)

    result = 0
    
    index = 0
    for item in cost_portion:
        if number <= item:
            break
        index += 1
        
    index = 0 if index == 0 else index - 1

    number -= cost_portion[index]

    if number >= portion[index]:
        result = number
    else:
        result = portion[index]
    
    return result

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"