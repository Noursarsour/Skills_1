import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import pytest
from lists import print_indices, words_in_common, every_other_item, smallest_n_items


def test_return_none():
    """print_indices should return None.

    :points: 1
    """

    assert print_indices([]) is None


def test_print_each_item(capsys):
    """print_indices should output each item of the given list.

    :points: 2
    """

    print_indices(["apple", "berry", "cherry"])
    output = capsys.readouterr().out
    assert "apple" in output
    assert "berry" in output
    assert "cherry" in output


def test_print_each_index(capsys):
    """print_indices should output the index number of each item.

    :points: 2
    """

    print_indices(["apple", "berry", "cherry"])
    output = capsys.readouterr().out
    assert "0" in output
    assert "1" in output
    assert "2" in output


def test_no_counter_var():
    """The code for print_indices doesn't have a counting variable.

    :points: 3
    """

    pass


def test_words_in_common_return_list():
    """words_in_common should return a list.

    :points: 1
    """

    assert type(words_in_common(["test"], ["test"])) is list


def test_return_common_words():
    """words_in_common should return words shared between given lists.

    :points: 2
    """

    assert words_in_common(["python"], ["turtle", "lizard", "python"]) == ["python"]


def test_case_sensitive():
    """Words with different capitalization should be treated as different words.

    :points: 1
    """

    assert words_in_common(["CAKE"], ["cake"]) == []


def test_no_repeats():
    """The result of words_in_common should not contain duplicates.

    :points: 2
    """

    assert words_in_common(["cheese", "cheese"], ["cheese"]) == ["cheese"]


def test_smallest_n_items():
    """smallest_n_items should return a list of length `n`.

    :points: 1
    """

    nums = [1, 1, 1, 1, 1]

    assert len(smallest_n_items(nums, 0)) == 0
    assert len(smallest_n_items(nums, 1)) == 1
    assert len(smallest_n_items(nums, 3)) == 3


def test_descending_order():
    """smallest_n_items should return a list of numbers in descending order.

    :points: 3
    """

    assert smallest_n_items([0, 1, 2, 3, 4], 3) == [2, 1, 0]
    assert smallest_n_items([4, 3, 1, 0, 2], 3) == [2, 1, 0]
