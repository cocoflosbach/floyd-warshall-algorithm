"""Initialise distance inputs and expected outputs for a give node"""

# A sample data set to test if expected output matches the given graph


# Define infinity as the large enough 
# value to signify nodes with no direct relationship
INF = 99999

# Test 1: Small data set
sample_1 = [[
        [0, 7, INF, 8],
        [INF, 0, 5, INF],
        [INF, INF, 0, 2],
        [INF, INF, INF, 0]
        ]]

result_1 = [[
        [0, 7, 12, 8],
        [INF, 0, 5, INF],
        [INF, INF, 0, 2],
        [INF, INF, INF, 0]
        ]]
sample_2 = [[
        [0, 3, INF, 7],
        [8, 0, 2, INF],
        [5, INF, 0, 1],
        [2, INF, INF, 0]
        ]]

result_2 = [[
        [0, 3, INF, 7],
        [8, 0, 2, 15],
        [5, 8, 0, 1],
        [2, 8, INF, 0]
        ]]
