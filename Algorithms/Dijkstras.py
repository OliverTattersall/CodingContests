import heapq

def dijkstra(graph, start):

    distances = {vertex:float('inf') for vertex in graph}
    pq = []
    pq_update = {}
    distances[start] = 0

    for vertex, value in distances.items():
        entry = [vertex, value]
        heapq.heappush(pq, entry)
        pq_update[vertex] = entry

    while pq:
        # pq, pq_update,
        print( distances)
        item = heapq.heappop(pq)
        print(item)
        getmin = item[0]

        for neighbour, distance_neigh in graph[getmin].items():
            dist = distances[getmin] + distance_neigh
            if dist < distances[neighbour]:
                distances[neighbour] = dist
                pq_update[neighbour][1] = dist 

    # print(distances)
    return distances 




example_graph = {
    'U': {'V': 2, 'W': 5, 'X': 1},
    'V': {'U': 2, 'X': 2, 'W': 3},
    'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
    'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
    'Y': {'X': 1, 'W': 1, 'Z': 1},
    'Z': {'W': 5, 'Y': 1},
}
graph2={'A': {'B': 5, 'D': 5, 'E': 6}, 
        'B': {'A': 5, 'C': 4}, 
        'D': {'A': 5, 'C': 2, 'F': 6},
        'E': {'A': 6, 'C': 2, 'F': 1}, 
        'C': {'B': 4, 'D': 2, 'E': 2, 'F': 4},
        'F': {'C': 4, 'D': 6, 'E': 1}}
print(dijkstra(graph2, 'F'))


