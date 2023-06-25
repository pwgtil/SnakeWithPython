from position import Position
from direction import Direction


class GameState:
    def __init__(self,
                 snake,
                 direction,
                 food,
                 field_size):
        self.snake = snake
        self.direction = direction
        self.food = food
        self.field_size = field_size

    def step(self):
        new_head = self.next_head(self.direction)
        self.snake.append(new_head)
        self.snake = self.snake[1:]

    def next_head(self, direction):
        pos = self.snake[-1]
        if direction == Direction.UP:
            return Position(pos.x, pos.y - 1)
        elif direction == Direction.DOWN:
            return Position(pos.x, pos.y + 1)
        elif direction == Direction.RIGHT:
            return Position(pos.x + 1, pos.y)
        elif direction == Direction.LEFT:
            return Position(pos.x - 1, pos.y)
