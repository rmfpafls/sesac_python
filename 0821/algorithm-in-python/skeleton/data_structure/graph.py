class Vertex:
    def __init__(self, node_id, datum): # v1 = Vertex(0, 1)
        self.node_id = node_id 
        self.datum = datum

    def __eq__(self, other):
        if isinstance(self, Vertex) and isinstance(other, Vertex):
            return self.node_id == other.node_id
        return False 

    def __hash__(self): # hash : 임의의 데이터를 고정된 크기의 정수 값으로 변환하는 과정 또는 그 결과를 의미
        return hash((self.node_id, self.datum))

    def __str__(self):
        return str(self.datum)

class Edge:
    def __init__(self, from_vertex, to_vertex, is_directed = True, **data):
        assert isinstance(from_vertex, Vertex)    
        self.from_vertex = from_vertex

        assert isinstance(to_vertex, Vertex)
        self.to_vertex = to_vertex

        self.is_directed = is_directed
        self.data = data 
    
    def __eq__(self, other):
        if isinstance(self, Edge) and isinstance(other, Edge):
            return self.from_vertex == other.from_vertex and self.to_vertex == other.to_vertex


class AdjList: # value - edge로 연결되어 있는 꼴 
    def __init__(self, V, E):
        pass 

class AdjMatrix: 
    # vertex 별로 숫자를 부여
    # 영등포 구정 0 문래 1 신도림 2  
    def __init__(self, V, E):
        pass 