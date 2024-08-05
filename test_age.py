from age import get_collective_mins
from datetime import date

def test_get_mins():
     # Test cases with expected results
    assert get_collective_mins(date(1999, 1, 1), date(2000, 1, 1)) == 525600
    assert get_collective_mins(date(2001, 1, 1), date(2003, 1, 1)) == 1051200
    assert get_collective_mins(date(1995, 1, 1), date(2000, 1, 1)) == 2629440
    assert get_collective_mins(date(2020, 6, 1), date(2032, 1, 1)) == 6092640

    # Edge case: Same date
    assert get_collective_mins(date(2000, 1, 1), date(2000, 1, 1)) == 0