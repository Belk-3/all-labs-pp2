# 11. Check if a word is a palindrome
def is_palindrome(word):
    result = word == word[::-1]
    print(f"Is '{word}' a palindrome? {result}")
    return result