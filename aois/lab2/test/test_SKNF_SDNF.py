import unittest
from SKNF_SDNF import SKNF_SDNF
from LogicFunction import LogicFunction


class TestSKNF_SDNF(unittest.TestCase):
    def setUp(self):
        self.formula = formula = "((a > b) ~ (! c))"
        self.foo = LogicFunction(formula)

    def test_normal_sknf(self):
        variables = self.foo.find_variables()
        table_vars = self.foo.make_vars_table()
        result = self.foo.make_final_result_column()
        sknf = SKNF_SDNF.normal_sknf(variables, table_vars, result)
        exp_sknf = '(!a | !b | !c) & (!a | b | c) & (a | !b | !c) & (a | b | !c) '
        self.assertEqual(sknf, exp_sknf)

    def test_normal_sdnf(self):
        variables = self.foo.find_variables()
        table_vars = self.foo.make_vars_table()
        result = self.foo.make_final_result_column()
        sdnf = SKNF_SDNF.normal_sdnf(variables, table_vars, result)
        exp_sdnf = '(a & b & !c) | (a & !b & c) | (a & b & !c) | (a & !b & !c) '
        self.assertEqual(sdnf, exp_sdnf)

    def test_num_sknf(self):
        variables = self.foo.find_variables()
        table_vars = self.foo.make_vars_table()
        result = self.foo.make_final_result_column()
        num_sknf = SKNF_SDNF.num_sknf(variables, table_vars, result)
        exp_num_sknf = [0, 3, 4, 6]
        self.assertEqual(num_sknf, exp_num_sknf)

    def test_num_sknf(self):
        variables = self.foo.find_variables()
        table_vars = self.foo.make_vars_table()
        result = self.foo.make_final_result_column()
        num_sdnf = SKNF_SDNF.num_sdnf(variables, table_vars, result)
        exp_num_sdnf = [1, 2, 5, 7]
        self.assertEqual(num_sdnf, exp_num_sdnf)

    def test_index_form(self):
        result = self.foo.make_final_result_column()
        decimal = SKNF_SDNF.index_form(result)
        exp_decimal = 100
        self.assertNotEqual(decimal, exp_decimal)


if __name__ == '__main__':
    unittest.main()
