from functools import lru_cache

@lru_cache()
def is_palindrome(word: str) -> bool:
    if len(word) == 0 or len(word) == 1:
        return True

    if word[0] != word[len(word) - 1]:
        return False

    return is_palindrome(word[1:-1])
