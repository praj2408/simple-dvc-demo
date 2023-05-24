def square(n: float) -> float:
    """Square a number."""
    return n**2

def test_square():
    # When
    subject = square(4)

    # Then
    assert subject == 16