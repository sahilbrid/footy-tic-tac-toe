from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

class TicTacToe():
    def __init__(self):
        self.board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        self.current_player = 'X' if random.randint(0, 1) == 0 else 'O'

    def fix_spot(self, row, col):
        if self.board[row][col] == '-':
            self.board[row][col] = self.current_player
            return True
        else:
            return False

    def is_player_win(self, player):
        win = None
        n = len(self.board)
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n-1-i] != player:
                win = False
                break
        if win:
            return win
        return False

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def swap_player_turn(self):
        self.current_player = 'X' if self.current_player == 'O' else 'O'

    def get_current_player(self):
        return self.current_player

    def get_board(self):
        return self.board

game = TicTacToe()

@app.route('/move', methods=['POST'])
def move():
    data = request.json
    row, col = data['row'], data['col']
    if game.fix_spot(row, col):
        if game.is_player_win(game.get_current_player()):
            return jsonify({'status': 'win', 'player': game.get_current_player()})
        elif game.is_board_filled():
            return jsonify({'status': 'draw'})
        else:
            game.swap_player_turn()
            return jsonify({'status': 'continue', 'player': game.get_current_player()})
    else:
        return jsonify({'status': 'error', 'message': 'Spot already taken'})

@app.route('/board', methods=['GET'])
def get_board():
    return jsonify(game.get_board())

@app.route('/reset', methods=['POST'])
def reset():
    global game
    game = TicTacToe()
    return jsonify({'status': 'reset'})


if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

class TicTacToe():
    def __init__(self):
        self.board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        self.current_player = 'X' if random.randint(0, 1) == 0 else 'O'

    def fix_spot(self, row, col):
        if self.board[row][col] == '-':
            self.board[row][col] = self.current_player
            return True
        else:
            return False

    def is_player_win(self, player):
        win = None
        n = len(self.board)
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n-1-i] != player:
                win = False
                break
        if win:
            return win
        return False

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def swap_player_turn(self):
        self.current_player = 'X' if self.current_player == 'O' else 'O'

    def get_current_player(self):
        return self.current_player

    def get_board(self):
        return self.board

game = TicTacToe()

@app.route('/move', methods=['POST'])
def move():
    data = request.json
    row, col = data['row'], data['col']
    if game.fix_spot(row, col):
        if game.is_player_win(game.get_current_player()):
            return jsonify({'status': 'win', 'player': game.get_current_player()})
        elif game.is_board_filled():
            return jsonify({'status': 'draw'})
        else:
            game.swap_player_turn()
            return jsonify({'status': 'continue', 'player': game.get_current_player()})
    else:
        return jsonify({'status': 'error', 'message': 'Spot already taken'})

@app.route('/board', methods=['GET'])
def get_board():
    return jsonify(game.get_board())

if __name__ == '__main__':
    app.run(debug=True)
