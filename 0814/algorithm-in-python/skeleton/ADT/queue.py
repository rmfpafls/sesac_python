import sys 
sys.path.append('../data_structure')

try:
    from linked_list import LinkedList, LinkedNode, DoublyLinkedNode, DoublyLinkedList
except ModuleNotFoundError:
    from data_structure.linked_list import LinkedList, LinkedNode, DoublyLinkedNode, DoublyLinkedList

class Queue:
    def __init__(self, *elements, backend = list):
        assert isinstance(elements, list) or isinstance(elements, tuple)

        self.backend = backend
        if self.backend == list:
            self.list = list(elements) #elements = 1,2,3,4 # self.list = [1,2,3,4]

        elif self.backend == LinkedList:

            self.linked_list = LinkedList(elements) # make right linked list 

    def elements(self): # q1 = Queue(1,2,3,4, backend = backend)
        if self.backend == list:
            return self.list 
        
        elif self.backend == LinkedList:
            res = []
            if self.linked_list.head is None:
                return res
            elif self.linked_list.head.next == None: 
                res.append(self.linked_list.head.datum)
                # print("This is res :", res)
                return res 
            
            cur = self.linked_list.head
            while cur != self.linked_list.end:
                res.append(cur.datum)
                cur = cur.next
            res.append(self.linked_list.end.datum)
            # print("dkfrhfhdskf",res)
            return res

    def size(self):
        if self.backend == list:
            return len(self.list)
        elif self.backend == LinkedList:
            if self.linked_list.head is None:
                return 0
            elif  self.linked_list.head.next is None: 
                return 1
            
            cur = self.linked_list.head
            prev = cur.next
            cur = prev 
            count = 2
            while prev.next != None and cur.next != None:
                prev = prev.next
                cur = cur.next
                count += 1 
            return count
                

    
    def enqueue(self, elem):
        if self.backend == list:
            self.list = [elem] + self.list 

        elif self.backend == LinkedList:
            self.linked_list.head = LinkedNode('id', elem, self.linked_list.head)
            print("This is self.linked_list.head.datum : ", self.linked_list.head.datum)

    def dequeue(self):
        if self.backend == list:
            return self.list.pop()
        elif self.backend == LinkedList:
            result = self.linked_list.end
            cur = self.linked_list.head
            prev = cur.next 
            cur = prev.next # 이거하면 prev- cur꼴 

            while cur != self.linked_list.end:
                prev = prev.next
                cur = cur.next
            
            
            prev.next = None
            self.linked_list.end = prev

            return result.datum
        
    def front(self):
        if self.backend == list:
            return self.list[-1]
        elif self.backend == LinkedList: 
            return self.linked_list.end.datum
        
    def is_empty(self):
        if self.backend == list:
            return self.list == []
        elif self.backend == LinkedList: 
            return self.linked_list.head is None
            

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
        self.backend = backend
        # 정렬하고 넘길거에요^^히히.. LinkedList로 만들고 정렬할 수도 있음!! 
        # 그건 use_merge 파일에 있음! 
        self.list = list(elements_with_priority)
        for i in range(len(self.list)): 
            for j in range(i+1, len(self.list)):
                if self.list[i][1] > self.list[j][1]: 
                    self.list[i], self.list[j] = self.list[j], self.list[i]
        
        if self.backend == list:
            self.list = self.list
        
        elif self.backend == LinkedList:
            self.linked_list = LinkedList(tuple(self.list))

    

    def elements(self): # 우선순위대로 정렬해야됨 
        if self.backend == list:
            print("PriorityQueue의 List elements(): ", self.list)
            return self.list 
        
        elif self.backend == LinkedList:
            res = []
            cur = self.linked_list.head
            while cur != self.linked_list.end:
                # print("cur.datum[1] 값 : ", cur.datum[1])
                res.append(cur.datum)
                cur = cur.next
            res.append(self.linked_list.end.datum)
            print("PriorityQueue의 LinkedList elements(): ",res)
            return res



    def enqueue(self, elem):
        if self.backend == list:
            self.list.append(elem)
            return 

        # assert not q2.is_empty()
        # q2.dequeue()
    def dequeue(self):
        if self.backend == list:
            return self.list.pop()
        elif self.backend == LinkedList:
            if self.size() > 2:
                result = self.linked_list.end
                cur = self.linked_list.head
                prev = cur.next 
                cur = prev.next # 이거하면 prev- cur꼴 

                while cur != self.linked_list.end:
                    prev = prev.next
                    cur = cur.next

                prev.next = None
                self.linked_list.end = prev
                print("This is result.datum", result.datum)
                return result.datum
            else: #리스트에 2개 1개있는 경우
                if self.linked_list.head.next == None: # 1개 남아있는 경우
                    result = self.linked_list.head
                    self.linked_list = []
                    return result
                else: # 2개 남아있는 경우 
                    result = self.linked_list.end.datum
                    self.linked_list.head.next = None
                    return result
                    
                
    def front(self):
        if self.backend == list:
            return self.list[-1]
        elif self.backend == LinkedList: 
            return self.linked_list.end.datum

    def size(self):
        if self.backend == list:
            return len(self.list)
        elif self.backend == LinkedList:
            if self.linked_list.head is None:
                return 0
            elif  self.linked_list.head.next is None: 
                return 1
            
            cur = self.linked_list.head
            prev = cur.next
            cur = prev 
            count = 2
            while prev.next != None and cur.next != None:
                prev = prev.next
                cur = cur.next
                count += 1 
            return count

    
    def is_empty(self):
        if self.backend == list:
            return self.list == []
        elif self.backend == LinkedList: 
            print("is_empty의 self.linked_list : ", self.linked_list) 
            return self.linked_list == []

    def __str__(self):
        return str(self.elements())

    def __eq__(self, other):
        if isinstance(other, Queue):
            return self.elements == other.elements 
        return False 

if __name__ == '__main__':
    available_backends = [list, LinkedList] #DoublyLinkedList , , LinkedList

    for backend in available_backends:
        # q1 = Queue(1,2,3,4, backend = backend)
        
        # assert q1.elements() == [1,2,3,4]
        # assert q1.size() == 4
        
        # q1.enqueue(5)
        # assert q1.elements() == [5,1,2,3,4]
        # assert q1.size() == 5
        # assert q1.dequeue() == 4
        # assert q1.size() == 4
        # assert q1.elements() == [5,1,2,3]
        # assert q1.front() == 3 


        # q2 = Queue(backend = backend)

        # assert q2.elements() == []
        # assert q2.size() == 0
        # assert q2.is_empty()
        
        # q2.enqueue(1)

        # assert q2.elements() == [1]
        # assert q2.size() == 1
        # assert not q2.is_empty()
        
        # if backend == LinkedList:
        #     print(q1.linked_list, q2.linked_list)
    
        q2 = PriorityQueue(('c',1), ('d',4), ('e',2), ('b',3), backend = backend)
        #왜 enqueue()는 없음?????!?!?!
        assert q2.elements() == [('c',1), ('e',2), ('b',3), ('d',4)]
        assert q2.size() == 4 
        assert q2.front() == ('d', 4) 
        assert not q2.is_empty()
        q2.dequeue()

        assert q2.elements() == [('c',1), ('e',2), ('b',3)]
        assert q2.size() == 3 
        assert q2.front() == ('b', 3) 
        assert not q2.is_empty()

        q2.dequeue()
        q2.dequeue()
        q2.dequeue()
    
        assert q2.is_empty()
        ## 완성! 
        


