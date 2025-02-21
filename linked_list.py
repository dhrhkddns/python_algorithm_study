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
            res += " → " + str(node.data)
            node = node.next
        return res 
    

    # def __contains__(self, target): #if --- in : 할때마다 자동으로 오버로딩되서 실행되는 메소드
    #     if self.head is None:
    #         return False
    #     node = self.head #처음 노드는 모르는 걸 전제로 하기때문에 head는 알고 있으니까 self.head를 노드에 할당해야함.
    #     while node is not None: #연결 리스트 처음부터 끝까지 탐색하기 위해서 while을 적용함.
    #         if node.data == target:
    #             return True #if문에 True 전달함. 리턴값으로 값이 연결 리스트 안에 있다는 뜻임.
    #         node = node.next #현재 노드에는 요소가 없기 때문에 다음 노드로 하고 노드 변수 갱신
    #     return False #다 돌아도 요소가 없음.





    def __contains__(self, target): #오버로딩 특이한 실행조건을 가진 메소드로 if i in my_list에서 i를 target 파라미터로 받고, my_list는 self로 받는 메소드.
        if self.head is None: #head에 노드 자체가 없는 경우는 시작조차 안한, 즉 연결 리스트에 아무것도 없어서 보나마나 할 것 없이 False여서 return으로 False값을 준다.
            return False
        node = self.head #일단 연결리스트에서 처음 접근은 노드에 self.head 헤드를 할당하는 식으로 그다음에는 next로 하나씩 접근 해야함. head를 node에 할당해야함.
        while node is not None: #현재 head에 있는 노드가 존재할때, 즉 연결 리스트에 뭐라도 요소가 존재하는 경우.
            if node.data == target: #현재 노드에 있는 데이터가 target, i의 값과 일치할때, 연결 리스트에 내가 검색하는 값이 있기 때문에 return True로 반환해준다.
                return True
            node = node.next #현재 노드에는 target데이터가 없어서 다음 값을 검색하기 위해서 next로 넘겨서 node를 갱신한다. -> -> ->
        
        ### 이상태는 모든 node는 None이고 끝까지 간 상태, 그러므로 다 검색해도 target은 연결리스트에 없는 상황.
        return False
        











if __name__ == "__main__":
    import random
    data = list(range(10,20))
    random.shuffle(data)
    my_list = LinkedList()
    for i in data:
        my_list.append(i)
    print(f"연결 리스트의 상태\n{my_list}")
    print(type(my_list))
    print()
    for _ in range(4):
        i = random.randint(5,25)
        if i in my_list: #__contains__ 오버로딩 메소드 자동으로 실행.
            print(f"{i}는 연결 리스트에 있습니다!")
        else:
            print(f"{i}는 연결 리스트에 없습니다!")

if __name__ == "__main__": #이 스크립트에서 직접 실행할때
    import random #리스트를 랜덤으로 섞어서 예시로 넣어줄거라서
    data = list(range(10,20)) #10....19 총 10개의 요소를 data에 일단 넣는다.
    random.shuffle(data) #반환값 없이 그냥 현재 data는 오름차순인데 랜덤으로 섞어버림.
    my_list = LinkedList() # 클래스 객체 여기에 append할거라서 '연결 리스트' 객체 생성!
    for i in data: #data를 하나하나씩 인덱스 0 부터 -1까지 다 append해준다.
        my_list.append(i)
    
    ####for문이 끝난 상황, 즉 연결리스트에 요소들이 다 들어가 있는 상태.
    print(f"연결 리스트의 상태\n{my_list}") #오버로딩 __str__을 트리거해서 연결 리스트 상태를 다음줄에 출력해줌 19->4>6->25...
    print(type(my_list))
    print()

    for _ in range(4): #총 4번 확인하는 용도 _는 굳이 저걸 쓰지 않겠다. 횟수를 4번 하겠다가 강한 뉘앙스임.
        i = random.randint(15,25) #연결리스트에 있는지 확인할 임의의 integer 생성.
        if i in my_list: #여기서 오버로딩 직접 메소드 호출안해도 if in 사용하면 __contains__ 자동으로 호출됨. my_list는 self 인자, i는 target 인자로 전송됨.
            print(f"{i}는(은) 연결 리스트에 있습니당!")
        else:
            print(f"{i}는(은) 연결 리스트에 없습니당:(")

