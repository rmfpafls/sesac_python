import sys 
sys.path.append('../data_structure') # 주소 안에 있는 코드를 사용할 수 있음

try:
    from linked_list import LinkedList, LinkedNode, DoublyLinkedNode, DoublyLinkedList
except ModuleNotFoundError:
    from data_structure.linked_list import LinkedList, LinkedNode, DoublyLinkedNode, DoublyLinkedList

class Queue: # 먼저 들어온 놈이 먼저임
    def __init__(self, *elements, backend = list): # q1, 1,2,3,4, 
        assert isinstance(elements, list) or isinstance(elements, tuple)

        self.backend = backend # 큐라는 거는 약속이에요. 약속을 어떻게 구현할건데? 저는 리스트요 backend가 리스트

        if self.backend == list:
            self.list = list(elements) 

        elif self.backend == LinkedList: #elements = 1,2,3,4
            self.linked_list = LinkedList(elements)
            # [<__main__.LinkedNode object at 0x0000029D36115990>, <__main__.LinkedNode object at 0x0000029D361159D0>, <__main__.LinkedNode object at 0x0000029D36115A10>, <__main__.LinkedNode object at 0x0000029D36115A50>]<__main__.Queue object at 0x0000029D36115790>

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
                
    def front(self): 
        if self.backend == list:
            return self.list[-1]
        elif self.backend == LinkedList:
            return self.list[-1].datum

    def size(self):
        if self.backend == list:
            return len(self.list)
        elif self.backend == LinkedList: 
            return len(self.list)
    
    def is_empty(self):
        if self.backend == list:
            return self.list == []
        elif self.backend == LinkedList:
            return self.list == []

    def __str__(self):
        return str(self.elements())

    def __eq__(self, other):
        if isinstance(other, Queue):
            return self.elements == other.elements 
        return False 

class PriorityQueue: #큐랑 생긴게 똑같아요. 우선순위가 먼저고 거기서 들어온 순서대로 계산 
    def __init__(self, *elements_with_priority, backend = list):
        """Get list of 2-tuple containing (obj, number), which denotes object and its priority. Higher the number, the element have hight priority. 
        숫자가 높을수록 우선순위가 높아요 
        """
        # self = q2, elements_with_priority = ('c',1), ('d',4), ('e',2), ('b',3), backend = backend) 
        # self.list = list(elements_with_priority)
        # print(self.list)


    def elements(self):
        if self.backend == list:
            return self.list 

    def enqueue(self, elem):
        if self.backend == list:
            self.list.append(elem)

    def dequeue(self):
        if self.backend == list:
            return self.list.pop()
                
    def front(self):
        if self.backend == list:
            return self.list[-1]

    def size(self):
        if self.backend == list:
            return len(self.list)
    
    def is_empty(self):
        if self.backend == list:
            return self.list == []

    def __str__(self):
        return str(self.elements())

    def __eq__(self, other):
        if isinstance(other, Queue):
            return self.elements == other.elements 
        return False 

if __name__ == '__main__':
    available_backends = [list, LinkedList]#, DoublyLinkedList]

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
        ### 여기까지 통과할 수 있어야돼요 


        # q2 = PriorityQueue(('c',1), ('d',4), ('e',2), ('b',3), backend = backend)
        # #(c,1) 앞에있는게 ?? 
        # assert q2.elements() == [('c',1), ('e',2), ('b',3), ('d',4)]
        # assert q2.size() == 4 
        # assert q2.front() == ('d', 4)  # 맨 마지막 빠진 놈 
        # assert not q2.is_empty()
        # q2.dequeue()

        # assert q2.elements() == [('c',1),('e',2), ('b',3)]
        # assert q2.size() == 3 
        # assert q2.front() == ('b', 3) 
        # assert not q2.is_empty()

        # q2.dequeue()
        # q2.dequeue()
        # q2.dequeue()
        # q2.dequeue()

        # assert q2.is_empty()


