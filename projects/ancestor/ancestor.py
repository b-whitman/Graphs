
def earliest_ancestor(ancestors, starting_node):
    # node = starting_node
    # Find the parents of node
    # If node has no parents, return -1
    # while len(parents) > 0,
    ## new_parents = parents of parents
    ## if len(new_parents) == 1 and new_parents has no parents,
    ### return new_parents[0]
    ## elif len(new_parents) > 1
    ### parents = new_parents
    ## elif len(new_parents) == 0
    ### return min value in new_parents
    # Once while loop exits,
    # return min value in new_parents