# q1 = Queue(1,2,3,4, backend = backend)
# assert q1.elements() == [1,2,3,4]     

class Queue: # 먼저 들어온 놈이 먼저임
    def __init__(self, *elements, backend = list): # q1, 1,2,3,4, 
        assert isinstance(elements, list) or isinstance(elements, tuple)

        self.backend = backend # 큐라는 거는 약속이에요. 약속을 어떻게 구현할건데? 저는 리스트요 backend가 리스트

        if self.backend == list:
            self.list = list(elements) 

        elif self.backend == LinkedList: #elements = 1,2,3,4
            elements_list = list(elements) # self.list = [1,2,3,4]
            self.list = [] 
            for i in range(len(elements_list)):
                if i != len(elements_list)-1: #다음값이 존재한다면
                    node = LinkedNode(node_id = i, datum = elements[i], next = elements[i+1])
                    self.list.append(node)
                else: # 마지막값이면 next는 none
                    node = LinkedNode(node_id = i, datum = elements[i])
                    self.list.append(node)
            print("self.list의 값", self.list, "\n") 
            # 출력값 : [<__main__.LinkedNode object at 0x0000029D36115990>, <__main__.LinkedNode object at 0x0000029D361159D0>, <__main__.LinkedNode object at 0x0000029D36115A10>, <__main__.LinkedNode object at 0x0000029D36115A50>]<__main__.Queue object at 0x0000029D36115790>
            self.Linked_list = LinkedList(self.list)

    def elements(self): 
        #self에는     q1 = Queue(1,2,3,4, backend = backend) 한 값이 들어가있음
        #element(q1) == [1,2,3,4]가 되어야함 
        if self.backend == list:
            return self.list 
        elif self.backend == LinkedList:
            print("element에서 실행된 값", self.list)
            new_list = []
            for i in self.list: 
                new_list.append(i.datum)
            print("제발되라",new_list,"\n")
            return new_list
        
    def enqueue(self, elem): # 삽입 
        # self = q1 elem = 추가할 값
        if self.backend == list:
            self.list = [elem] + self.list
        elif self.backend == LinkedList: 
            #elem에 대한 정의
            if self.list != []: 
                Linked_elem = LinkedNode(node_id = elem, datum = elem, next = self.list[0].datum)
            else:
                Linked_elem = LinkedNode(node_id = elem, datum = elem)
                
            self.list = [Linked_elem] + self.list
            new_list = []
            for i in self.list:
                new_list.append(i.datum)
            print("제발제발되라", new_list)             
            return new_list
        
    def dequeue(self): #맨 뒤 제거
        if self.backend == list:
            return self.list.pop()
        elif self.backend == LinkedList: 
            self.list[-2].next == None
            pop_ele = self.list.pop()
        print("dfsfsfsfsf",self.list)
        return pop_ele.datum
    
    def size(self):
        if self.backend == list:
            return len(self.list)
        elif self.backend == LinkedList: 
            return len(self.list)
     
    def front(self): 
        if self.backend == list:
            return self.list[-1]
        elif self.backend == LinkedList:
            return self.list[-1].datum
        
    def is_empty(self):
        if self.backend == list:
            return self.list == []
        elif self.backend == LinkedList:
            return self.list == []


            


class LinkedNode:
    def __init__(self, node_id, datum, next = None):
        self.node_id = node_id 
        self.datum = datum
        self.next = next 

class LinkedList:
    def __init__(self, elements): # elements에 list 타입으로 들어올거임 
        if elements == []: # 안건들여도 됨. 빈값이면 None
            self.head = None 
            self.tail = None 
            self.end = None
            self.size = 0 #하나 넣을때마다 +1 뺄때마다 -1
        else:
            self.head = elements[0]
            self.tail = elements[1:]
            self.end = elements[-1]
            self.size = len(elements)



available_backends = [LinkedList]

for backend in available_backends:
        q1 = Queue(1,2,3,4, backend = backend)
        
        assert q1.elements() == [1,2,3,4]
        assert q1.size() == 4

        q1.enqueue(5)
        assert q1.elements() == [5,1,2,3,4]
        assert q1.size() == 5
        assert q1.dequeue() == 4
        assert q1.size() == 4
        assert q1.elements() == [5,1,2,3]
        assert q1.front() == 3 

        q2 = Queue(backend = backend)

        assert q2.elements() == []
        assert q2.size() == 0
        assert q2.is_empty()
        
        q2.enqueue(1)

        assert q2.elements() == [1]
        assert q2.size() == 1
        assert not q2.is_empty()
        
        if backend == LinkedList:
            print(q1.linked_list, q2.linked_list)
