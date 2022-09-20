"""This is a recursive version
of the floyd_Warshall shortest paths algorithm."""


def floyd_warshall_rec(dist):
    """A recursive implementation of Floyd's algorithm"""

    # Define number of nodes in the given graph
    node_number = len(dist)

    #Define the infinite variable  which will be used for nodes not connected to each other
    INF = 9999

    # Define recursive formula for finding
    # the shortest path between two vertices

    #Initialise variables [i] as start_node, [j] as end_node  and [k] as intermediate_node
    def fw_recursive_func(i, j, k):

        #If start_node [i] is equal to end_node [j]
        #If intermediate [k] is less than 0
        if k < 0:
            return dist[i][j]

        #If start_node [i] and end_node [j] is greater than or equal to
        #INF, return INF
        elif [i][j] >= INF:
            return INF

        # If there is a new shorter route through k, replace current route
        else:
            return min(
                fw_recursive_func(i, j, k - 1),
                fw_recursive_func(i, k, k - 1) +
                fw_recursive_func(k, j, k - 1))

    # Find the shortest path and update graph
    for k in range(node_number):
        for i in range(node_number):
            for j in range(node_number):
                dist[i][j] = fw_recursive_func(i, j, k)

            # Return the updated shortest path matrix
    return dist

