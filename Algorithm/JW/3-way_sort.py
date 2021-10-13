def merge(A, i, j, k, l):
    # i <= j and j < k <= l
    # 정렬된 두 부분 A[i..j]와 A[k..l]을 merge하는 함수
		tmp = []
		while i <= j and k <= l:
			if A[i] > A[k]:
				tmp.append(A[k])
				k += 1
			elif A[i] < A[k]:
				tmp.append(A[i])
				i += 1
			else:
				tmp.append(A[i])
				tmp.append(A[k])
				i += 1
				k += 1
		if i == j:
			A = tmp + A[k:l+1]
		else:
			A = tmp + A[i:j+1]
		return A


A = [1, 3, 5, 7, 8, -1, 0, 4]

print(merge(A, 0, 3, 5, 7))