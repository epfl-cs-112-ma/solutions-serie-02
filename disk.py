import math

class Disk:
    __center_x: float
    __center_y: float
    __radius: float

    def __init__(self, center_x: float, center_y: float, radius: float) -> None:
        if radius <= 0:
            raise ValueError(f"Radius must be positive but was {radius}")
        self.__center_x = center_x
        self.__center_y = center_y
        self.__radius = radius

    def area(self) -> float:
        return math.pi * self.__radius * self.__radius

    def contains_point(self, x: float, y: float) -> bool:
        diff_x = x - self.__center_x
        diff_y = y - self.__center_y
        dist = math.sqrt(diff_x*diff_x + diff_y*diff_y)
        return dist <= self.__radius
