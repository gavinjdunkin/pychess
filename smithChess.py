"""
This is designed for text entry, modified smith notation
"""
board = [['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
         ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
         ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']]

turn = 0
history = []
color = 0
def move(board, move, color):
    letters = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}
    lettersIndex = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h'}
    iLocation = move[0:2]
    fLocation = move[len(move)- 2: len(move)]
    piece = boardCoordinates(board, iLocation)
    if isLegalMove(board, move, color):
        board[8-int(iLocation[1])][letters[iLocation[0]]] = ' '
        board[8-int(fLocation[1])][letters[fLocation[0]]] = piece
        if color == 0: color = 1
        elif color == 1: color = 0
        return board, color, ' '
    else:
        return board, color, 'Illegal move'

def isLegalMove(board, move, color):
    move = move.strip('n')
    iLocation = move[0:2]
    fLocation = move[len(move)- 2: len(move)]
    piece = boardCoordinates(board, iLocation)
    if color == 0 and piece.islower():
        return False
    if color == 1 and piece.isupper():
        return False
    if piece == ' ': return False
    if fLocation == iLocation: return False
    if piece == 'p' or piece == 'P':
        return pawnLegal(color, board, iLocation, fLocation)
    if piece == 'n' or piece == 'N':
        return knightLegal(color, board, iLocation, fLocation)
    if piece == 'b' or piece == 'B':
        return bishopLegal(color, board, iLocation, fLocation)
    if piece == 'r' or piece == 'R':
        return rookLegal(color, board, iLocation, fLocation)
    if piece == 'q' or piece == 'Q':
        return queenLegal(color, board, iLocation, fLocation)
    if piece == 'k' or piece == 'K':
        return kingLegal(color, board, iLocation, fLocation)
    
    
def threatened(board):
    blackThreatened = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    whiteThreatened = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    for i in range(len(board)):
        for k in range(len(board[i])):
            if board[i][k] == 'P':
                try: whiteThreatened[i-1][k+1] = 'P'
                except: pass
                try: whiteThreatened[i-1][k-1] = 'P'
                except: pass
            if board[i][k] == 'p':
                try: blackThreatened[i+1][k+1] = 'p'
                except: pass
                try: blackThreatened[i+1][k-1] = 'p'
                except: pass
            if board[i][k] == 'N':
                try: whiteThreatened[i+2][k+1] = 'N'
                except: pass
                try:
                    if i-2 >= 0: whiteThreatened[i-2][k+1] = 'N'
                except: pass
                try:
                    if k-1 >= 0: whiteThreatened[i+2][k-1] = 'N'
                except: pass
                try:
                    if k-1 >= 0 and i - 2 >= 0: whiteThreatened[i-2][k-1] = 'N'
                except: pass
                try: whiteThreatened[i+1][k+2] = 'N'
                except: pass
                try:
                    if i-1 >= 0: whiteThreatened[i-1][k+2] = 'N'
                except: pass
                try:
                    if k-2 >= 0: whiteThreatened[i+1][k-2] = 'N'
                except: pass
                try:
                    if i-1 >= 0 and k-2 >= 0: whiteThreatened[i-1][k-2] = 'N'
                except: pass
            if board[i][k] == 'n':
                try: blackThreatened[i+2][k+1] = 'n'
                except: pass
                try:
                    if i-2>=0: blackThreatened[i-2][k+1] = 'n'
                except: pass
                try:
                    if k-1>=0: blackThreatened[i+2][k-1] = 'n'
                except: pass
                try:
                    if i-2>=0 and k-1>=0: blackThreatened[i-2][k-1] = 'n'
                except: pass
                try: blackThreatened[i+1][k+2] = 'n'
                except: pass
                try:
                    if i-1>=0:blackThreatened[i-1][k+2] = 'n'
                except: pass
                try:
                    if k-2>=0: blackThreatened[i+1][k-2] = 'n'
                except: pass
                try:
                    if i-1>=0 and k-2>=0: blackThreatened[i-1][k-2] = 'n'
                except: pass
            if board[i][k] == 'B':
                for j in range(1,8):
                    try:
                        whiteThreatened[i+j][k+j] = 'B'
                    except: break
                    if board[i+j][k+j] != ' ':
                        break
                
                for j in range(1,8):
                    if i-j >= 0:
                        try:  
                            whiteThreatened[i-j][k+j] = 'B'
                        except: break
                    
                        if board[i-j][k+j] != ' ':
                            break
                    else:
                        break
                
                for j in range(1,8):
                    if k-j >= 0:
                        try:
                            whiteThreatened[i+j][k-j] = 'B'
                        except: break
                    
                        if board[i+j][k-j] != ' ':
                            break
                    else:
                        break
                
                for j in range(1,8):
                    if i-j>=0 and k-j>=0:
                        try:
                            whiteThreatened[i-j][k-j] = 'B'
                        except: break
                    
                        if board[i-j][k-j] != ' ':
                            break
                    else:
                        break
                
            if board[i][k] == 'b':
                for j in range(1,8):
                    try:
                        blackThreatened[i+j][k+j] = 'b'
                    except: break
                    
                    if board[i+j][k+j] != ' ':
                        break
                
                for j in range(1,8):
                    if i-j >= 0:
                        try:
                            blackThreatened[i-j][k+j] = 'b'
                        except: break
                    
                        if board[i-j][k+j] != ' ':
                            break
                    else:
                        break
                
                for j in range(1,8):
                    if k-j >= 0:
                        try:
                            blackThreatened[i+j][k-j] = 'b'
                        except: break
                    
                        if board[i+j][k-j] != ' ':
                            break
                    else:
                        break
                
                for j in range(1,8):
                    if i-j>=0 and k-j>=0:
                        try:
                            blackThreatened[i-j][k-j] = 'b'
                        except: break
                    
                        if board[i-j][k-j] != ' ':
                            break
                    else:
                        break
                
            if board[i][k] == 'R':
                for j in range(1,8):
                    try:
                        whiteThreatened[i+j][k] = 'R'
                    except: break
                    
                    if board[i+j][k] != ' ':
                        break
                
                for j in range(1,8):
                    if i-j >= 0:
                        try:
                            whiteThreatened[i-j][k] = 'R'
                        except: break
                    
                        if board[i-j][k] != ' ':
                            break
                    else:
                        break
                
                for j in range(1,8):
                    try:
                        whiteThreatened[i][k+j] = 'R'
                    except: break
                    
                    if board[i][k+j] != ' ':
                        break
                
                for j in range(1,8):
                    if k-j >= 0:
                        try:
                            whiteThreatened[i][k-j] = 'R'
                        except: break
                    
                        if board[i][k-j] != ' ':
                            break
                    else: break
                
            if board[i][k] == 'r':
                for j in range(1,8):
                    try:
                        blackThreatened[i+j][k] = 'r'
                    except: break
                    
                    if board[i+j][k] != ' ':
                        break
                
                for j in range(1,8):
                    if i-j >= 0:
                        try:
                            blackThreatened[i-j][k] = 'r'
                        except: break
                    
                        if board[i-j][k] != ' ':
                            break
                    else:
                        break
                
                for j in range(1,8):
                    try:
                        blackThreatened[i][k+j] = 'r'
                    except: break
                    
                    if board[i][k+j] != ' ':
                        break
                
                for j in range(1,8):
                    if k-j >= 0:
                        try:
                            blackThreatened[i][k-j] = 'r'
                        except: break
                    
                        if board[i][k-j] != ' ':
                            break
                    else:
                        break
                
            if board[i][k] == 'Q':
                for j in range(1,8):
                    try:
                        whiteThreatened[i+j][k+j] = 'Q'
                    except: break
                    
                    if board[i+j][k+j] != ' ':
                        break
                
                for j in range(1,8):
                    if i-j >= 0:
                        try:
                            whiteThreatened[i-j][k+j] = 'Q'
                        except: break
                    
                        if board[i-j][k+j] != ' ':
                            break
                    else:
                        break
                
                for j in range(1,8):
                    if k-j >= 0:
                        try:
                            whiteThreatened[i+j][k-j] = 'Q'
                        except: break
                    
                        if board[i+j][k-j] != ' ':
                            break
                    else:
                        break
                
                for j in range(1,8):
                    if i-j>=0 and k-j>=0:
                        try:
                            whiteThreatened[i-j][k-j] = 'Q'
                        except: break
                    
                        if board[i-j][k-j] != ' ':
                            break
                    else: break
                
                for j in range(1,8):
                    try:
                        whiteThreatened[i+j][k] = 'Q'
                    except: break
                    
                    if board[i+j][k] != ' ':
                        break
                
                for j in range(1,8):
                    if i-j >= 0:
                        try:
                            whiteThreatened[i-j][k] = 'Q'
                        except: break
                    
                        if board[i-j][k] != ' ':
                            break
                    else:
                        break
                
                for j in range(1,8):
                    try:
                        whiteThreatened[i][k+j] = 'Q'
                    except: break
                    
                    if board[i][k+j] != ' ':
                        break
                
                for j in range(1,8):
                    if k-j >= 0:
                        try:
                            whiteThreatened[i][k-j] = 'Q'
                        except: break
                    
                        if board[i][k-j] != ' ':
                            break
                    else:
                        break
                
            if board[i][k] =='q':
                for j in range(1,8):
                    try:
                        blackThreatened[i+j][k+j] = 'q'
                    except: break
                    
                    if board[i+j][k+j] != ' ':
                        break
                
                for j in range(1,8):
                    if i-j >= 0:
                        try:
                            blackThreatened[i-j][k+j] = 'q'
                        except: break
                    
                        if board[i-j][k+j] != ' ':
                            break
                    else:
                        break
                
                for j in range(1,8):
                    if k-j >= 0:
                        try:
                            blackThreatened[i+j][k-j] = 'q'
                        except: break
                    
                        if board[i+j][k-j] != ' ':
                            break
                    else:
                        break
                
                for j in range(1,8):
                    if i-j>=0 and k-j>=0:
                        try:
                            blackThreatened[i-j][k-j] = 'q'
                        except: break
                    
                        if board[i-j][k-j] != ' ':
                            break
                    else:
                        break
                
                for j in range(1,8):
                    try:
                        blackThreatened[i+j][k] = 'q'
                    except: break
                    
                    if board[i+j][k] != ' ':
                        break
                
                for j in range(1,8):
                    if i-j >= 0:
                        try:
                            blackThreatened[i-j][k] = 'q'
                        except: break
                    
                        if board[i-j][k] != ' ':
                           break
                    else:
                        break
                
                for j in range(1,8):
                    try:
                        blackThreatened[i][k+j] = 'q'
                    except: break
                    
                    if board[i][k+j] != ' ':
                        break
                
                for j in range(1,8):
                    if k-j >= 0:
                        try:
                            blackThreatened[i][k-j] = 'q'
                        except: break
                    
                        if board[i][k-j] != ' ':
                            break
                    else:
                        break
            if board[i][k] == 'K':
                try:
                    if whiteThreatened[i+1][k+1] == ' ': whiteThreatened[i+1][k+1] = 'K'
                except: pass
                try:
                    if whiteThreatened[i+1][k] == ' ': whiteThreatened[i+1][k] = 'K'
                except: pass
                try:
                    if whiteThreatened[i+1][k-1] == ' ' and k-1>=0: whiteThreatened[i+1][k-1] = 'K'
                except: pass
                try:
                    if whiteThreatened[i][k+1] == ' ': whiteThreatened[i][k+1] = 'K'
                except: pass
                try:
                    if whiteThreatened[i][k-1] == ' ' and k-1>=0: whiteThreatened[i][k-1] = 'K'
                except: pass
                try:
                    if whiteThreatened[i-1][k+1] == ' ' and i-1>=0: whiteThreatened[i-1][k+1] = 'K'
                except: pass
                try:
                    if whiteThreatened[i-1][k] == ' ' and i-1>=0: whiteThreatened[i-1][k] = 'K'
                except: pass
                try:
                    if whiteThreatened[i-1][k-1] == ' ' and i-1>=0 and k-1>=0: whiteThreatened[i-1][k-1] = 'K'
                except: pass
            if board[i][k] == 'k':
                try:
                    if blackThreatened[i+1][k+1] == ' ': blackThreatened[i+1][k+1] = 'k'
                except: pass
                try:
                    if blackThreatened[i+1][k] == ' ': blackThreatened[i+1][k] = 'k'
                except: pass
                try:
                    if blackThreatened[i+1][k-1] == ' ' and k-1>=0: blackThreatened[i+1][k-1] = 'k'
                except: pass
                try:
                    if blackThreatened[i][k+1] == ' ': blackThreatened[i][k+1] = 'k'
                except: pass
                try:
                    if blackThreatened[i][k-1] == ' ' and k-1>=0: blackThreatened[i][k-1] = 'k'
                except: pass
                try:
                    if blackThreatened[i-1][k+1] == ' ' and i-1>=0: blackThreatened[i-1][k+1] = 'k'
                except: pass
                try:
                    if blackThreatened[i-1][k] == ' ' and i-1>=0: blackThreatened[i-1][k] = 'k'
                except: pass
                try:
                    if blackThreatened[i-1][k-1] == ' ' and i-1>=0 and k-1>=0: blackThreatened[i-1][k-1] = 'k'
                except: pass
    #King can't defend what is attacked
    for i in range(len(whiteThreatened)):
        for k in range(len(whiteThreatened[i])):
            if whiteThreatened[i][k] == 'K' and blackThreatened[i][k] != ' ':
                whiteThreatened[i][k] == ' '
    for i in range(len(blackThreatened)):
        for k in range(len(blackThreatened[i])):
            if blackThreatened[i][k] == 'K' and whiteThreatened[i][k] != ' ':
                blackThreatened[i][k] == ' '
                
                
    return whiteThreatened, blackThreatened
                    
                
            
def pawnLegal(color, board, iLocation, fLocation):
    #one move forward
    if iLocation[0] == fLocation[0] and int(iLocation[1]) + 1 == int(fLocation[1]) and color == 0 and boardCoordinates(board, fLocation) == ' ':
        return True
    if iLocation[0] == fLocation[0] and int(iLocation[1]) - 1 == int(fLocation[1]) and color == 1 and boardCoordinates(board, fLocation) == ' ':
        return True
    #double pawn move
    if int(iLocation[1]) == 2 and int(iLocation[1]) + 2 == int(fLocation[1]) and color == 0 and boardCoordinates(board, fLocation) == ' ' and boardCoordinates(board, fLocation[0] + str(int(fLocation[1]) - 1)) == ' ':
        return True
    if int(iLocation[1]) == 7 and int(iLocation[1]) - 2 == int(fLocation[1]) and color == 1 and boardCoordinates(board, fLocation) == ' ' and boardCoordinates(board, fLocation[0] + str(int(fLocation[1]) + 1)) == ' ':
        return True
    #conditions in which the pawn takes
    if (iLocation[0] == leftFile(fLocation[0]) or iLocation[0] == rightFile(fLocation[0])) and int(iLocation[1]) + 1 == int(fLocation[1]) and color == 0 and boardCoordinates(board, fLocation).islower():
        return True
    if (iLocation[0] == leftFile(fLocation[0]) or iLocation[0] == rightFile(fLocation[0])) and int(iLocation[1]) - 1 == int(fLocation[1]) and color == 1 and boardCoordinates(board, fLocation).isupper():
        return True
    else:
        return False

def knightLegal(color, board, iLocation, fLocation):
    letters = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}
    lettersIndex = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h'}
    #right
    if ((iLocation[0] == lettersIndex[letters[fLocation[0]]+2] and int(iLocation[1]) + 1 == int(fLocation[1])) or (iLocation[0] == lettersIndex[letters[fLocation[0]]+2] and int(iLocation[1]) - 1 == int(fLocation[1]))) and ((boardCoordinates(board, fLocation).islower() and color == 0) or (boardCoordinates(board, fLocation).isupper() and color == 1) or boardCoordinates(board, fLocation) == ' '):
        return True
    #left
    if ((iLocation[0] == lettersIndex[letters[fLocation[0]]-2] and int(iLocation[1]) + 1 == int(fLocation[1])) or (iLocation[0] == lettersIndex[letters[fLocation[0]]-2] and int(iLocation[1]) - 1 == int(fLocation[1]))) and ((boardCoordinates(board, fLocation).islower() and color == 0) or (boardCoordinates(board, fLocation).isupper() and color == 1) or boardCoordinates(board, fLocation) == ' '):
        return True
    #up
    if ((iLocation[0] == lettersIndex[letters[fLocation[0]]-1] and int(iLocation[1]) + 2 == int(fLocation[1])) or (iLocation[0] == lettersIndex[letters[fLocation[0]]+1] and int(iLocation[1]) + 2 == int(fLocation[1]))) and ((boardCoordinates(board, fLocation).islower() and color == 0) or (boardCoordinates(board, fLocation).isupper() and color == 1) or boardCoordinates(board, fLocation) == ' '):
        return True
    #down
    if ((iLocation[0] == lettersIndex[letters[fLocation[0]]+1] and int(iLocation[1]) - 2 == int(fLocation[1])) or (iLocation[0] == lettersIndex[letters[fLocation[0]]-1] and int(iLocation[1]) - 2 == int(fLocation[1]))) and ((boardCoordinates(board, fLocation).islower() and color == 0) or (boardCoordinates(board, fLocation).isupper() and color == 1) or boardCoordinates(board, fLocation) == ' '):
        return True
    else:
        return False

def bishopLegal(color, board, iLocation, fLocation):
    letters = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}
    lettersIndex = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h'}
    #Not a diagonal
    if abs(int(fLocation[1]) - int(iLocation[1])) != abs(letters[fLocation[0]] - letters[iLocation[0]]):
        return False
    vertical = 1
    horizontal = 1
    if int(fLocation[1]) - int(iLocation[1]) > 0:
        vertical = 1
    if int(fLocation[1]) - int(iLocation[1]) < 0:
        vertical = 0
    if letters[fLocation[0]] - letters[iLocation[0]] > 0:
        horizontal = 1
    if letters[fLocation[0]] - letters[iLocation[0]] < 0:
        horizontal = 0
    #Up and to the right
    if vertical ==1 and horizontal == 1:
        for i in range(1,abs(int(fLocation[1]) - int(iLocation[1]))):
            if boardCoordinates(board, lettersIndex[letters[iLocation[0]] + i] + str(int(iLocation[1]) + i)) != ' ':
                return False
    #Down and to the left
    if vertical ==0 and horizontal == 0:
        for i in range(1,abs(int(fLocation[1]) - int(iLocation[1]))):
            if boardCoordinates(board, lettersIndex[letters[iLocation[0]] - i] + str(int(iLocation[1]) - i)) != ' ':
                return False
    #Up and to the left
    if vertical ==1 and horizontal == 0:
        for i in range(1,abs(int(fLocation[1]) - int(iLocation[1]))):
            if boardCoordinates(board, lettersIndex[letters[iLocation[0]] - i] + str(int(iLocation[1]) + i)) != ' ':
                return False
    #Down and to the right
    if vertical == 0 and horizontal == 1:
        for i in range(1,abs(int(fLocation[1]) - int(iLocation[1]))):
            if boardCoordinates(board, lettersIndex[letters[iLocation[0]] + i] + str(int(iLocation[1]) - i)) != ' ':
                return False
    #Ensuring open space or enemy piece
    if (boardCoordinates(board, fLocation).isupper() and color == 0) or (boardCoordinates(board, fLocation).islower() and color == 1):
        return False
    else:
        return True
    
def rookLegal(color, board, iLocation, fLocation):
    letters = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}
    lettersIndex = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h'}
    if abs(int(fLocation[1]) - int(iLocation[1])) > 0 and abs(letters[fLocation[0]] - letters[iLocation[0]]) > 0:
        return False
    direction = ''
    if int(fLocation[1]) - int(iLocation[1]) > 0:
        direction = 'up'
    if int(fLocation[1]) - int(iLocation[1]) < 0:
        direction = 'down'
    if letters[fLocation[0]] - letters[iLocation[0]] > 0:
        direction = 'left'
    if letters[fLocation[0]] - letters[iLocation[0]] > 0:
        direction = 'right'
    if direction == 'up':
        for i in range(1,abs(int(fLocation[1]) - int(iLocation[1])-1)):
            if boardCoordinates(board, iLocation[0] + str(int(iLocation[1]) + i)) != ' ':
                return False
    if direction == 'down':
        for i in range(1,abs(int(fLocation[1]) - int(iLocation[1])-1)):
            if boardCoordinates(board, iLocation[0] + str(int(iLocation[1]) - i)) != ' ':
                return False
    if direction == 'left':
        for i in range(1,abs(letters[fLocation[0]] - letters[iLocation[0]])):
            if boardCoordinates(board, lettersIndex[letters[iLocation[0]] + i] + iLocation[1]) != ' ':
                return False
    if direction == 'right':
        for i in range(1,abs(letters[fLocation[0]] - letters[iLocation[0]])):
            if boardCoordinates(board, lettersIndex[letters[iLocation[0]] - i] + iLocation[1]) != ' ':
                return False
    if (boardCoordinates(board, fLocation).isupper() and color == 0) or (boardCoordinates(board, fLocation).islower() and color == 1):
        return False
    else:
        return True

def queenLegal(color, board, iLocation, fLocation):
    letters = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}
    lettersIndex = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h'}
    if abs(int(fLocation[1]) - int(iLocation[1])) != abs(letters[fLocation[0]] - letters[iLocation[0]]) and ((abs(int(fLocation[1]) - int(iLocation[1])) > 0) and abs(letters[fLocation[0]] - letters[iLocation[0]]) > 0):
        return False
    if int(fLocation[1]) - int(iLocation[1]) > 0:
        vertical = 2
    if int(fLocation[1]) - int(iLocation[1]) < 0:
        vertical = 0
    if int(fLocation[1]) - int(iLocation[1]) == 0:
        vertical = 1
    if letters[fLocation[0]] - letters[iLocation[0]] > 0:
        horizontal = 2
    if letters[fLocation[0]] - letters[iLocation[0]] < 0:
        horizontal = 0
    if letters[fLocation[0]] - letters[iLocation[0]] == 0:
        horizontal = 1
    #up
    if vertical == 2 and horizontal == 1:
        for i in range(1,abs(int(fLocation[1]) - int(iLocation[1])-1)):
            if boardCoordinates(board, iLocation[0] + int(iLocation[1]) + i) != ' ':
                return False
    #down
    if vertical == 0 and horizontal == 1:
        for i in range(1,abs(int(fLocation[1]) - int(iLocation[1])-1)):
            if boardCoordinates(board, iLocation[0] + int(iLocation[1]) - i) != ' ':
                return False
    #left
    if vertical == 1 and horizontal == 0:
        for i in range(1,abs(letters[fLocation[0]] - letters[iLocation[0]])):
            if boardCoordinates(board, lettersIndex[letters[iLocation[0]] + i] + iLocation[1]) != ' ':
                return False
    #right
    if vertical == 1 and horizontal == 2:
        for i in range(1,abs(letters[fLocation[0]] - letters[iLocation[0]])):
            if boardCoordinates(board, lettersIndex[letters[iLocation[0]] - i] + iLocation[1]) != ' ':
                return False
    #up and to the right
    if vertical == 2 and horizontal == 2:
        for i in range(1,abs(int(fLocation[1]) - int(iLocation[1]))):
            if boardCoordinates(board, lettersIndex[letters[iLocation[0]] + i] + str(int(iLocation[1]) + i)) != ' ':
                return False
    #down and to the left
    if vertical == 0 and horizontal == 0:
        for i in range(1,abs(int(fLocation[1]) - int(iLocation[1]))):
            if boardCoordinates(board, lettersIndex[letters[iLocation[0]] - i] + str(int(iLocation[1]) - i)) != ' ':
                return False
    #up and to the left
    if vertical == 2 and horizontal == 0:
        for i in range(1,abs(int(fLocation[1]) - int(iLocation[1]))):
            if boardCoordinates(board, lettersIndex[letters[iLocation[0]] - i] + str(int(iLocation[1]) + i)) != ' ':
                return False
    #down and to the right
    if vertical == 0 and horizontal == 2:
        for i in range(1,abs(int(fLocation[1]) - int(iLocation[1]))):
            if boardCoordinates(board, lettersIndex[letters[iLocation[0]] + i] + str(int(iLocation[1]) - i)) != ' ':
                return False
    if (boardCoordinates(board, fLocation).isupper() and color == 0) or (boardCoordinates(board, fLocation).islower() and color == 1):
        return False
    else:
        return True

def kingLegal(color, board, iLocation, fLocation):
    letters = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}
    lettersIndex = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h'}
    whiteThreatened, blackThreatened = threatened(board)
    if abs(int(fLocation[1])-int(iLocation[1]))>1 or abs(letters[fLocation[0]] - letters[iLocation[0]])>1:
        return False
    if (boardCoordinates(blackThreatened, fLocation) != ' ' and color == 0) or (boardCoordinates(whiteThreatened, fLocation) != ' ' and color == 1):
        return False
    else:
        return True

def boardCoordinates(board, coordinate):
    file = coordinate[0]
    rank = int(coordinate[1])
    if file == 'a': return board[8-rank][0]
    if file == 'b': return board[8-rank][1]
    if file == 'c': return board[8-rank][2]
    if file == 'd': return board[8-rank][3]
    if file == 'e': return board[8-rank][4]
    if file == 'f': return board[8-rank][5]
    if file == 'g': return board[8-rank][6]
    if file == 'h': return board[8-rank][7]

def leftFile(file):
    if file == 'b': return 'a'
    if file == 'c': return 'b'
    if file == 'd': return 'c'
    if file == 'e': return 'd'
    if file == 'f': return 'e'
    if file == 'g': return 'f'
    if file == 'h': return 'g'
    else: return ''

def rightFile(file):
    if file == 'a': return 'b'
    if file == 'b': return 'c'
    if file == 'c': return 'd'
    if file == 'd': return 'e'
    if file == 'e': return 'f'
    if file == 'f': return 'g'
    if file == 'g': return 'h'
    else: return ''
color = 0
while True:
    for a in board:
        print(a)
    print('Enter Move:')
    moveInp = input()
    board, color, ret = move(board, moveInp, color)
    if ret == 'Illegal move':
        print(ret)
