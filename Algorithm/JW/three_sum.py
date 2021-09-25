# def two_sum(X, Y, t):
#     p1, p2 = 0, 0
#     while p1 < len(X) and p2 < len(Y): # 한번순회
#         if X[p1] + Y[p2] == t: # if문에서 기본연산 2회
#             return True 
#         elif X[p1] + Y[p2] < t: # elif문에서 기본연산 4회
#             p1 += 1
#         else: # else문에서 기본연산 2회
#             p2 += 1
#     return False
# # elif문과 else문은 선택적이므로 T(4n+c) 혹은 T(2n+c), 따라서 Big-O로 표기하면 O(n)이다.

# def three_sum(X, Y, Z):
#     X, Y = sorted(X), sorted(Y, reverse=True)
#     for i in Z:
#         if two_sum(X, Y, -i):
#             return True
#     return False
# # 리스트 Z를 순회하는 for문 안에 two_sum이 있으므로 T(4n^2 + cn) 혹은 T(2n^2 + cn)이 된다. 
# # 따라서 Big-O로 표기하면 O(n^2)이다.

def binary_search(X, n):
    low, high = 0, len(X)-1
    while low <= high:
        mid = low + high // 2
        if n < X[mid]:
            high = mid - 1
        elif n == X[mid]:
            return True
        else:
            low = mid + 1
    return False

def two_sum(X, Y, t):
    for i in X:
        if binary_search(Y, t-i):
            return True
    return False

def three_sum(X, Y, Z):
    Y = sorted(Y)
    for i in Z:
        if two_sum(X, Y, -i):
            return True
    return False

X = input()
Y = input()
Z = input()
X = [int(i) for i in X.split(' ')]
Y = [int(i) for i in Y.split(' ')]
Z = [int(i) for i in Z.split(' ')]
print(three_sum(X, Y, Z))
