import pytest

from disk import Disk

def test_creation() -> None:
    with pytest.raises(ValueError):
        Disk(1.2, 3.4, -1.0)
    with pytest.raises(ValueError):
        Disk(1.2, 3.4, 0.0)

def test_area() -> None:
    disk = Disk(1.0, 2.0, 3.0)
    assert disk.area() == pytest.approx(28.274333882308138)

def test_contains_point() -> None:
    disk = Disk(1.0, 2.0, 3.0)
    assert disk.contains_point(1.5, 3.2)
    assert disk.contains_point(0, 0)
    assert disk.contains_point(1, 4.9)
    assert not disk.contains_point(-1, -1)
    assert not disk.contains_point(1, 5.1)
