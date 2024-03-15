
def selection_sort(A, n):
    for i in range(n):
        least = i
        for j in range(i+1, n):
            if A[j] < A[least]:
                least = j
        A[i], A[least] = A[least], A[i]

A = [3, 7, 9, 4, 2, 8, 1, 5]
n = len(A)
selection_sort(A, n)
print('정렬된 배열:', A)