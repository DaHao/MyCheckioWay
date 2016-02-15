OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")

def boolean(x, y, operation):
    
    conj = lambda x, y: x and y 
    disj = lambda x, y: x or y 
    impl = lambda x, y: not x or y
    excl = lambda x, y: disj(x, y) and not conj(x, y)
    equi = lambda x, y: not excl(x, y)
    
    funs = [conj, disj, impl, excl, equi]
    
    return funs[OPERATION_NAMES.index(operation)](x, y)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert boolean(1, 0, "conjunction") == 0, "and"
    assert boolean(1, 0, "disjunction") == 1, "or"
    assert boolean(1, 1, "implication") == 1, "material"
    assert boolean(0, 1, "exclusive") == 1, "xor"
    assert boolean(0, 1, "equivalence") == 0, "same?"
