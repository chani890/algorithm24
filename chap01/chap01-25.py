#연습문제 25번
#리스트 A와 B의 합집합,교집합 및 차집합을 각각 구하는 프로그램
#202110028강찬희
def union(A, B):
    return list(set(A + B))

def intersection(A, B):
    return list(set(A) & set(B))

def difference(A, B):
    return list(set(A) - set(B))

A = [1, 2, 3, 4, 5]
B = [4, 5, 6, 7, 8]

print("A와 B의 합집합:", union(A, B))
print("A와 B의 교집합:", intersection(A, B))
print("A와 B의 차집합:", difference(A, B))