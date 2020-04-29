
inf = 1e10 

def floyd_warshall(weights):
    V = len(weights)
    dist_matrix = weights
    for k in range(V):
        next_dist_matrix = [list(row) for row in dist_matrix] # make a copy of distance matrix
        for i in range(V):
            for j in range(V):
                next_dist_matrix[i][j] = min(dist_matrix[i][j], dist_matrix[i][k] + dist_matrix[k][j])
        dist_matrix = next_dist_matrix # update
    return dist_matrix


graph = [
    [0, inf, inf, -3],
    [inf, 0, inf, 8],
    [inf, 4, 0, -2],
    [5, inf, 3, 0]
]

print(floyd_warshall(graph))


