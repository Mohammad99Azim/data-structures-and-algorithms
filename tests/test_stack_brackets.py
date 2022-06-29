from stack_queue_brackets.stack_brackets import *
import pytest


def test_no_brackets_string():
    actual = validate_brackets("asdfasdfasdfasdf")
    expected = True
    assert actual == expected



def test_one_brackets_string_all_true():
    actual = validate_brackets("{}(){}")
    expected = True
    assert actual == expected

    actual = validate_brackets("()[[Extra Characters]]")
    expected = True
    assert actual == expected

    actual = validate_brackets("{}{Code}[Fellows](())")
    expected = True
    assert actual == expected

    actual = validate_brackets("{{{{asdfasdfasdfasdf}}}}")
    expected = True
    assert actual == expected


def test_one_brackets_string_all_false():
    actual = validate_brackets("{(){}")
    expected = False
    assert actual == expected

    actual = validate_brackets("()[[Extra Characters]")
    expected = False
    assert actual == expected

    actual = validate_brackets("{}{Code}[Fellows](()")
    expected = False
    assert actual == expected

    actual = validate_brackets("{{{sdfasdfasdfasdf}}}}")
    expected = False
    assert actual == expected



def test_empty_string_raises_exception():
    with pytest.raises(Exception) as e:
        validate_brackets("")
    assert repr(e) == "<ExceptionInfo Exception('The string is Empty !!!') tblen=2>"
