VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"

import re
def checkio(text):
    words = [ word for word in re.split(r'[^A-Za-z0-9]', text) if  word.isalpha() and len(word) > 1 ]
    result=0
    for word in words:
        if (all( w.upper() in VOWELS for w in word[::2]) and all( w.upper() in CONSONANTS for w in word[1::2] )) \
            or ( all( w.upper() in CONSONANTS for w in word[::2] ) and all( w.upper() in VOWELS for w in word[1::2] ) ):
            result += 1
        
            
    return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
