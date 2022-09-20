""" Perform Unit Testing to test the recursive version of Floyd_warshall
Algorithm """

# Import testing package
import unittest

# Import the recursive function from the functions folder
from functions.floyd_warshall_recursive import floyd_warshall_rec
# Import sample test data from sample_data file
from tests.sample_data import (sample_1, result_1,)


# Unit Tests
class TestFloydWarshall(unittest.TestCase):
    """Test Class for the Floyd_warshall recursive algorithm"""

    def test_floyd_warshall_rec(self):
        """This test case checks that the actual output returned is equal to the expected
        output of graph1_node_input defined in the test data file"""

        self.assertEqual(floyd_warshall_rec(sample_1), result_1,
                         "Test Failed. Actual output does not match expected output")



if __name__ == '__main__':
    # Run the testing script
    unittest.main()