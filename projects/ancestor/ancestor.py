
def earliest_ancestor(ancestors, starting_node):
    # node = starting_node
    node = starting_node
    # Find the parents of node
    parents = get_parents(ancestors, node)
    # If node has no parents, return -1
    if len(parents) == 0:
        return -1
    # while len(parents) > 0,
    ## new_parents = parents of parents
    while len(parents) > 0:
        new_parents = []
        for node in parents:
            new_parents.append(get_parents(ancestors, node)) 
        new_parents_flat = []
        for sublist in new_parents:
            for parent in sublist:
                new_parents_flat.append(parent)
        new_parents = new_parents_flat
        if len(new_parents) == 1 and len(get_parents(ancestors, new_parents[0])) == 0:
            return new_parents[0]
        elif len(new_parents) > 1:
            parents = new_parents
        elif len(new_parents) == 0:
            return min(parents)
    return min(parents)


def get_parents(ancestors, node):
    # Iterate over ancestors and return list of nodes that appear as ancestors 
    # of given node
    parents = []
    for edge in ancestors:
        if edge[1] == node:
            parents.append(edge[0])
    print(parents)
    return parents
