# Python3 implementation to find the
# maximum LCM of pairs in an array
from math import gcd

# Function comparing all LCM pairs


def maxLcmOfPairs(arr, n):

	# To store the highest LCM
	maxLCM = -1

	# To generate all pairs from array
	for i in range(n):
		for j in range(i + 1, n, 1):

			# Find LCM of the pair
			# Update the maxLCM if this is
			# greater than its existing value
			maxLCM = max(maxLCM, (arr[i] * arr[j]) //
						gcd(arr[i], arr[j]))

	# Return the highest value of LCM
	return maxLCM


# Driver code
if __name__ == '__main__':

	arr = [17, 3, 8, 6]
	n = len(arr)

	print(maxLcmOfPairs(arr, n))

# This code is contributed by hupendraSingh
