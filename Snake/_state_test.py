import unittest
from game_state import GameState
from position import Position
from direction import Direction


class GameStateTest(unittest.TestCase):

    # =======================================
    # Simple moves
    # =======================================
    def test_snake_should_move_right(self):
        state = GameState(
            snake=[
                Position(1, 2),
                Position(1, 3),
                Position(1, 4)
            ],
            direction=Direction.RIGHT,
            food=Position(10, 10),
            field_size=20
        )

        state.step()

        expected_state = [
            Position(1, 3),
            Position(1, 4),
            Position(2, 4),
        ]

        self.assertEquals(expected_state, state.snake)

    def test_snake_should_move_left(self):
        state = GameState(
            snake=[
                Position(1, 2),
                Position(1, 3),
                Position(1, 4)
            ],
            direction=Direction.LEFT,
            food=Position(10, 10),
            field_size=20
        )

        state.step()

        expected_state = [
            Position(1, 3),
            Position(1, 4),
            Position(0, 4),
        ]

        self.assertEquals(expected_state, state.snake)

    def test_snake_should_move_up(self):
        state = GameState(
            snake=[
                Position(1, 2),
                Position(1, 3),
                Position(2, 3)
            ],
            direction=Direction.UP,
            food=Position(10, 10),
            field_size=20
        )

        state.step()

        expected_state = [
            Position(1, 3),
            Position(2, 3),
            Position(2, 2),
        ]

        self.assertEquals(expected_state, state.snake)

    def test_snake_should_move_down(self):
        state = GameState(
            snake=[
                Position(1, 2),
                Position(1, 3),
                Position(1, 4)
            ],
            direction=Direction.DOWN,
            food=Position(10, 10),
            field_size=20
        )

        state.step()

        expected_state = [
            Position(1, 3),
            Position(1, 4),
            Position(1, 5),
        ]

        self.assertEquals(expected_state, state.snake)

    # =======================================
    # Moves over the edge of the map
    # =======================================
    def test_snake_should_move_up_on_top(self):
        state = GameState(
            snake=[
                Position(2, 2),
                Position(2, 1),
                Position(2, 0)
            ],
            direction=Direction.UP,
            food=Position(10, 10),
            field_size=20
        )

        state.step()

        expected_state = [
            Position(2, 1),
            Position(2, 0),
            Position(2, 19),
        ]

        self.assertEquals(expected_state, state.snake)

    def test_snake_should_move_down_on_bottom(self):
        state = GameState(
            snake=[
                Position(2, 17),
                Position(2, 18),
                Position(2, 19)
            ],
            direction=Direction.DOWN,
            food=Position(10, 10),
            field_size=20
        )

        state.step()

        expected_state = [
            Position(2, 18),
            Position(2, 19),
            Position(2, 0),
        ]

        self.assertEquals(expected_state, state.snake)

    def test_snake_should_move_right_on_edge(self):
        state = GameState(
            snake=[
                Position(17, 1),
                Position(18, 1),
                Position(19, 1)
            ],
            direction=Direction.RIGHT,
            food=Position(10, 10),
            field_size=20
        )

        state.step()

        expected_state = [
            Position(18, 1),
            Position(19, 1),
            Position(0, 1)
        ]

        self.assertEquals(expected_state, state.snake)

    def test_snake_should_move_left_on_edge(self):
        state = GameState(
            snake=[
                Position(2, 1),
                Position(1, 1),
                Position(0, 1)
            ],
            direction=Direction.LEFT,
            food=Position(10, 10),
            field_size=20
        )

        state.step()

        expected_state = [
            Position(1, 1),
            Position(0, 1),
            Position(19, 1)
        ]

        self.assertEquals(expected_state, state.snake)

    # =======================================
    # Eating food
    # =======================================
    def test_snake_eats_food(self):
        state = GameState(
            snake=[
                Position(1, 2),
                Position(2, 2),
                Position(3, 2)
            ],
            direction=Direction.UP,
            food=Position(3, 1),
            field_size=20
        )

        state.step()

        expected_state = [
            Position(1, 2),
            Position(2, 2),
            Position(3, 2),
            Position(3, 1)
        ]

        self.assertEquals(expected_state, state.snake)
        self.assertEquals(False, state.food in state.snake)