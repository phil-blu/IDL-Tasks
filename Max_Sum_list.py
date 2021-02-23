# Write a function that takes in a non-empty array of integers and return the maximum 
# sum that can be obtained by summing up all of the integers in a non-empty subarray 
# of the input array. A subarray must only contain adjacent numbers (numbers next to each other in the input array).
# array = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
	

	

def maximum_sum(a_list):
	    
	    
	 lenth = len(a_list)
	    
	 # A case for when the input list is empty
	 if lenth == 0:
	     return 0
	

	 # initializing the maximum sum to be zero
	 max_sum = 0
	

	 # looping through the range of the the list indices
	 for one in range(lenth):
	

	     ### obtaining the sublist
	        
	     if one == 0:   # for the first item in the list which should have one adjacent number
	         sub_list = a_list[one:one+2]
	        
	     elif one == lenth - 1:  # for the last item in the list which should have one adjacent number
	         sub_list = a_list[one -1:one + 1]
	

	     else: # for the general case where every other item in between has an adjacent number to the left and right.
	         sub_list = a_list[one - 1: one + 2]
	

	     ### getting sum of sub_list
	        
	     the_sum = 0  # initializing the sum as zero, then we tranverse through
	     for item in sub_list:
	         the_sum = the_sum + item   # summing up elements of the list
	     print(one, sub_list, the_sum)
	        
	     if max_sum < the_sum:
	         max_sum = the_sum
	

	 return max_sum
	

	

	






	a_list = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
	fn = maximum_sum(a_list)
