str1=input('Enter a string:')
rev=str1[::-1]
def is_palindrome(x):
    if rev == x:
        return True
    return False    
print(is_palindrome(str1))    