def check_connection(network, first, second):

    excludedList = []
    excludedList.append(first)
    searchList = []
    searchList.append(first)

    while searchList:
        nowNode = searchList.pop(0)
        searchList += FindNetworkString(network, nowNode, excludedList)
        if second in searchList:
            return True

    return False

def FindNetworkString(networkList, findStr, excludedList):
    resultList = []
    for item in networkList:
        friends = item.split('-')
        if findStr in friends:
            if friends[0] not in excludedList:
                resultList.append(friends[0])
                excludedList.append(friends[0])
            if friends[1] not in excludedList:
                resultList.append(friends[1])
                excludedList.append(friends[1])

    return list(set(resultList))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."
