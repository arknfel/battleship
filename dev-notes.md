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
An instance of class board represents a game instance, keeping track of the game state, modifying the board istance per action/event/iteration, will represent the game state as it will be changing.

Instead of having to worry about the MxN cells, untill the game gets more complex we only need to worry about occupied cells and leave it to validators to make sure that shots are within the grid. We can safly assume that if a shot's coordinates does not match any of the occupied cells, it is surely a `'WATER'` shot.

The idea here is to map each group of cells to the corresponding occupying ship:
```python
board.occupied_cells = {
    '[1, 2]': ship_instance1,
    '[4, 2]': ship_instance2
}
```
This will enable us to easily map the shots coordinates to the ships ( `O(1)` time complixity ), then simply change the ship's condition accordingly, now let us take a look at the Ship model:
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
if the ship creation passes all validation, we update the board.occupied cells with the new ship cells.

By that, by the time we have instantiated all ships, our board will have all occupied cells mapped to their ships.  
<br>
<hr>


## Important Note

- I was able to pass all the featur-tests but one: `features/play_battelship.feature:20  Can sink a ship`
- The scenario is trying to hit the same ship 3 times, while expecting a result/response of `'SINK'` which is not feasible, considering the rules of the game.
- ship:
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
