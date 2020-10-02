"""tests/test_functions.py

Tests for functions.py
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from io import StringIO
from unittest.mock import patch

import functions


# TODO: get_hometown() return string

# TODO: get_full_name(first, last) return full name

# TODO: output_greeting(first, last, hometown) print
# Hi Fido Bark, I'd like to visit Oakland!
# or
# Hi Mel M, we're from the same place!

# TODO: get_filled_list(n, fill=None) return filled list with length n

# TODO: word_tripler() return ("hi", "hihihi"), also check if it has
# inner function


if __name__ == "__main__":
    import pytest

    pytest.main(["-c", str(Path(__file__).parent / "conftest.py"), "--no-header"])