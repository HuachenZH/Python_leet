def is_palindrome(n:int) -> bool:
    return str(n) == str(n)[::-1]
print(is_palindrome(1441))
