class Tree:
    def __init__(self, root, children = []):
        self.root = root
        self.children = children

    def root_datum(self):
        print("첫째", self.root)
        return self.root 
    
    def height(self): #  assert t1.height() == 3
        count = 1
        while self.children != []:
            count += 1
        print(count)
        return count 

        
    def __str__(self):
        pass


        

    
if __name__ == '__main__':
    t1 = Tree(1, [
                Tree(11, [Tree(111), Tree(112)],), 
                Tree(12, [Tree(121), Tree(122), Tree(123),])
             ]
         )
    # Tree(self, root, children), self = t1, root =1 , children = []
    print("값: ",t1.root)
    print("t1.height()", t1.height())
    t1.root_datum()
    assert t1.root_datum() == 1 
    assert t1.height() == 3 # 본인 포함해서 밑에 딸린 애들이 몇 개냐 
    # 맨마지막 애의 children은 [] 빈리스트