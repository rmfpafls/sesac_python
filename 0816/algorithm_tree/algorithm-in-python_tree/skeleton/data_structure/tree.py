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
        self.root = TreeNode(node_id= root, datum = root)
        self.children = children

    def iter_nodes(self): # 노드 자체
        yield self.root  

        for child in self.children:
            for n in child.iter_nodes():
                yield n
        # 1
        # 11 11 111 112 113
        # 12 121 122 123 순으로 쌓이게 됨 

    def iter_nodes_with_address(self): # for addr, n in t1.iter_nodes_with_address(): 
        # addr = [1,1] , n = node 
        yield [], self.root 
        # 루트 노드와  그 주소(빈 리스트)를 반환 
        # yield는 일회성 함수라서 재귀로 돌아왔을 때 실행되지 않음

        for idx, child in enumerate(self.children):# 각 자식 트리에 대해
            for addr, n in child.iter_nodes_with_address():
                yield [idx] + addr, n 
        # [], 1
        # [0], 11
        # [0,0] ,111
        # [0,1] . 112
        # [1], 12
        # [1,0] , 121
        # [1,1] , 122
        # [1,2] , 123


    def __iter__(self):
        yield self.root.datum

        for child in self.children:
            for n in child.iter_nodes():
                yield n 
        # iter_nodes와 같은 순서대로 돌지만 datum 값을 yield에 저장
  

    def insert(self, address, elem):
    # t1.insert([2], Tree(13, [Tree(131), Tree(132), Tree(133)])) # [2] 위치에 밑에 tree를 넣겠다 
    # t1.insert([1, 1], Tree(122, [Tree(1221), Tree(1222)]))
        #부모가 같으면 자식 리스트에 elem을 넣으면 돼
        
        parent = address[:-1]

        if parent == []: 
            self.children.append(elem)
        else:
            cur = self
            for addr in address[:-1]: 
                cur = cur.children[addr]
            cur.children.insert(address[-1], elem)



    def delete(self, address):
        pass
        
    def search(self, elem): # assert t1.search(n.datum) == addr
        find = self.iter_nodes_with_address()

        for i,j in find: 
            if j.datum == elem: 
                print("search(self,elem) : ", i)
                return i
                            

    def root_datum(self):
        print("****************root_datum : ", self.root.datum)
        return self.root.datum

    def height(self): #  assert t1.height() == 3
        count = 1
        if self.children == []:
            return count
        else: 
            for child in self.children: 
                child.height() 
                count += 1 
            return count

    # def __str__(self):
    #     pass 


if __name__ == '__main__':
    t1 = Tree(1, [
                Tree(11, [Tree(111), Tree(112)],), 
                Tree(12, [Tree(121), Tree(122), Tree(123),])
             ]
         )
    # Tree(self, root, children), self = t1, root =1 , children = []
    print("t1 :",t1)
    
    assert t1.root_datum() == 1 
    assert t1.height() == 3 # 본인 포함해서 밑에 딸린 애들이 몇 개냐 
    # 맨마지막 애의 children은 [] 빈리스트

    for addr, n in t1.iter_nodes_with_address():
        assert [int(e)-1 for e in list(str(n.datum))[1:]] == addr # 3자식 [0][1]의 부모가 [0]이 맞는지 확인하려면 [1]을 빼면 돼 
        assert t1.search(n.datum) == addr 

    t1.insert([2], Tree(13, [Tree(131), Tree(132), Tree(133)])) # [2] 위치에 밑에 tree를 넣겠다 
    t1.insert([1, 1], Tree(122, [Tree(1221), Tree(1222)]))

    print("t1 :", t1)
 
    assert 122 == t1.delete([1,2])
    assert 123 == t1.delete([1,2])

    for addr, n in t1.iter_nodes_with_address(): #지우는거  
        #부모를 죽이면 자식을 죽여야돼?말아야돼? = 죽여도 되고 안죽여도돼 
        # 근데 여기서는 다 죽이는 대학살극을 펼칠거에요 : 24.08.16 강사님.
        assert [int(e)-1 for e in list(str(n.datum))[1:]] == addr 
        assert t1.search(n.datum) == addr 

    print(t1)