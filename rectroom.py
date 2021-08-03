from typing import Tuple

class RectRoom:
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x1 = x
        self.y1 = y
        self.x2= x + width
        self.y2 = y + height

    @property
    def center(self) -> Tuple[int,int]
        center_x = int((self.x1 + self.x2) / 2)
        center_y = int((self.y1 + self.y2) / 2)

        return self.center_x, self.center_y

    @property
    def inner(self) -> Tuple[slice, slice]

    # Return inner area of room as 2D array index
    return slice(self.x1 + 1, self.x2) , slice(self.y1+1, self.y2)
