try:
    a = int(input())
except ValueError:
    print("That's not an int!")


def get_numbers(a):
    s = []
    while a > 0:
        s.append(a % 10)
        a //= 10
    return s


def is_palindrome(s):
    flag_palindrome = True
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            flag_palindrome = False
    return flag_palindrome


if is_palindrome(get_numbers(a)):
    print('this is a palindrome')
else:
    print('this is not a palindrome')
    
