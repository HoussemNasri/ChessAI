import chess
import AI

board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
ai = AI.AI(board)


def getHumanMove():
    return chess.Move.from_uci(str(input()))


def getAIMove():
    return ai.selectmove(4)


def getRandomMove():
    pass


print(board)
while not board.is_game_over():
    print()
    print("Human: ", end='')
    h = getHumanMove()

    while not board.is_legal(h):
        print("Warning! Illegal move")
        print("Human: ", end='')
        h = getHumanMove()
    board.push(h)

    print(board)
    if board.is_game_over():
        break
    print("\nLoding...")
    print("AI: ", end='')
    AIMove = getAIMove()
    print(AIMove)
    if board.is_legal(AIMove):
        board.push(AIMove)
    else:
        print("FATAL ERROR! The AI is broken")
        exit(-1)
    print(board)

print(board)
