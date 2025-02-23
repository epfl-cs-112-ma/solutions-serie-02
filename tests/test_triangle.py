import pytest

from triangle import Point3D, Triangle

def test_distance() -> None:
    assert Point3D(1.2, 3.4, 5.6).distance(Point3D(6.5, 4.3, 2.1)) == pytest.approx(6.414826575987849)

def test_is_isosceles() -> None:
    a = Point3D(1.2, 3.4, 5.6)
    b = Point3D(6.5, 4.3, 2.1)
    c = Point3D(1, 2, 3)
    assert not Triangle(a, b, c).is_isosceles()

    a = Point3D(0, 0, 1)
    b = Point3D(-3, 4, 5)
    c = Point3D(3, 4, -3)
    assert Triangle(a, b, c).is_isosceles()

def test_permimeter() -> None:
    a = Point3D(1.2, 3.4, 5.6)
    b = Point3D(6.5, 4.3, 2.1)
    c = Point3D(1, 2, 3)
    assert Triangle(a, b, c).perimeter() == pytest.approx(15.403652411370743)
