from LogicFunction import LogicFunction
from SKNF_SDNF import SKNF_SDNF


def attempt():
    formula = '((! (a ~ b)) | c)'
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
    sknf_list = SKNF_SDNF.split_sknf(sknf)
    glued_sknf = SKNF_SDNF.gluing(sknf_list)
    print('\n\nGluing phase for PCNF:')
    print(glued_sknf)
    min_sknf, table_constituents_sknf = SKNF_SDNF.minimize_sknf(variables, table_vars, result)
    print('\nMinimized PCNF (calculation method)')
    print(min_sknf)
    sdnf_list = SKNF_SDNF.split_sdnf(sdnf)
    glued_sdnf = SKNF_SDNF.gluing(sdnf_list)
    print('\n\nGluing phase for PDNF:')
    print(glued_sdnf)
    min_sdnf, table_constituents_sdnf = SKNF_SDNF.minimize_sdnf(variables, table_vars, result)
    print('\nMinimized PDNF (calculation method)')
    print(f"{min_sdnf}\n")

    print(''
          '')
    print('Calculation - table method:'
          ''
          '')
    print("PCNF:"
          "")
    for item in table_constituents_sknf:
        out = ''
        for i in item:
            out += i
            out += '|'
        print(out)
    print(f'\n Minimized PCNF (table-calculation method): {SKNF_SDNF.table_calc_sknf(sknf)}\n')
    print(""
          "PDNF:"
          "")
    for item in table_constituents_sdnf:
        out = ''
        for i in item:
            out += i
            out += '|'
        print(out)
    print(f'\n Minimized PDNF (table-calculation method): {SKNF_SDNF.table_calc_sdnf(sdnf)}\n')
    print('\n\n Karnaugh map and table method:')
    result_dictionary = attempt1.make_truth_dict(table_vars, result)
    kmap = SKNF_SDNF.make_kmap(variables, result_dictionary)
    for index, item in enumerate(kmap):
        out = ''
        for i in item:
            out += i
            out += ''
            if index > 0:
                out += '  |  '
            else:
                out += ' '
        print(out)
    print(f'\n Minimized PCNF: {SKNF_SDNF.table_method_result(sknf, 0)}')
    print(f'\n Minimized PDNF: {SKNF_SDNF.table_method_result(sdnf, 1)}')


if __name__ == "__main__":
    attempt()
