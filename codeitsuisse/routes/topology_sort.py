# def topology_sort(adjacency_list, visited_list, output_stack, vertex):
#     if not visited_list[vertex]:
#         visited_list[vertex] = True
#         for neighbor in adjacency_list[vertex]:
#             topology_sort(adjacency_list, visited_list, output_stack, neighbor)
#         output_stack.insert(0, vertex)
from collections import defaultdict, deque

GRAY, BLACK = 0, 1

def topological(graph):
    order, enter, state = deque(), set(graph), {}
    # error = False
    def dfs(node):
        state[node] = GRAY
        for k in graph.get(node, ()):
            sk = state.get(k, None)
            if sk == GRAY: 
                # error = True
                return list(order) #, error
            if sk == BLACK: 
                continue
            enter.discard(k)
            dfs(k)
        order.appendleft(node)
        state[node] = BLACK

    while enter: 
        dfs(enter.pop())
    return list(order)