'''
Write a function that takes in a non-empty string and that returns a boolean representing whether the string
is a palindrome. A palindrome is defined as a string that's written the same way forward and backward.
Note that single-character strings are palindromes.
string = "abcdcba"
'''

string = "abcdcba"
def improved_palindrome(string):
    if string == "":
        return None

    #Initialising the left and right pointers
    else:
        left = 0
        right = len(string)
        count = 0

        #Comparing the sting simultaneously from both ends
        while left < len(string):
            while right > 0:
                if string[left] == string[right-1]:
                    count +=1
                    left += 1
                    right -= 1

                else:
                    return False

        if count == len(string):
            return True
        else: return False

print(improved_palindrome(string))

#Complexity Analysis
#O(n^2) for time
#O(1) for space
