"""
https://www.geeksforgeeks.org/count-trailing-zeroes-factorial-number/

We can easily observe that the number of 2s in prime factors is always more than or equal to the number of 5s. 
So if we count 5s in prime factors, we are done. How to count total number of 5s in prime factors of n!? 
A simple way is to calculate floor(n/5). For example, 7! has one 5, 10! has two 5s. It is not done yet, 
there is one more thing to consider. Numbers like 25, 125, etc have more than one 5. 
For example if we consider 28!, we get one extra 5 and number of 0s become 6. Handling this is simple, 
first divide n by 5 and remove all single 5s, then divide by 25 to remove extra 5s and so on. Following is the summarized formula for counting trailing 0s.

Trailing 0s in n! = Count of 5s in prime factors of n!
                  = floor(n/5) + floor(n/25) + floor(n/125) + ....
                  
                  
"""

# Python3 program to 
# count trailing 0s 
# in n! 

# Function to return 
# trailing 0s in 
# factorial of n 
def findTrailingZeros(n): 
	
	# Initialize result 
	count = 0

	# Keep dividing n by 
	# powers of 5 and 
	# update Count 
	i=5
	while (n/i>=1): 
		count += int(n/i) 
		i *= 5

	return int(count) 

# Driver program 
n = 100
print("Count of trailing 0s "+
	"in 100! is",findTrailingZeros(n)) 

# This code is contributed by Smitha Dinesh Semwal 
