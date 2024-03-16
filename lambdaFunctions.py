# lamda functions are unnamed functions in python or anonymous fnctions
sum = lambda num : num * 2

print(sum(5))   # output: 10

def isPalindrome(string):
    if(string[::-1]  == string):
        return "This is a palindrome"
    else:
        return "Not a palindrome"

print(isPalindrome("radar"))

# lamdba forpalindrome function

isPalindromeFunction = lambda  string : "This is a palindrome" if(string[::-1]  == string) else "Not a palindrome"

print(isPalindromeFunction("mum"))