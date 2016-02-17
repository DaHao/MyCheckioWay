import re

def checkio(data):

    #replace this for solution
    flag1 = False
    flag2 = False
    flag3 = False
    flag4 = False
    
    if len(data) >= 10:
        flag4 = True
    
    if (re.search("[a-z]+", data) != None):
        flag1 = True
    
    if (re.search("[A-Z]+", data) != None):
        flag2 = True;
        
    if(re.search("[0-9]+", data) != None):
        flag3 = True;
    
    if flag1 and flag2 and flag3 and flag4:
        return True;
    else:
        return False;

        
#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"

