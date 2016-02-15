def checkio(first, second):
    first = { x for x in first.split(',') }
    second = { y for y in second.split(',') }

    t = list(first & second)
    t.sort()
    return ','.join(t)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"
