import unittest
from back_propagation import *


class TestBackPropagation(unittest.TestCase):
    def test_forward(self):
        # Identify function
        inputs = [1]
        functions = [[lambda x: x, [0]]]
        output = forward(inputs, functions)
        self.assertEqual(output, 1)

        # 1 + 2 * 3
        inputs = [1, 2, 3]
        functions = [[lambda x, y: x * y, [1, 2]], [lambda x, y: x + y, [0, 3]]]
        output = forward(inputs, functions)
        self.assertEqual(output, 7)

        # W @ x + b
        W = np.random.rand(10, 5)
        x = np.random.rand(5, 1)
        b = np.random.rand(10, 1)
        inputs = [W, x, b]
        functions = [[lambda x, y: x @ y, [0, 1]], [lambda x, y: x + y, [3, 2]]]
        output = forward(inputs, functions)
        np.testing.assert_almost_equal(output, inputs[0] @ inputs[1] + inputs[2])