# def check_palindrom(string):
#     return string == string[::-1]

def check_palindrom(string):
    left, right = 0, len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True 
print(check_palindrom("madam"))

