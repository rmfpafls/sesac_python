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

    def __iter__(self):
        yield None 

    def __str__(self):
        res = ''

        return res 

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

if __name__ == "__main__":
    lst = LinkedList(1,2,3,4)

    assert lst.head.datum == 1
    assert lst.head.next.datum == 2
    assert lst.head.next.next.datum == 3
    assert lst.head.next.next.next.datum == 4
    assert lst.head.next.next.next.next is None
    assert lst.head.next.next.next == lst.end