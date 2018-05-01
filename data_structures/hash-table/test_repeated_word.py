from repeated_word import repeated_word
import pytest


def test_repeated_word_type_error():
    with pytest.raises(TypeError):
        repeated_word(42)


def test_repeated_word_long():
    dupe = repeated_word('In the week before their departure \
                   to Arrakis, when all the final scurrying about had reached \
                   a nearly unbearable frenzy, an old crone came to visit the \
                   mother of the boy, Paul.')
    assert dupe == 'the'


def test_repeated_word_no_dupes():
    with pytest.raises(KeyError):
        repeated_word('It was a bright cold day in April, and the clocks were \
                       striking thirteen.')
