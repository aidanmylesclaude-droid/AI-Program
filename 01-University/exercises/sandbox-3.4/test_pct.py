# test_pct.py: automated checks for pct.py (Lesson 3.4).
# pytest finds every function whose name starts with "test_" and runs it.
# "assert X" means: this must be true, otherwise the test FAILS.
import pytest
from pct import pct_change

def test_rise():
    # 100 -> 110 is a 10% rise
    assert pct_change(100, 110) == 10

def test_capstone_eur():
    # The real EUR numbers from the capstone: 0.90284 -> 0.91045
    assert round(pct_change(0.90284, 0.91045), 2) == 0.84

def test_fall():
    # 200 -> 150 is a 25% fall (was deliberately wrong as -50 in Lesson 3.4; fixed after reading the failure)
    assert pct_change(200, 150) == -25

def test_zero_start_is_refused():
    # Dividing by zero must raise an error, not return nonsense
    with pytest.raises(ValueError):
        pct_change(0, 5)
