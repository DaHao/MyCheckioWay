def checkio(words_set):
    
    for tail in words_set:
        
        for word in words_set:
            tail_len = len(tail)
            word_len = len(word)
            
            if tail == word:
                continue
            
            if tail == word[word_len-tail_len:]:
                return True

    return False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio({"hello", "lo", "he"}) == True, "helLO"
    assert checkio({"hello", "la", "hellow", "cow"}) == False, "hellow la cow"
    assert checkio({"walk", "duckwalk"}) == True, "duck to walk"
    assert checkio({"one"}) == False, "Only One"
    assert checkio({"helicopter", "li", "he"}) == False, "Only end"
