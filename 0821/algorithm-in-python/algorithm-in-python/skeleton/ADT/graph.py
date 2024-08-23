import sys 
sys.path.append('../data_structure')

try:
    from graph_datastructure import AdjList, AdjMatrix, Vertex, Edge
except ModuleNotFoundError:
    from data_structure.graph_datastructure import AdjList, AdjMatrix, Vertex, Edge


class Graph:
    def __init__(self, V, E, backend = 'VE'): 
        #VE, 'adjacent_list', 'adjacnet_matrix'
        for v in V:
            assert isinstance(v, Vertex) 
        for e in E:
            assert isinstance(e, Edge)
            assert e.from_vertex in V 
            assert e.to_vertex in V 

        self.V = V 
        self.E = E 

        if backend == 'VE':# value - edge
            pass 
        elif backend == 'adjacent_list':
            pass 
        elif backend == 'adjacnet_matrix':
            pass 

    def add_vertex(self, v): # vertex를 추가
        assert isinstance(v, Vertex)
        self.V.append(v)
    
    def remove_vertex(self, v): 
        # vertex : vertex를 제거
        # 관련된 edge도 제거해야됨 
        assert isinstance(v, Vertex)
        self.V.remove(v)

        for i in self.E:
            if i.from_vertex == v or i.to_vertex == v: 
                self.E.remove(i)


    def add_edge(self, e): # edge를 추가 
        assert isinstance(e, Edge)
        self.E.append(e)

    def remove_edge(self, e): # edge를 제거
        # g1.remove_edge(e6)
        assert isinstance(e, Edge)
        self.E.remove(e)


    def get_vertices(self): # 노드 값들만 반환
        result = []
        for i in self.V:
            result.append(i.datum)
        print("get_vertices : ", result)
        return result

    def get_neighbors(self, v): # 그 노드의 이웃들만 반환
        assert isinstance(v, Vertex)
        neighbors_result = []
        for j in self.E: 
            if j.from_vertex == v:
                neighbors_result.append(j.to_vertex)
            elif j.to_vertex == v: 
                neighbors_result.append(j.from_vertex)
        neighbors_result = list(set(neighbors_result)) 

        # for z in range(len(neighbors_result)): 
        #     for y in range(1, len(neighbors_result)):
        #         if neighbors_result[z].datum > neighbors_result[y].datum: 
        #             neighbors_result[z], neighbors_result[y] = neighbors_result[y], neighbors_result[z]

        print(f"{v}'s neighbors :", [i.datum for i in neighbors_result])
        return neighbors_result

    def dfs(self, src): #깊이 우선 탐색
        assert isinstance(src, Vertex)
        # self = g1.neighbors_result[z]
        # src는 시작점 v1= Vertex(0,1)처럼 vertex객체가 들어감 
        # 그래프의 모든 vertex를 root에서 시작하여 각각 dfs, bfs로 순회

        # 1. src 값에서 시작해 get_neighbor를 사용해서 이웃 중에 하나로 
        # 2. 그 이웃의 방문하지않은 이웃으로 
        # 3. 계속하다가 없으면 그 전 이웃으로 들어와서 get_neighbor 중에 방문하지 않은 값이 있으면 다시 거기로 들어가 
        # 이걸 재귀로 하면 돼
        # 는데 말이 쉽지

        dfs_result = [src]
        dfs_visited = [src]

        def in_to_the_dfs(self,src):
            while get_neighbors(self,src) != []:
                for i in get_neighbors(self,src): 
                    if i not in dfs_visited: 
                        dfs_visited.append(i)
                        return in_to_the_dfs(self, i)
        return in_to_the_dfs(self, src)
        
        print("dfs result : ",[i.datum for i in dfs_visited])
    


        

        
         
            

    def bfs(self, src):
        assert isinstance(src, Vertex) 
        # 강사님이 v1에서 v2를 먼저가던 v3를 먼저 가던 상관 없다고 하셨음
        visited = [src] #방문한 노드 리스트
        result = []

        while visited != []: 
            for i in visited: 
                neighbors = self.get_neighbors(i)
                for j in neighbors:
                    if j not in visited and j not in result: 
                        visited.append(j)
                result.append(visited.pop(0))
        
        print_result = []
        for k in result:
            print_result.append(k.datum)
        print("bfs result : ", print_result) 




    # Do not modify this method

    @staticmethod 
     # @: 클래스 안에 정의된 메서드가 인스턴스나 클래스에 의존하지 않고 독립적으로 동작할 때 사용 
    def spring_layout(nodes, edges, iterations=50, k=0.1, repulsion=0.01):
        import numpy as np
        # Initialize positions randomly
        positions = {node: np.random.rand(2) for node in nodes}
        
        for _ in range(iterations):
            forces = {node: np.zeros(2) for node in nodes}
            
            # Repulsive forces between all pairs of nodes
            for i, node1 in enumerate(nodes):
                for j, node2 in enumerate(nodes):
                    if i != j:
                        diff = positions[node1] - positions[node2]
                        dist = np.linalg.norm(diff)
                        if dist > 0:
                            forces[node1] += (diff / dist) * repulsion / dist**2
            
            # Attractive forces for connected nodes
            for edge in edges:
                node1, node2 = edge.from_vertex, edge.to_vertex
                diff = positions[node2] - positions[node1]
                dist = np.linalg.norm(diff)
                
                if dist > 0:
                    force = k * (dist - 1)  # spring force
                    forces[node1] += force * (diff / dist)
                    forces[node2] -= force * (diff / dist)
            
            # Update positions
            for node in nodes:
                positions[node] += forces[node]
        
        return positions

    def show(self):
        import matplotlib.pyplot as plt
        nodes = self.V 
        edges = self.E 
        positions = Graph.spring_layout(nodes, edges)
        plt.figure(figsize=(8, 6))
        ax = plt.gca()

        # Plot nodes
        for node, pos in positions.items():
            ax.scatter(*pos, s=2000, color='lightblue')
            ax.text(*pos, node, fontsize=20, ha='center', va='center')

        # Plot edges
        for edge in edges:
            node1, node2 = edge.from_vertex, edge.to_vertex
            x_values = [positions[node1][0], positions[node2][0]]
            y_values = [positions[node1][1], positions[node2][1]]
            ax.plot(x_values, y_values, color='gray', linewidth=2)

        ax.set_title("Graph Visualization with Spring Layout", fontsize=20)
        ax.set_xticks([])
        ax.set_yticks([])
        plt.show()


if __name__ == '__main__':
    v1 = Vertex(0, 1) # data_structure의 Vertex
    v2 = Vertex(1, 2)
    v3 = Vertex(2, 3)
    v4 = Vertex(3, 4)
    v5 = Vertex(4, 5)

    e1 = Edge(v1, v2) 
    e2 = Edge(v1, v3) 
    e3 = Edge(v2, v3)
    e4 = Edge(v2, v4)
    e5 = Edge(v3, v5) 
    e6 = Edge(v4, v5)

    V = [v1, v2]
    E = [e1]

    g1 = Graph(V, E) 

    g1.add_vertex(v3)
    g1.add_vertex(v4)
    g1.add_vertex(v5)

    g1.add_edge(e2)
    g1.add_edge(e3)
    g1.add_edge(e4)
    g1.add_edge(e5)
    g1.add_edge(e6)

    #여기서부터는 내가 짠 테스트 코드 

    g1.bfs(v1)
    g1.dfs(v1)
    g1.remove_edge(e6)
    g1.remove_vertex(v4)
    g1.get_vertices()
    g1.get_neighbors(v1)

    g1.show()



