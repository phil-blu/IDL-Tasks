'''
Write a function that takes in an array of positive integers and returns the maximum sum of
non-adjacent elements in the array.
If the input array is empty, the function should return 0.
array = [75, 105, 120, 75, 90, 135]
'''

Array = [75, 105, 120, 75, 90, 135]
A = []
def maximum_sum(array):
    #handling exception of an empty array
    if array == []:
        return 0

    #Gets the sum of none adjacent elements
    else:
        even_sum, odd_sum = 0, 0
        for i in array[::2]:
            even_sum += i
        for i in array[1::2]:
            odd_sum += i


        #Checks for maximum value
        if even_sum > odd_sum:
            return even_sum
        elif even_sum < odd_sum:
            return odd_sum
        elif even_sum == odd_sum:
            return None

print(maximum_sum(Array))

'''
COMPLEXITY ANALYSIS
O(2n) for time which is O(n) for time
O(1) for space
'''
