class Node:
    def __init__(self, data=None, link=None):
        self.data = data
        self.link = link

items = int(input("노드의 개수: "))
A = None  # 연결 리스트의 헤드 노드를 가리키는 변수

# 연결 리스트 구성
for i in range(items):
    data = input(f"노드 데이터 #{i+1}: ")
    # 새로운 노드 생성
    new_node = Node(data)
    # 생성된 노드를 연결 리스트에 추가
    if A is None:
        A = new_node
    else:
        current = A
        while current.link is not None:
            current = current.link
        current.link = new_node

# 연결 리스트의 내용 출력
print("리스트의 내용:", end=" ")
current = A
while current is not None:
    print(current.data, end=" ")
    current = current.link