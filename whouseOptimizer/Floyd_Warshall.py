
nV = 4

INF = 999

  # Instancier le modèle
dist_matrix = prob._dist_matrix


def floydWarshall(graph):
    dist = list(map(lambda i : list(map(lambda j : j, i)), graph) )
    
    for k in range(nV): 
        for i in range(nV): 
            for j in range(nV): 
                dist[i][j] = min(dist[i][j], dist[i][k]+ dist[k][j]) 
    printSolution(dist) 

def printSolution(dist): 
    for i in range(nV): 
        for j in range(nV): 
            if(dist[i][j] == INF): 
                print("INF", end =" ")
            else: 
                print(dist[i][j], end ="  ")  
        print(" ")

#INF si il n'y a pas d'arc entre i et j
#0 quand i = j
graph = [[0, 3, INF, 5],
        [2, 0, INF, 4],
        [INF, 1, 0, INF],
        [INF, INF, 2, 0]]

floydWarshall(graph)



