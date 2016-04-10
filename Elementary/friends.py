class Friends:
    conn = []
    def __init__(self, connections):
        for x in connections:
            if x not in self.conn:
                self.conn.append(x)

    def add(self, connection):
        result = connection not in self.conn
        if result:
            self.conn.append(connection)
        return result

    def remove(self, connection):
        result = connection in self.conn
        if result:
            self.conn.remove(connection)
        return result

    def names(self):
        result = set()
        for x in self.conn:
            result |= x
        return result

    def connected(self, name):
        result = set()
        for x in self.conn:
            if name in x:
                result |= x
                
        if name in result:
            result.remove(name)
            
        return result



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"
