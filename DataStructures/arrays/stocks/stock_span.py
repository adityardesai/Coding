# https://www.geeksforgeeks.org/the-stock-span-problem/
# TC: O(N)
# SC: O(N)

# Python linear time solution for stock span problem 

# A stack based efficient method to calculate s 
def calculateSpan(price, S): 
	
	n = len(price) 
	# Create a stack and push index of fist element to it 
	st = [] 
	st.append(0) 

	# Span value of first element is always 1 
	S[0] = 1

	# Calculate span values for rest of the elements 
	for i in range(1, n): 
		
		# Pop elements from stack while stack is not 
		# empty and top of stack is smaller than price[i] 
		while( len(st) > 0 and price[st[-1]] <= price[i]): 
			st.pop() 

		# If stack becomes empty, then price[i] is greater 
		# than all elements on left of it, i.e. price[0], 
		# price[1], ..price[i-1]. Else the price[i] is 
		# greater than elements after top of stack 
        if len(st) <= 0:
          S[i] = i + 1  
        else:
          S[i] = (i - st[-1]) 

		# Push this element to stack 
		st.append(i) 
