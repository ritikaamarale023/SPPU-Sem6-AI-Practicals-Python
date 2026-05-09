# A* Algorithm in Python

# Graph with cost values
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 6)],
    'C': [('F', 5)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

# Heuristic values
heuristic = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 3,
    'E': 1,
    'F': 0
}

# A* Algorithm Function
def astar(start, goal):

    open_list = [start]
    closed_list = []

    g = {}
    g[start] = 0

    parents = {}
    parents[start] = start

    while open_list:

        # Find node with minimum f(n)
        current = open_list[0]

        for node in open_list:
            if g[node] + heuristic[node] < g[current] + heuristic[current]:
                current = node

        # Goal node found
        if current == goal:
            path = []

            while parents[current] != current:
                path.append(current)
                current = parents[current]

            path.append(start)
            path.reverse()

            print("Shortest Path Found:")
            print(" -> ".join(path))
            return

        # Check neighbors
        for neighbor, cost in graph[current]:

            if neighbor not in open_list and neighbor not in closed_list:
                open_list.append(neighbor)

                parents[neighbor] = current
                g[neighbor] = g[current] + cost

        open_list.remove(current)
        closed_list.append(current)

    print("Path does not exist!")

# Main Program
astar('A', 'F')