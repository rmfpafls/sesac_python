try:
    from node import Node 
except ModuleNotFoundError:
    from data_structure.node import Node

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
            elements_list = list(elements) 
            elements_list = [1,2,3,4]
            for i in range(len(elements_list)):
                if i != len(elements_list)-1: #다음값이 존재한다면
                    node = LinkedNode(node_id = i, datum = elements[i], next = elements[i+1])
                    node = LinkedNode(node_id = 0, datum = elements[0], next = elements[1])
                else: # 마지막값이면 next는 none
                    node = LinkedNode(node_id = i, datum = elements[i])
            
            self.head = elements[0]
            self.tail = elements[1:]
            self.end = elements[-1]
            self.size = len(elements)

    def __iter__(self):
        yield None 

    def __str__(self):
        res = ''
        return res 
    
    def append(self, elem):
        if not isinstance(elem,LinkedNode):
            elem = LinkedNode(self, size, elem, next = None)

        self.end.next  = LinkedNode(elem) 
        #이거 밑에 줄이랑 바꿔서 쓰면 next가 자기 자신을 가르키기 때문에 코딩 아작난다고 함
        self.end = elem
        self.size += 1 

class DoublyLinkedNode(Node):
    def __init__(self, node_id, datum, prev = None, next = None):
        self.node_id = node_id 
        self.datum = datum
        self.next = next 
        self.prev = prev 

class DoublyLinkedList:
    def __init__(self, elements):
        if elements == []:
            self.head = None 
            self.tail = None 
            self.end = None
            self.size = 0
        else:
            self.head = None 
            self.tail = None 
            self.end = None
            self.size = 0

    def __iter__(self):
        yield None 

    def __str__(self):
        res = ''

        return res 

if __name__ == '__main__':
    head = LinkedNode(0, 'a')
    node_list = []
    for i in range(10):
        node_list.append(LinkedNode(i, i*100))
    
    for idx, e in enumerate(node_list[:-1]):
        e.next = node_list[idx+1]
    
    node_list2 = []
    node_list2_elements = list(range(10))
    for i in node_list2_elements[:-1]:
        node = LinkedNode(i, i*100, next = node_list2_elements[i+1])
        node_list2.append(node)
    

    from code import interact
    interact(local = locals())
    