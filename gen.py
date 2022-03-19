import chess
import chess.engine
import random
import json

board = chess.Board()

engine = chess.engine.SimpleEngine.popen_uci(r'stockfish')
dict_norm = {}

while True:
    model_number = random.randrange(0, 1000000)

    while not board.is_game_over():
        try:
            board.push(random.choice(list(board.legal_moves)))
            print(board)

        except:
            move = engine.play(board, chess.engine.Limit(depth=20)).move
            
            board.push(move)
            print(board)

            dict_norm[str(move)] = str(board.shredder_fen())

            with open(f'./weights_norm_{model_number}.json', 'w+') as weights_file:
                json.dump(dict_norm, weights_file, indent=4)

        move = engine.play(board, chess.engine.Limit(depth=20)).move
            
        board.push(move)

        print(board)

        dict_norm[str(move)] = str(board.shredder_fen())

        with open(f'./weights_norm_{model_number}.json', 'w+') as weights_file:
                json.dump(dict_norm, weights_file, indent=4)
    
    board.clear()
    board.set_fen(chess.STARTING_FEN)

    while not board.is_game_over():
        try:
            move = engine.play(board, chess.engine.Limit(depth=20)).move
            
            board.push(move)
            print(board)

            dict_norm[str(move)] = str(board.shredder_fen())

            with open(f'./weights_norm_{model_number}.json', 'w+') as weights_file:
                json.dump(dict_norm, weights_file, indent=4)

        except:
            board.push(random.choice(list(board.legal_moves)))
            print(board)

        try:
            board.push(random.choice(list(board.legal_moves)))
            print(board)

        except:
            move = engine.play(board, chess.engine.Limit(depth=20)).move

            try:
                board.push(move)
                print(board)

                dict_norm[str(move)] = str(board.shredder_fen())

                with open(f'./weights_norm_{model_number}.json', 'w+') as weights_file:
                    json.dump(dict_norm, weights_file, indent=4)

            except:
                break
    
    board.clear()
    board.set_fen(chess.STARTING_FEN)
    
