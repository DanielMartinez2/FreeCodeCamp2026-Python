def dfs(adj_matrix: list[list], node: int) -> list:    
    print("Matriz: ",adj_matrix)
    visited = [node]
    nodes = set(visited)           
    while visited:        
        current = visited.pop()
        print('Nó atual: ',current)
        for index, elem in enumerate(adj_matrix[current]):            
            if elem and index not in nodes:
                nodes.add(index)
                visited.append(index)
    return [x for x in nodes]    

#dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]], 1)
#print(dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]], 1))

#print(dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0]], 3))