'''
Write a function that takes in a non-empty string and that returns a boolean representing whether the string is a palindrome. 
A palindrome is defined as a string that's written the same way forward and backward. Note that single-character strings are palindromes.
string = "abcdcba"
'''

string = "abcdcba"
def palindrome(string):
    #checks for empty string
    if string == "":
        return (None)

    #reverses string
    reversed_string = ""
    for i in string:
        reversed_string = i+reversed_string


    #Compares both lists
    if string == reversed_string:
        return (True)
    else:
        return (False)

print(palindrome(string))

'''
Cost Implication:
O(n) for time
O(n) for space
'''
