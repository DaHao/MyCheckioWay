def checkio(game_result):

    result = 'D'
    for row in game_result:
        if all( x == 'X' for x in row ):
            result = 'X'
            break
        if all( x == 'O' for x in row ):
            result = 'O'
            break
            
    if (game_result[0][0] == game_result[1][0] == game_result[2][0])  and (game_result[0][0] != '.'):
        result = game_result[0][0]
    elif (game_result[0][1] == game_result[1][1] == game_result[2][1]) and (game_result[0][1] != '.'):
        result = game_result[0][1]
    elif (game_result[0][2] == game_result[1][2] == game_result[2][2])  and (game_result[0][2] != '.'):
        result = game_result[0][2]
    elif (game_result[0][0] == game_result[1][1] == game_result[2][2])  and (game_result[0][0] != '.'):
        result = game_result[0][0]
    elif (game_result[0][2] == game_result[1][1] == game_result[2][0])  and (game_result[0][2] != '.'):
        result = game_result[0][2]
    
    
    return result

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"

