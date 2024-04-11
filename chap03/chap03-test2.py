def sequential_search(A, key):
    for i in range(len(A)):
        if A[i] == key:
            return i
    return -1

data = [5, 3, 8, 4, 9, 1, 6, 2, 7]
key = int(input("key 입력: "))
result = sequential_search(data, key)

if result != -1:
    print(f"{key} 값은 리스트의 인덱스 {result} 에 위치함")
else:
    print(f"{key} 는 리스트에 없음")
