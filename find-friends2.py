#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      User
#
# Created:     12/12/2015
# Copyright:   (c) User 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def check_connection(network, first, second):
    print()
    chain = []
    token = network[0].split('-')
    chain.append( token )

    for node in network:
        token = node.split('-')
        flag = False
        for item in chain:
            if token[0] in item or token[1] in item:
                item +=  token
                flag = True

        if not flag:
            chain.append( token )

        print(chain)
        print()

    result = False
    for item in chain:
        if first in item and second in item:
            result = True

    return result


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("nikola-robin","batman-nwing","mr99-batman","mr99-robin",
         "dr101-out00","out00-nwing",),
         "dr101","mr99") == True

