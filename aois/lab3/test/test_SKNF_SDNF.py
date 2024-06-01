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
        exp_sknf = '(a | b | !c) & (a | !b | !c) & (!a | b | c) & (!a | !b | !c) '
        self.assertEqual(sknf, exp_sknf)

    def test_normal_sdnf(self):
        variables = self.foo.find_variables()
        table_vars = self.foo.make_vars_table()
        result = self.foo.make_final_result_column()
        sdnf = SKNF_SDNF.normal_sdnf(variables, table_vars, result)
        exp_sdnf = '(!a & !b & !c) | (!a & b & !c) | (a & !b & c) | (a & b & !c) '
        self.assertEqual(sdnf, exp_sdnf)

    def test_gluing(self):
        variables = self.foo.find_variables()
        table_vars = self.foo.make_vars_table()
        result = self.foo.make_final_result_column()
        sknf = SKNF_SDNF.normal_sknf(variables, table_vars, result)
        sknf_list = SKNF_SDNF.split_sknf(sknf)
        glued_sknf = SKNF_SDNF.gluing(sknf_list)
        exp_sknf = ['(a!c)', '(!b!c)', '(!abc)', '(!a!b!c)']
        self.assertEqual(glued_sknf, exp_sknf)

    def test_min_sknf(self):
        variables = self.foo.find_variables()
        table_vars = self.foo.make_vars_table()
        result = self.foo.make_final_result_column()
        min_sknf, table = SKNF_SDNF.minimize_sknf(variables, table_vars, result)
        exp_min_sknf = '(a|!c)&(!a|b|c)&(!b|!c)'
        self.assertEqual(min_sknf, exp_min_sknf)

    def test_table_clac_method(self):
        variables = self.foo.find_variables()
        table_vars = self.foo.make_vars_table()
        result = self.foo.make_final_result_column()
        sknf = SKNF_SDNF.normal_sknf(variables, table_vars, result)
        min_sknf = SKNF_SDNF.table_calc_sknf(sknf)
        exp_min_sknf = '(a|!c)&(!a|b|c)&(!b|!c)'
        self.assertEqual(min_sknf, exp_min_sknf)

    def test_karnaugh_map_method(self):
        variables = self.foo.find_variables()
        table_vars = self.foo.make_vars_table()
        result = self.foo.make_final_result_column()
        sknf = SKNF_SDNF.normal_sknf(variables, table_vars, result)
        min_sknf = SKNF_SDNF.table_method_result(sknf, 0)
        exp_min_sknf = '(a|!c)&(!a|b|c)&(!b|!c)'
        self.assertEqual(min_sknf, exp_min_sknf)

    def test_split_sknf(self):
        variables = self.foo.find_variables()
        table_vars = self.foo.make_vars_table()
        result = self.foo.make_final_result_column()
        sknf = SKNF_SDNF.normal_sknf(variables, table_vars, result)
        exp_sknf_list = ['(ab!c)', '(a!b!c)', '(!abc)', '(!a!b!c)']
        sknf_list = SKNF_SDNF.split_sknf(sknf)
        self.assertEqual(sknf_list, exp_sknf_list)

    def test_truth_dict(self):
        table_vars = self.foo.make_vars_table()
        result = self.foo.make_final_result_column()
        result_dictionary = self.foo.make_truth_dict(table_vars, result)
        first_dict_el = result_dictionary['000']
        first_res_el = str(result[0])
        self.assertEqual(first_dict_el, first_res_el)

    def test_karnaugh_map(self):
        table_vars = self.foo.make_vars_table()
        result = self.foo.make_final_result_column()
        result_dictionary = self.foo.make_truth_dict(table_vars, result)
        variables = self.foo.find_variables()
        kmap = SKNF_SDNF.make_kmap(variables, result_dictionary)
        f_row = kmap[1][1:]
        exp_row = ['1', '0', '0', '1']
        self.assertEqual(f_row, exp_row)

if __name__ == '__main__':
    unittest.main()
