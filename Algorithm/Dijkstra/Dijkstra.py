graph = {"start": {"a": 6, "b": 2}, "a": {"end": 1}, "b": {"a": 3, "end": 5}, "end": {}}

infinity = float("inf")
costs = {"a": 6, "b": 2, "end": infinity}

parents = {"a": "start", "b": "start", "end": None}

processed = []


def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs.keys():
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowest_cost_node(costs)

while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

print(parents)
