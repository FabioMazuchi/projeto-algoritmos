def is_palindrome_recursive(word, low_index, high_index):
    low = low_index
    high = high_index

    if len(word) == 0:
        return False

    if high == 0:
        return True
    else:
        if word[low].upper() != word[high].upper():
            return False
        return is_palindrome_recursive(word, low + 1, high - 1)
