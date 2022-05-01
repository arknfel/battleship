import pickle
from http import HTTPStatus

from flask import Flask, jsonify, request, current_app

from battleship.controler import start, shoot


app = Flask(__name__)
# app.secret_key = "UshallnotPASS"
app.debug = True

@app.route('/battleship', methods=['POST'])
def create_battleship_game():

    try:
        payload = request.get_json()
        print(payload)

        board = start(payload['ships'])

        # session['board'] = pickle.dumps(board)
        current_app.board = board
        return jsonify('New Game Started'), HTTPStatus.OK

    except Exception as e:
        print(e)
        return jsonify(f'{e}'), HTTPStatus.BAD_REQUEST


@app.route('/battleship', methods=['PUT'])
def shot():
    try:
        coords = request.get_json()
        
        # board = pickle.loads(session['board'])
        board = current_app.board

        outcome = shoot(coords, board)

        # session['board'] = pickle.dumps(board)
        return jsonify({"result": f"{outcome}"}), HTTPStatus.OK

    except AttributeError as e:
        print(e)
        return jsonify(f'No game was created'), HTTPStatus.BAD_REQUEST

    # except Exception as e:
    #     print(e)
    #     return jsonify(f'{e}'), HTTPStatus.BAD_REQUEST


@app.route('/battleship', methods=['DELETE'])
def delete_battleship_game():

    if 'board' in current_app.__dict__:
        del current_app.board

        return jsonify('Game Deleted'), HTTPStatus.OK
    return jsonify('No game to delete'), HTTPStatus.BAD_REQUEST
