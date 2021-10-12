def max_sum(A, left, right):
    	# A[left], ..., A[right] 중 최대 구간 합 리턴
	mid = (left + right) // 2
	if left == mid:
		return max(max(A), sum(A))
        
	max1, max2 = 0, 0
	sum1, sum2 = 0, 0
	for i in range(mid, left-1, -1):
		sum1 += A[i]
		if sum1 > max1:
			max1 = sum1
	for i in range(mid+1, right+1):
		sum2 += A[i]
		if sum2 > max2:
			max2 = sum2
	# print("mid:", mid)
	# print(max1, max2)
	return(max(max_sum(A, left, mid - 1), max_sum(A, mid+1, right), max1 + max2))

A = [int(x) for x in input().split()]

sol = max_sum(A, 0, len(A)-1)
print(sol)