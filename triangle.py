from __future__ import annotations

from dataclasses import dataclass
import math

class Point3D:
    x: float
    y: float
    z: float

    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z

    def distance(self, other: Point3D) -> float:
        diff_x = other.x - self.x
        diff_y = other.y - self.y
        diff_z = other.z - self.z
        return math.sqrt(diff_x*diff_x + diff_y*diff_y + diff_z*diff_z)

class Triangle:
    a: Point3D
    b: Point3D
    c: Point3D

    def __init__(self, a: Point3D, b: Point3D, c: Point3D) -> None:
        self.a = a
        self.b = b
        self.c = c

    def __ab(self) -> float:
        return self.a.distance(self.b)

    def __bc(self) -> float:
        return self.b.distance(self.c)

    def __ca(self) -> float:
        return self.c.distance(self.a)

    def __approx_same(self, x: float, y: float) -> bool:
        return abs(x - y) < 1e-10

    def is_isosceles(self) -> bool:
        ab = self.__ab()
        bc = self.__bc()
        ca = self.__ca()
        return self.__approx_same(ab, bc) or self.__approx_same(bc, ca) or self.__approx_same(ca, ab)

    def perimeter(self) -> float:
        return self.__ab() + self.__bc() + self.__ca()
