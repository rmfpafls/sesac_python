class LinkedNode:
    def __init__(self, node_id, datum, next = None):
        self.node_id = node_id 
        self.datum = datum
        self.next = next 


class LinkedList:
    def __init__(self, elements):#elements = 1,2,3,4
        if elements == []:
            self.head = None 
            self.tail = None 
            self.end = None
            self.size = 0
        else:
            elements_list = list(elements)

            for idx, e in enumerate(elements_list):
                n = LinkedNode(node_id = idx, datum = e)
                elements_list[idx] = n
            
            for idx, e in enumerate(elements_list):
                if idx != len(elements_list) -1: 
                    e.next = elements_list[idx+1]
            elements_list[-1].next = None

            self.head = elements_list[0]
            self.tail = elements_list[1:]
            self.end = elements_list[-1]
            self.size = len(elements_list)


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
            cur = self.linked_list.head
            while cur != self.linked_list.end:
                res.append(cur.datum)
                cur = cur.next
            res.append(self.linked_list.end.datum)
            print("dkfrhfhdskf",res)
            return res

    def size(self):
        if self.backend == list:
            return len(self.list)
        elif self.backend == LinkedList:
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

    def dequeue(self):
        if self.backend == list:
            return self.list.pop()
        elif self.backend == LinkedList:
            result = self.linked_list.end.datum
            cur = self.linked_list.head
            prev = cur.next 
            cur = prev.next # 이거하면 prev- cur꼴 

            while cur != self.linked_list.end:
                prev = prev.next
                cur = cur.next
                
            prev.next = None
            
            return result
            



available_backends = [LinkedList]

for backend in available_backends:
    q1 = Queue(1,2,3,4, backend = backend)
    
    # assert q1.elements() == [1,2,3,4]
    # assert q1.size() == 4

    q1.enqueue(5)
    assert q1.elements() == [5,1,2,3,4]
    assert q1.size() == 5
    assert q1.dequeue() == 4
    assert q1.size() == 4
    assert q1.elements() == [5,1,2,3]
    assert q1.front() == 3 


# if __name__ == "__main__":
#     lst = LinkedList(1,2,3,4)

#     assert lst.head.datum == 1
#     assert lst.head.next.datum == 2
#     assert lst.head.next.next.datum == 3
#     assert lst.head.next.next.next.datum == 4
#     assert lst.head.next.next.next.next is None
#     assert lst.head.next.next.next == lst.end