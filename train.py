from __future__ import annotations

class Light:
    """Un feu de signalisation qui est vert ou rouge."""

    is_green: bool
    """Indique si le feu est vert.

    Cet attribut peut être directement modifié.
    """

    def __init__(self, is_green: bool = False) -> None:
        self.is_green = is_green

class Segment:
    __next_segment: Segment | None
    __light: Light | None

    def __init__(self, next_segment: Segment | None = None, light: Light | None = None):
        self.__next_segment = next_segment
        self.__light = light

    def can_train_advance(self) -> bool:
        if self.__next_segment is None:
            return False
        elif self.__light is None:
            return True
        else:
            return self.__light.is_green

    def next_segment(self) -> Segment:
        assert self.__next_segment is not None, "There is no next_segment"
        return self.__next_segment

class Train:
    __current_segment: Segment

    def __init__(self, initial_segment: Segment) -> None:
        self.__current_segment = initial_segment

    def current_segment(self) -> Segment:
        return self.__current_segment

    def can_advance(self) -> bool:
        return self.__current_segment.can_train_advance()

    def advance(self) -> None:
        if not self.can_advance():
            raise Exception("The train cannot advance right now.")
        self.__current_segment = self.__current_segment.next_segment()
