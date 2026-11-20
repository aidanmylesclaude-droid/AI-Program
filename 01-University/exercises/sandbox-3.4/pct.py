# pct.py: the "percent change" maths from the Stage 1 capstone, pulled out
# into a function so it can be tested on its own (Lesson 3.4).
def pct_change(first, last):
    """How much `last` changed compared with `first`, in percent."""
    if first == 0:
        raise ValueError("first must not be zero (can't divide by zero)")
    return (last - first) / first * 100
