# 배열에서 k번째로 작은 수 찾기

def quick_select(A, k):
	p = A[0]
	S, L, M = [], [], []
	for x in A:
		if x < p:
			S.append(x)
		elif x == p:
			M.append(x)
		else:
			L.append(x)
	if len(S) >= k:
		return quick_select(S, k)
	elif len(S) + len(M) < k:
		return quick_select(L, k - len(S) - len(M))
	else:
		return M[0]
	
n, k = map(int, input().split()) # n = 배열의 길이 k = k번째로 작은 원소
arr = list(map(int, input().split())) # 배열입력
print(quick_select(arr, k))