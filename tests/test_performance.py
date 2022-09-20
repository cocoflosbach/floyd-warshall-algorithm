"""Get and compare runtime performance between the recursive
and imperative versions of the Floyd_Warshall algorithm"""

# Import built-in packages
import sys
import timeit

# Import the recursive function from the functions folder
from functions.floyd_warshall_recursive import floyd_warshall_rec
# Import the imperative function from the functions folder
from functions.floyd_warshall_imperative import floyd_warshall_imp


def compare_performance():
    """Function to calculate the runtime for both verions of the algorithm"""

    INF = 99999
    graph = [[
        [0, 3, INF, 7],
        [8, 0, 2, INF],
        [5, INF, 0, 1],
        [2, INF, INF, 0]
        ]]

    # Calculate time execution time for the recursive version
    recursive_time = timeit.timeit(floyd_warshall_rec(graph), number= 4000)

    # Calculate time execution time for the recursive version
    imperative_time = timeit.timeit(floyd_warshall_imp(graph), number= 4000)

    return recursive_time, imperative_time


if __name__ == '__main__':
    recursive_time, imperative_time = compare_performance()
    # Print the comparison of both recursive and imperative execution times
    print("Recursive execution time: " + recursive_time)
    print("Imperative execution time: " + imperative_time)