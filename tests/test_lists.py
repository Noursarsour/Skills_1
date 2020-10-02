"""tests/test_lists.py

Tests for lists.py
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from io import StringIO
from unittest.mock import patch

import pytest

from lists import (
    print_indices,
    words_in_common,
    every_other_item,
    every_last_char,
    get_highest_score,
    smallest_n_nums,
)


def test_print_indices_return():
    """print_indices should return None"""

    assert print_indices([]) is None


def test_print_indices_output():
    """print_indices should output each item in list followed by its index."""

    # This will let check what was printed to standard output
    with patch("sys.stdout", new_callable=StringIO) as output:
        print_indices(["apple", "berry", "cherry"])

        assert output.getvalue() == "apple 0\nberry 1\ncherry 2\n"


def test_words_in_common_return():
    """words_in_common should return a list."""

    assert type(words_in_common([], [])) is list


def test_words_in_common_gets_common_items():
    """words_in_common should return words shared between given lists."""

    assert words_in_common(["python"], ["turtle", "lizard", "python"]) == ["python"]


def test_no_repeats():
    """The result of words_in_common should not contain duplicates."""

    assert words_in_common(["cheese", "cheese"], ["cheese", "cheese"]) == ["cheese"]


def test_every_other_item_return():
    """every_other_item should return a list."""

    assert type(every_other_item([])) is list


def test_every_other_item():
    """every_other_item should return a new list with every 2 items of given
    list."""

    assert every_other_item(["a", "b", "c", "d"]) == ["b", "d"]


def test_every_last_char_return():
    """every_last_char should return a list."""

    assert type(every_last_char([])) is list


def test_every_last_char():
    """every_last_char should return the last character of each string."""

    assert every_last_char(["hello!"]) == ["!"]
    assert every_last_char(["multiple", "items", "?"]) == ["e", "s", "?"]


def test_smallest_n_nums_return():
    """smallest_n_items should return a set."""

    assert type(smallest_n_nums([], 0)) is set


def test_smallest_n_nums():
    """smallest_n_items should return a set of length `n` if all numbers are unique."""

    nums = [1, 2, 3, 4, 5]

    assert len(smallest_n_nums(nums, 0)) == 0
    assert len(smallest_n_nums(nums, 1)) == 1
    assert len(smallest_n_nums(nums, 5)) == 5


def test_smallest_n_nums_not_enough():
    """smallest_n_items should handle lists shorter than `n`."""

    assert smallest_n_nums([1, 5, 2], 5) == {1, 2, 5}


if __name__ == "__main__":
    pytest.main(["-c", str(Path(__file__).parent / "conftest.py"), "--no-header"])
