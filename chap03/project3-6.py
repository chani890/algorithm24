def sequential_search(A,key):
    for i in range(len(A)):
        if A[i-1] == 1 and A[i] == 0 :    
            A[i-1], A[i] = 0, 1
            bChanged = True
            return i
    return -1