def merge(A, i, j, k, l):
    # i <= j and j < k <= l
    # 정렬된 두 부분 A[i..j]와 A[k..l]을 merge하는 함수
	tmp = []
	while i <= j and k <= l:
		if A[i] >= A[k]:
			tmp.append(A[k])
			k += 1
		else:
			tmp.append(A[i])
			i += 1
	for idx in range(k, l+1):
		tmp.append(A[idx])
	for idx in range(i, j+1):
		tmp.append(A[idx])	
	return tmp

A = [61, 86, 17, 31, 2, 81, 19, 0, 62, 49, 91, 35, 28, 68, 36, 69, 36, 32, 77, 33]
# A = [10, 9, 8, 7, 6, 5, 4, 3, 2 ,1]
def m_sort(A, first, last): 
	mid1 = first + (last - first) // 3
	mid2 = first + 2*((last - first) // 3) + 1
	if last - first < 1:
		return A
	else:
		m_sort(A, first, mid1)
		m_sort(A, mid1+1, mid2)
		m_sort(A, mid2+1, last)
		A[first:mid2+1] = merge(A, first, mid1,	mid1+1, mid2)
		A[first:last+1] = merge(A, first, mid2, mid2+1, last)
		return A
    # 3-way merge sort - merge 함수를 이용해 적절히 합병한다

def check(A):
	for i in range(1, len(A)):
		if A[i-1] > A[i]:
			return False
	return A[0]+A[(len(A)//2)]+A[-1]

m_sort(A, 0, len(A)-1)

# print(m_sort(A, 0, len(A)-1))
print(check(A))