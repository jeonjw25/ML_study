import random, timeit
def insertion_sort(A):
    for i in range(1, len(A)):
        j = i-1
        while j >= 0 and A[j] > A[i]:
            A[j], A[i] = A[i], A[j]
            j -= 1
def quick_sort(A, first, last):
    global Qc, Qs
    if last - first == 20: 
        Qc += 1
        insertion_sort(A[first:last+1])
        return 
    left, right = first+1, last
    pivot = A[first]
    while left <= right:
        Qc += 1
        while left <= last and A[left] < pivot:
            Qc += 2
            left += 1
        while right > first and A[right] > pivot:
            Qc += 2
            right -= 1
        if left <= right:
            Qc += 1
            A[left], A[right] = A[right], A[left]
            Qs += 1
            left += 1
            right -= 1
    A[first], A[right] = A[right], A[first]
    Qs += 1

    quick_sort(A, first, right - 1)
    quick_sort(A, right+1, last)

# def new_quick_sort(A, first, last):
#     if first >= last: return 
#     left, right = first+1, last
#     pivot = A[first]
#     while left <= right:
#         while left <= last and A[left] < pivot:
#             left += 1
#         while right > first and A[right] > pivot:
#             right -= 1
#         if left <= right:
#             A[left], A[right] = A[right], A[left]
#             left += 1
#             right -= 1
#     A[first], A[right] = A[right], A[first]

#     new_quick_sort(A, first, right - 1)
#     new_quick_sort(A, right+1, last)

def merge_sort(A, first, last):
    if first >= last: return
    merge_sort(A, first, (first+last)//2)
    merge_sort(A, (first+last)//2 + 1, last)
    merge_two_sorted_list(A, first, last)

def merge_two_sorted_list(A, first, last):
    global Mc, Ms
    m = (first + last) // 2
    i , j = first, m+1
    B = []
    while i <= m and j <= last:
        Mc += 3
        if A[i] <= A[j]:
            B.append(A[i])
            i += 1
        else:
            B.append(A[j])
            j += 1
    B += A[i:m+1]
    B += A[j:last+1]
    for i in range(first, last+1):
        Ms += 1
        A[i] = B[i-first]


def heap_sort(A):
    global Hs
    n = len(A)
    make_heap(A)
    for k in range(len(A) -1, -1, -1):
        A[0], A[k] = A[k], A[0]
        Hs += 1
        n = n - 1
        heapify_down(A, 0, n)
        
def make_heap(A):
    for k in range(len(A)-1, -1, -1):
        heapify_down(A, k, len(A))

def heapify_down(A, k, n):
    global Hs, Hc
    while 2*k + 1 < n:
        Hc += 6
        L, R = 2*k + 1, 2*k + 2
        if L < n and A[L] > A[k]:
            m = L
        else:
            m = k
        if R < n and A[R] > A[m]:
            m = R
        if m != k:
            Hs += 1
            A[k], A[m] = A[m], A[k]
            k = m
        else: break

def check_sorted(A):
    for i in range(n-1):
        if A[i] > A[i+1]: return False
    return True

Qc, Qs, Mc, Ms, Hc, Hs = 0, 0, 0, 0, 0, 0

n = int(input())
random.seed()
A = []
for i in range(n):
    A.append(random.randint(-1000, 1000))
B = A[:]
C = A[:]

print("")
print("Quick sort:")
print("time = ", timeit.timeit("quick_sort(A, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Qc, Qs))

print("Merge sort:")
print("time = ", timeit.timeit("merge_sort(B, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Mc, Ms))

print("Heap sort:")
print("time = ", timeit.timeit("heap_sort(C)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Hc, Hs))

assert(check_sorted(A))
assert(check_sorted(B))
assert(check_sorted(B))

# import matplotlib.pyplot as plt
# Q_t, M_t, H_t = [], [], []
# Q_c, M_c, H_c = [], [], []
# Q_s, M_s, H_s = [], [], []
# T = [100, 500, 5000, 10000, 50000, 100000, 500000]
# for i in T:
#     # random.seed()
#     A = []
#     for i in range(i):
#         A.append(random.randint(-1000, 1000))
#     B = A[:]
#     C = A[:]
#     # print("")
#     # print("Quick sort:")
#     # # print("time = ", timeit.timeit("quick_sort(A, 0, i-1)", globals=globals(), number=1))
#     t1 = timeit.timeit("quick_sort(A, 0, i-1)", globals=globals(), number=1)
#     # print("  comparisons = {:10d}, swaps = {:10d}\n".format(Qc, Qs))

#     # print("Merge sort:")
#     # # print("time = ", timeit.timeit("merge_sort(B, 0, i-1)", globals=globals(), number=1))
#     t2 = timeit.timeit("merge_sort(B, 0, i-1)", globals=globals(), number=1)
#     # print("  comparisons = {:10d}, swaps = {:10d}\n".format(Mc, Ms))

#     # print("Heap sort:")
#     # print("time = ", timeit.timeit("heap_sort(C)", globals=globals(), number=1))
#     t3 = timeit.timeit("heap_sort(C)", globals=globals(), number=1)
#     # print("  comparisons = {:10d}, swaps = {:10d}\n".format(Hc, Hs))
#     Q_t.append(t1)
#     Q_c.append(Qc)
#     Q_s.append(Qs)
#     M_t.append(t2)
#     M_c.append(Mc)
#     M_s.append(Ms)
#     H_t.append(t3)
#     H_c.append(Hc)
#     H_s.append(Hs)
# print(T)
# print(Q_s)
# print(M_s)
# print(H_s)
# # plt.plot(T, Q_s, 'r')
# # # plt.plot(T, M_c, 'g')
# # # plt.plot(T, H_c, 'b')
# # # ax1.bar(i, timeit.timeit("quick_sort(A, 0, n-1)", globals=globals(), number=1), label='quick')
# # # ax1.bar(i, timeit.timeit("merge_sort(A, 0, n-1)", globals=globals(), number=1), label='merge')
# # # ax1.bar(i, timeit.timeit("heap_sort(A)", globals=globals(), number=1), label='heap')
# # plt.show()