def checkio(text):
    FindLetter = {}
    for letter in text:
        if letter.isalpha():
            FindLetter[letter.lower()] = FindLetter.get(letter.lower(), 0) +1

    result = ''
    maxValue = 0
    for k, v in FindLetter.items():
        if v > maxValue or ( v == maxValue and result > k ):
            result = k
            maxValue = v
            
    return result

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
