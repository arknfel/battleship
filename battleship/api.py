import pickle
from http import HTTPStatus

from flask import Flask, jsonify, request, session

from battleship.controler import start, shoot


app = Flask(__name__)
app.secret_key = "UshallnotPASS"
app.debug = True

@app.route('/battleship', methods=['POST'])
def create_battleship_game():
    try:
        payload = request.get_json()

        board = start(payload['ships'])
        session['board'] = pickle.dumps(board)

        return jsonify({"msg": "New Game Started"}), HTTPStatus.OK

    except Exception as e:
        
        return jsonify(f'{e}'), HTTPStatus.BAD_REQUEST


@app.route('/battleship', methods=['PUT'])
def shot():
    try:
        coords = request.get_json()

        board = pickle.loads(session['board'])
        outcome = shoot(coords, board)

        session['board'] = pickle.dumps(board)

        return jsonify(f'{outcome}'), HTTPStatus.OK

    except Exception as e:
        return jsonify(f'{e}'), HTTPStatus.BAD_REQUEST


@app.route('/battleship', methods=['DELETE'])
def delete_battleship_game():
    if 'board' in session:
        del session['board']
        return jsonify(f'Game Deleted'), HTTPStatus.OK

    return jsonify(f'No game to delete'), HTTPStatus.OK
