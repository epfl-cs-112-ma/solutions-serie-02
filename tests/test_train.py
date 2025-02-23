import pytest

from train import *

def test_scenario() -> None:
    light_terminus = Light(is_green=True)
    light_1 = Light(is_green=True)
    light_2 = Light()

    terminus = Segment(light=light_terminus)
    segment4 = Segment(terminus)
    segment3 = Segment(segment4, light=light_2)
    segment2 = Segment(segment3, light=light_1)
    segment1 = Segment(segment2)

    train = Train(initial_segment=segment1)

    assert train.can_advance()
    train.advance()
    assert train.current_segment() is segment2

    assert train.can_advance() # the light is green
    train.advance()
    assert train.current_segment() is segment3

    assert not train.can_advance() # the light is red!
    with pytest.raises(Exception):
        train.advance() # we must not be allowed to advance
    assert train.current_segment() is segment3 # still on segment3

    light_2.is_green = True

    assert train.can_advance()
    train.advance()
    assert train.current_segment() is segment4

    assert train.can_advance()
    train.advance()
    assert train.current_segment() is terminus

    assert not train.can_advance() # the light is green but it is the terminus
    with pytest.raises(Exception):
        train.advance() # we must not be allowed to advance
    assert train.current_segment() is terminus # still at the terminus
