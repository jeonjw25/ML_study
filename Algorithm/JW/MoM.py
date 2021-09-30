import copy

def find_median_five(A):
	cnt = 0
	tmp = copy.deepcopy(A)
	while cnt < len(A) // 2:
		tmp.remove(max(tmp))
		cnt += 1
	return max(tmp)

# A = [2, 5, 4, 3]
# print(find_median_five(A))

def MoM(A, k): # L의 값 중에서 k번째로 작은 수 리턴
	if len(A) == 1: # no more recursion
		return A[0]
	i = 0
	S, M, L, medians = [], [], [], []
	while i+4 < len(A):
		medians.append(find_median_five(A[i: i+5]))
		# i += 5
	if i < len(A) and i+4 >= len(A): # 마지막 그룹으로 5개 미만의 값으로 구성
		medians.append(find_median_five(A[i:]))

	mom = MoM(medians, len(medians) // 2)
	for v in A:
		if v < mom:
			S.append(v)
		elif v > mom:
			L.append(v)
		else:
			M.append(v)

	if len(S) >= k : return MoM(S, k)
	elif len(S) + len(M) < k: return MoM(L, k - len(S) - len(M))
	else: return mom

# n과 k를 입력의 첫 줄에서 읽어들인다
# n개의 정수를 읽어들인다. (split 이용 + int로 변환)
n, k = map(int, input().split())
A = list(map(int, input().split()))
print(MoM(A, k))