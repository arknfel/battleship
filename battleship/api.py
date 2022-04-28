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

        # save board for future requests to load
        session['board'] = pickle.dumps(board)

        return jsonify('New Game Started'), HTTPStatus.OK

    except Exception as e:
        return jsonify(f'{e}'), HTTPStatus.BAD_REQUEST


@app.route('/battleship', methods=['PUT'])
def shot():
    try:
        coords = request.get_json()
        
        # load recent board status
        board = pickle.loads(session['board'])
        
        # compute outcome after the shot
        outcome = shoot(coords, board)

        # save new board status
        session['board'] = pickle.dumps(board)

        return jsonify(f'{outcome}'), HTTPStatus.OK

    except KeyError:
        return jsonify(f'No game was created'), HTTPStatus.BAD_REQUEST

    except Exception as e:
        return jsonify(f'{e}'), HTTPStatus.BAD_REQUEST


@app.route('/battleship', methods=['DELETE'])
def delete_battleship_game():

    if 'board' in session:
        del session['board']

        return jsonify('Game Deleted'), HTTPStatus.OK
    return jsonify('No game to delete'), HTTPStatus.OK
