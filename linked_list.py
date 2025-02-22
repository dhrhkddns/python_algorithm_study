class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
    
    def __len__(self):
        return self.length
    
    def appendleft(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            node = Node(data)
            node.next = self.head
            self.head = node
        self.length += 1

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = Node(data)
        self.length += 1
    
    def __str__(self):
        if self.head is None:
            return "Linked list is empty!"
        res = "Head"
        node = self.head
        while node is not None:
            res += " -> " + str(node.data)
            node = node.next
        return res

    def __contains__(self, target):
        if self.head is None:
            return False
        node = self.head
        while node is not None:
            if node.data == target:
                return True
            node = node.next
        return False
    
    def popleft(self):
        if self.head is None:
            return None
        node = self.head
        self.head = self.head.next
        self.length -= 1
        return node.data
    
    def pop(self):
        if self.head is None:
            return None
        node = self.head
        while node.next is not None:
            prev = node
            node = node.next
        if node == self.head:
            self.head = None
        else:
            prev.next = node.next
        self.length -= 1
        return node.data

    def remove(self, target):
        node = self.head
        while node is not None and node.data != target:
            prev = node
            node = node.next
        if node is None: #실제로 연결리스트의 요소개수가 0이거나, 요소들이 있는데 검색해서 내가 찾는 target 값이 없을때
            return False
        if node == self.head: #target과 node.data가 동일해서 while문 건너뛰었을때, 첫번재 요소가 연결리스트에서 정답일때 찾는거일때
            self.head = self.head.next
        else:
            prev.next = node.next
        self.length -= 1
        return True
    
    # def insert(self, i, data):
    #     if i <= 0: #왼쪽 시작점에 요소를 넣고 싶을때
    #         self.appendleft(data)
    #     elif i >= self.length: #오른쪽 끝에 요소를 넣고 싶을때
    #         self.append(data)
    #     else:
    #         node = self.head
    #         for _ in range(i - 1):
    #             node = node.next
    #         new_node = Node(data)
    #         new_node.next = node.next
    #         node.next = new_node
    #         self.length += 1

    def insert(self, i, data):
        if i <= 0:
            self.appendleft(data)
        elif i >= self.length:
            self.append(data)
        else:
            node = self.head
            for _ in range(i - 1): #i -1번 시행해서 전 노드까지 가야함.
                node = node.next
            new_node = Node(data)
            new_node.next = node.next
            node.next = new_node
            self.length += 1









if __name__ =="__main__":
    import random
    my_list = LinkedList()
    for i in range(5):
        my_list.append(i)
    print(f"연결 리스트의 상태\n연결 리스트의 길이: {len(my_list)},{my_list}")
    print()
    for _ in range(5):
        i = random.randrange(10)
        data = random.randint(10,20)
        my_list.insert(i, data)
        print(f"{data}를 연결 리스트의 {i} 인덱스에 추가했습니다")
        print(f"연결 리스트의 길이 = {len(my_list)}, {my_list}\n")
