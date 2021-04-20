def is_palindrome(a):
    if len(a) < 2:
        raise Exception("String length should greater than 1.")
    return a ==a[::-1]

answer = is_palindrome("ab5b a")
print(answer)