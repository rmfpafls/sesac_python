try:
    from node import Node 
except ModuleNotFoundError:
    from data_structure.node import Node

class TreeNode:
    def __init__(self, node_id, datum):
        self.node_id = node_id
        self.datum = datum 

class Tree:
    def __init__(self, root, children = []):
        self.root = self.root
        self.children = children
        return 

    def iter_nodes(self):
        pass

    def iter_nodes_with_address(self):
        pass

    def __iter__(self):
        pass 

    def insert(self, address, elem):
        pass 

    def delete(self, address):
        pass
        
    def search(self, elem):
        pass 

    def root_datum(self):
        pass 

    def height(self):
        pass 

    def __str__(self):
        pass 


if __name__ == '__main__':
    t1 = Tree(1, [
                Tree(11, [Tree(111), Tree(112)],), 
                Tree(12, [Tree(121), Tree(122), Tree(123),])
             ]
         )
    # Tree(self, root, children), self = t1, root =1 , children = []
    print(t1)
    
    assert t1.root_datum() == 1 
    assert t1.height() == 3 # 본인 포함해서 밑에 딸린 애들이 몇 개냐 
    # 맨마지막 애의 children은 [] 빈리스트

    for addr, n in t1.iter_nodes_with_address():
        assert [int(e)-1 for e in list(str(n.datum))[1:]] == addr # 3자식 [0][1]의 부모가 [0]이 맞는지 확인하려면 [1]을 빼면 돼 
        assert t1.search(n.datum) == addr 

    t1.insert([2], Tree(13, [Tree(131), Tree(132), Tree(133)])) # [2] 위치에 밑에 tree를 넣겠다 
    t1.insert([1, 1], Tree(122, [Tree(1221), Tree(1222)]))

    print(t1)
    
    assert 122 == t1.delete([1,2])
    assert 123 == t1.delete([1,2])

    for addr, n in t1.iter_nodes_with_address(): #지우는거  
        #부모를 죽이면 자식을 죽여야돼?말아야돼? = 죽여도 되고 안죽여도돼 
        # 근데 여기서는 다 죽이는 대학살극을 펼칠거에요 : 24.08.16 강사님.
        assert [int(e)-1 for e in list(str(n.datum))[1:]] == addr 
        assert t1.search(n.datum) == addr 

    print(t1)