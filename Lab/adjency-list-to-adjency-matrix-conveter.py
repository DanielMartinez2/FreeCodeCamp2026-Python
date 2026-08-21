def adjacency_list_to_matrix(graph):    
    x = len(graph)
    adj_matrix = [[0]*x for i in range(x)]    
    for index, (key, value) in enumerate(graph.items()):        
        for num in value:
            adj_matrix[key][num] = 1
    print(adj_matrix)
    return adj_matrix

adjacency_list_to_matrix({0: [2], 1: [2, 3], 2: [0, 1, 3], 3: [1, 2]})
    