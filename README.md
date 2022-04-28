# Battleship Solution

To clone repo:
```bash
git clone https://github.com/arknfel/battleship.git
```

## Summary

The main idea of this implementation is the hash-map attribute `occupied_cells` of class `Board`:

```python
class Board:

    def __init__(self, xrange, yrange):
        
        self.xrange = xrange
        self.yrange = yrange
        self.occupied_cells = {}

    def spawn(self, ship):
        self.occupied_cells.update(ship.cells)
```
An instance of class `Board` represents a game instance, keeping track of the game state, modifying the board instance per event/iteration (depending on the game engine design), will represent the game state changing vs time.

Instead of having to worry about a whole grid of MxN cells, untill the game gets more complex, we only need to worry about occupied cells and leave it to validators to make sure that the dimentions and coordinates of the ships and shots are within the grid, so that we can safely assume that if a shot's coordinates does not match any of the occupied cells, it is surely a missed shot "WATER".  

The idea here is to map each group of occupied cells to the corresponding occupying ship:
```python
board.occupied_cells = {
    '[1, 2]': ship_instance1,
    '[4, 2]': ship_instance2
    ...
}
```
This will enable us to easily map the shots coordinates to the ships (`O(1)`, `O(n)` time, space complixity respectively, where n is the number of occupied cells), then simply change the ship's condition accordingly, now let us take a look at the `Ship` model:
```python
class Ship:

    status = True

    def __init__(self, meta):

        self.x = meta['x']
        self.y = meta['y']
        self.size = meta['size']
        self.direction = meta['direction']

        if self.direction == 'H':

            self.cells = {[x, self.y].__str__(): self for x in range(self.x, self.x + self.size)}

        elif self.direction == 'V':

            self.cells = {[self.x, y].__str__(): self for y in range(self.y, self.y + self.size)}

        self.front = list(self.cells.keys())[0]
        self.rear = list(self.cells.keys())[-1]
```

At instantiation, each ship will compute and hash-map the cells it is currently occupying,
if the ship creation passes all validation, we update the `board.occupied_cells` with the new ship cells right when the ship spawns on the board.

By that, by the time we have instantiated all ships, our board will have all occupied cells mapped to their ships.  
<br>
## Storing The Board Object
I used flask variable `current_app` to store the board object globaly per flask-application instance and across requests.

The `session` flask variable can also be used instead instead or with `current_app` to preserve the board state per sessions and requests regardless current flask application instance, since it utilizes cookies as a mean for caching.

We will need to configure a secret key to the flask app: `app.config['SECRET_KEY'] = f'{my_strong_secret}'`  

serialize the board: `session['board'] = pickle.dumps(board)`, deserialize it: `board = pickle.loads(session['board'])` with each game changing event, and `del session['board']` if the delete-game-method was invoked. 

<hr>


## Important Note

- I was able to pass all the feature-tests but one: `features/play_battelship.feature:20  Can sink a ship`
- The scenario is trying to hit the same ship 3 times, while expecting a result/response of `'SINK'` which is not feasible, considering the rules of the game.
- ship_meta:
```python
{
    "x": 7,
    "y": 4,
    "size": 3,
    "direction": "V"
}
```
- steps:
```text
Scenario: Can sink a ship                              # features/play_battelship.feature:20
    Given a request url ${BASE_URL}/battleship           # dev/lib/site-packages/behave_restful/lang/_given_steps.py:7
    Given a shot at 7,4                                  # features/steps/battleship_steps.py:5
    And a shot at 7,5                                    # features/steps/battleship_steps.py:5
    And a shot at 7,6                                    # features/steps/battleship_steps.py:5
    Then the response status is OK                       # dev/lib/site-packages/behave_restful/lang/_then_steps.py:7
    And the response json at $.result is equal to "SINK" # dev/lib/site-packages/behave_restful/lang/_then_steps.py:23
      Assertion Failed: Expected <WATER> to be equal to <SINK>, but was not.
```
- I am getting the correct result after 3 different shots hit the ship, `'WATER'`, however the test seem to expect the result to be `'SINK'`. Please review this feature-test.  

<br>
<hr>

### Thank you
Mostafa Mohamed
