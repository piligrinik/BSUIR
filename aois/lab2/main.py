from LogicFunction import LogicFunction
from SKNF_SDNF import SKNF_SDNF


def attempt():
    # formula = '(((! a) ~ (b | c)) | (d & e)) '
    # formula = '((a & b) > (c | d))'
    # formula = "(! (! (a > b)))"
    #
    formula = '(p | ((q | (r & s)) | (s | r)))'
    attempt1 = LogicFunction(formula)
    sub_f1 = attempt1.find_sub_formulas()
    variables = attempt1.find_variables()
    a = attempt1.result()
    variables_str = '  |  '.join(map(str, variables))
    sub_formulas = ' '.join(map(str, sub_f1))
    print(variables_str + ' | ' + sub_formulas)
    print('—' * len(variables_str + '  ' + sub_formulas))
    for item in a:
        out = ''
        for i in item:

            out += str(i)
            out += '  |  '
        print(out)
    table_vars = attempt1.make_vars_table()
    result = attempt1.make_final_result_column()
    sknf = SKNF_SDNF.normal_sknf(variables, table_vars, result)
    print("PCNF:")
    print(sknf)
    sdnf = SKNF_SDNF.normal_sdnf(variables, table_vars, result)
    print("PDNF:")
    print(sdnf)
    sknf_num = SKNF_SDNF.num_sknf(variables, table_vars, result)
    print("numeric form of PCNF:")
    print(sknf_num)
    sdnf_num = SKNF_SDNF.num_sdnf(variables, table_vars, result)
    print("numeric form of PDNF: ")
    print(sdnf_num)
    decimal = SKNF_SDNF.index_form(result)
    print("Index form: ")
    print(f"{decimal} - {result}")
    # for item in result:
    #     print(item)


if __name__ == "__main__":
    attempt()
