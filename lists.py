"""Skills 1: lists.py

Complete the following functions. To get a better idea of how each function
should behave, see the examples in test_lists.py.
"""


def get_words_by_first_letter(words, letter):
    """Return a list of all words that start with the given letter."""

    matching_words =[]
    for word in words:
        if word.startswith(letter):
            matching_words.append(word)
    return matching_words
    

def filter_by_length(items, length):
    """Return a list of all items with the given length."""
    matching_length = []
    for item in items:
        if len(item) == length:
            matching_length.append(item)
    return matching_length


def words_in_common(words1, words2):
    """Return strings that words1 and words2 have in common."""
    common_words= []
    for word in words1:
        if word in words2:
            if word not in common_words:
                common_words.append(word)
    return common_words



def every_other_item(items):
    """Return a list with every other element items (start with index 0)."""
    return items[::2]
    


def smallest_n_items(items, n):
    """Return the n smallest values in the given list, in descending order.

    You can assume that `n` will be less than the length of the list.
    """
    
    #sorted_items = sorted(items)[:n]
    #return sorted_items[::-1]
    
    items_list = []
    for item in items:
        if item <= n:
            items_list.append(item)
    items_list = sorted(items_list)
    return items_list[::-1]

def get_index(items, value):
    """Search for a value in items and return its index.

    If the value doesn't exist in items, return None. If the value appears more
    than once, return the index of the first occurrence of the value.
    """

    for item in range(len(items)):
        if items[item] == value:
            return item
        
if __name__ == "__main__":
    import sys
    from pathlib import Path

    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        try:
            import pytest
            pytest.main([f"test_{Path(__file__).name}"])
        except ModuleNotFoundError:
            print("Unable to run tests because 'pytest' wasn't found :(")
            print("Run the command below to install pytest:")
            print()
            print("    pip3 install pytest")
