import unittest
from LogicFunction import LogicFunction


class TestLogicFunction(unittest.TestCase):
    def setUp(self):
        self.formula = formula = "((a > b) ~ (! c))"
        self.foo = LogicFunction(formula)

    def test_sub_formulas(self):
        expected_first_f = '(a > b)'
        sub_formulas = self.foo.find_sub_formulas()
        assert expected_first_f == sub_formulas[0]

    def test_result(self):
        table = self.foo.result()
        transposed_table = [list(row) for row in zip(*table)]
        result_column = [0, 1, 1, 0, 0, 1, 0, 1]
        assert result_column == transposed_table[-1][:]

    def test_find_vars(self):
        variables = self.foo.find_variables()
        exp_variables = ['a', 'b', 'c']
        assert variables == exp_variables

    def test_vars_table(self):
        table = self.foo.make_vars_table()
        exp_column = [1, 1, 1, 1, 0, 0, 0, 0]
        assert exp_column == table[0]

if __name__ == '__main__':
    unittest.main()
