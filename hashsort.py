# dimension values variable, i.e. 3x3 matrix 
Dim = 3

# function implementing Hash Sort 


def HashSort(data, N, low): 
	swapCount = 0
	hysteresisCount = 0
	position = 0
	value = 0

	# condition to check if the end of data list is 
	# reached 
	while ((swapCount < N) and (hysteresisCount < N)): 
		value = data[(position) // Dim][(position) % Dim] 
		d = (value - low) // Dim 
		m = (value - low) % Dim 

		# if hysteresis occurs 
		if (data[d][m] == value): 

			# force push the position by 1 to avoid 
			# hysteresis 
			position += 1
			hysteresisCount += 1
		# if no hysteresis, then swap the positions 
		else: 
			temp = data[(position) // Dim][(position) % Dim] 
			data[(position) // Dim][(position) % Dim] = data[d][m] 
			data[d][m] = temp 
			swapCount += 1


# Driver Code 
if __name__ == '__main__': 
	N = 1
	arr = [[5, 8, 1], [9, 7, 2], [4, 6, 3]] 
	HashSort(arr, 9, N) 
	print("The resultant sorted array is: ") 
	# printing the resultant sorted array 
	for i in range(3): 
		for j in range(3): 
			print(arr[i][j], end =' ') 
		print() 
