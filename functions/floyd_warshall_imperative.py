"""This is an imperative version
of the floyd_Warshall shortest paths algorithm."""

import itertools

def floyd_warshall_imp(graph):
    """A simple implementation of Floyd's algorithm"""

    #Define number of nodes in the given graph
    node_number = len(graph)
    assert all(len(row) == node_number for row in graph)

    # Define dist as the output graph with the updated shortest path
    # between all nodes within the given graph

    dist = [row[:] for row in graph]

    for k in range(node_number):
        # select the start_nodes for each iteration
        for i in range(node_number):
            # select the end_nodes for each iteration
            for j in range(node_number):

                #Assume that if start_node and end_node are the same
                #then the distance would be zero
                if i == j:
                    dist[i][j] = 0
                    continue
                #return all possible paths and find the minimum
                #Update min value as the current shortest path
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


    return dist