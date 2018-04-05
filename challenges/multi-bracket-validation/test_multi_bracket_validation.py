import pytest
from multi_bracket_validation import multi_bracket_validation


def test_raises_error():
    """Test function raises exception without string input."""
    with pytest.raises(ValueError):
        multi_bracket_validation(7)


def test_true_response():
    """Test True response."""
    assert multi_bracket_validation('{}[]([)]') == True


def test_false_response():
    """Test False response."""
    assert multi_bracket_validation('{}[]([)') == False
