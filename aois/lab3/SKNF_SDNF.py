
from sources import find_vars
from sources import get_index
from sources import generate_gray_code
from sources import count_entries


class SKNF_SDNF:
    def __init__(self):
        pass

    @classmethod
    def normal_sknf(cls, variables: list[str], values: list[list], result: list):
        transposed_values = [list(row) for row in zip(*values)]
        sknf: str = ''
        sknf_old = ''
        for i in range(len(result)):
            elements = ''
            if result[i] == 0:
                for j in range(len(transposed_values[i])):
                    if transposed_values[i][j] == 0:
                        if j == 0:
                            elements += '(' + variables[j] + ' | '
                        elif variables[j] == variables[-1]:
                            elements += variables[j] + ') & '
                        else:
                            elements += variables[j] + ' | '
                    elif transposed_values[i][j] == 1:
                        if j == 0:
                            if len(variables) != 2:
                                elements += '(!' + variables[j] + ' | '
                            else:
                                elements += '(!' + variables[j] + ' | '
                        elif variables[j] == variables[-1]:
                            elements += '!' + variables[j] + ') & '
                        else:
                            elements += '!' + variables[j] + ' | '
            sknf_old += elements
            sknf = sknf_old[:-2]
        return sknf

    @classmethod
    def normal_sdnf(cls, variables: list[str], values: list[list], result: list):
        transposed_values = [list(row) for row in zip(*values)]
        sdnf: str = ''
        sdnf_old = ''
        for i in range(len(result)):
            elements = ''
            if result[i] == 1:
                for j in range(len(transposed_values[i])):
                    if transposed_values[i][j] == 1:
                        if j == 0:
                            elements += '(' + variables[j] + ' & '
                        elif variables[j] == variables[-1]:
                            elements += variables[j] + ') | '
                        else:
                            elements += variables[j] + ' & '
                    elif transposed_values[i][j] == 0:
                        if j == 0:
                            elements += '(!' + variables[j] + ' & '
                        elif variables[j] == variables[-1]:
                            elements += '!' + variables[j] + ') | '
                        else:
                            elements += '!' + variables[j] + ' & '
            sdnf_old += elements
            sdnf = sdnf_old[:-2]
        return sdnf

    @classmethod
    def find_odd_brackets(cls, transformed_list, brackets_size):
        odd_index = -1
        for i in range(brackets_size):
            if i not in transformed_list:
                odd_index = i
        return odd_index

    @classmethod
    def minimize_sknf(cls, variables: list[str], values: list[list], result: list):
        sknf = cls.normal_sknf(variables, values, result)
        sknf_clear = sknf.replace(' ', '').replace('|', '')
        sknf_list = sknf_clear.split('&')
        old_sknf = sknf_list.copy()
        sknf_list = cls.gluing(sknf_list)
        table, dead_end_sknf = cls._dead_end(old_sknf, sknf_list)
        sknf_str = cls.customize_min_sknf(dead_end_sknf)
        return sknf_str, table

    @classmethod
    def minimize_sdnf(cls, variables: list[str], values: list[list], result: list):
        sdnf = cls.normal_sdnf(variables, values, result)
        sdnf_clear = sdnf.replace(' ', '').replace('&', '')
        sdnf_list = sdnf_clear.split('|')
        old_sdnf = sdnf_list.copy()
        sdnf_list = cls.gluing(sdnf_list)
        table, dead_end_sdnf = cls._dead_end(old_sdnf, sdnf_list)
        sdnf_str = cls.customize_min_sdnf(dead_end_sdnf)
        return sdnf_str, table

    @classmethod
    def customize_min_sknf(cls, min_sknf: list):
        min_sknf_str = ''
        index_c = 0
        for item in min_sknf:
            min_sknf_str += item + '&'
        variables = find_vars(min_sknf_str)
        for index, token in enumerate(min_sknf_str):
            if token in variables and min_sknf_str[index_c + 1] != ')':
                min_sknf_str = min_sknf_str[:index_c + 1] + '|' + min_sknf_str[index_c + 1:]
                index_c += 1
            index_c += 1
        min_sknf_str = min_sknf_str[:-1]
        return min_sknf_str

    @classmethod
    def customize_min_sdnf(cls, min_sdnf: list):
        min_sdnf_str = ''
        index_c = 0
        for item in min_sdnf:
            min_sdnf_str += item + '|'
        variables = find_vars(min_sdnf_str)
        for index, token in enumerate(min_sdnf_str):
            if token in variables and min_sdnf_str[index_c + 1] != ')':
                min_sdnf_str = min_sdnf_str[:index_c + 1] + '&' + min_sdnf_str[index_c + 1:]
                index_c += 1
            index_c += 1
        min_sdnf_str = min_sdnf_str[:-1]
        return min_sdnf_str

    @classmethod
    def _dead_end(cls, snf: list, min_snf: list):
        new_min_sknf = []
        constituents = cls.make_table(snf, min_snf)
        entry = count_entries(constituents)
        table = cls.customize_table(snf, min_snf)
        transposed_constituents = [list(row) for row in zip(*constituents)]
        uses = []
        for k in range(len(transposed_constituents)):
            count = 0
            uses.clear()
            for g in range(len(transposed_constituents[k])):
                if transposed_constituents[k][g] == '   ✦    ':
                    count += 1
                    uses.append(g)
            if count == 1:
                if min_snf[uses[0]] not in new_min_sknf:
                    new_min_sknf.append(min_snf[uses[0]])
            if count >= 2:
                flag = True
                for use in uses:
                    if min_snf[use] in new_min_sknf:
                        flag = False
                if flag:
                    if not all(entry[uses[0]] == entry[use] for use in uses):
                        max_entry = uses[0]
                        for use in uses:
                            if entry[max_entry] < entry[use]:
                                max_entry = use
                        new_min_sknf.append(min_snf[max_entry])
                    else:
                        temporary_snf = []
                        for use in uses:
                            temporary_snf.append(len(find_vars(min_snf[use])))
                        if not all(len(find_vars(min_snf[use2])) == len(find_vars(min_snf[0])) for use2 in uses):
                            min_use = uses[temporary_snf.index(min(temporary_snf))]
                            new_min_sknf.append(min_snf[min_use])
        return table, new_min_sknf

    @classmethod
    def table_calc_sknf(cls, sknf):
        sknf_list = cls.split_sknf(sknf)
        min_sknf = cls.gluing(sknf_list)
        table, result_list = cls._dead_end(sknf_list, min_sknf)
        result = cls.customize_min_sknf(result_list)
        return result

    @classmethod
    def table_calc_sdnf(cls, sdnf):
        sdnf_list = cls.split_sdnf(sdnf)
        min_sdnf = cls.gluing(sdnf_list)
        table, result_list = cls._dead_end(sdnf_list, min_sdnf)
        result = cls.customize_min_sdnf(result_list)
        return result

    @classmethod
    def make_table(cls, snf: list, min_snf: list):
        constituents: list[list[str]] = [['        '] * len(snf) for i in range(len(min_snf))]
        for index1, term1 in enumerate(min_snf):
            for index2, term2 in enumerate(snf):
                flag = True
                for i in range(len(term1)):
                    for j in range(len(term2)):
                        if term1[i] == term2[j] and term1[i].isalpha():
                            if term1[i - 1] != term2[j - 1]:
                                if term1[i - 1] == '!' or term2[j - 1] == '!':
                                    flag = False
                if flag:
                    constituents[index1][index2] = '   ✦    '
        return constituents

    @classmethod
    def customize_table(cls, old_snf: list[str], min_snf: list[str]):
        max_len = 0
        for term in min_snf:
            if max_len < len(term):
                max_len = len(term)
        table_constituents = cls.make_table(old_snf, min_snf)
        for i in range(len(table_constituents)):
            table_constituents[i].insert(0, min_snf[i] + (' ' * (max_len - len(min_snf[i]))))
        table_constituents.insert(0, old_snf)
        # table_constituents[0].insert(0, '        ')
        return table_constituents

    @classmethod
    def gluing(cls, snf_list):
        minimize_list = []
        transformed_brackets = []
        while True:
            minimize_list.clear()
            transformed_brackets.clear()
            for index1, term1 in enumerate(snf_list):
                for index2, term2 in enumerate(snf_list):
                    if find_vars(term1) == find_vars(term2) and term1 != term2:
                        buffer = 0
                        index = 0
                        for i in range(len(term1)):
                            for j in range(len(term2)):
                                if term1[i] == term2[j] and term1[i].isalpha():
                                    if term1[i - 1] != term2[j - 1]:
                                        buffer += 1
                                        index = i
                        if buffer == 1:
                            if term1[index - 1] == '!':
                                new_term1 = term1[:index - 1] + term1[index + 1:]
                            else:
                                new_term1 = term1.replace(term1[index], '')
                            if index1 not in transformed_brackets and index2 not in transformed_brackets:
                                transformed_brackets.append(index2)
                                transformed_brackets.append(index1)
                            if new_term1 not in minimize_list:
                                minimize_list.append(new_term1)
            if not minimize_list:
                break
            else:
                for i in range(len(snf_list)):
                    if i not in transformed_brackets:
                        minimize_list.append(snf_list[i])
                snf_list = minimize_list.copy()
        return snf_list

    @classmethod
    def split_sknf(cls, sknf: str):
        sknf_clear = sknf.replace(' ', '').replace('|', '')
        sknf_list = sknf_clear.split('&')
        return sknf_list

    @classmethod
    def split_sdnf(cls, sdnf: str):
        sdnf_clear = sdnf.replace(' ', '').replace('&', '')
        sdnf_list = sdnf_clear.split('|')
        return sdnf_list

    @classmethod
    def make_kmap(cls, variables, truth_dict):
        num_vars = len(variables)
        gray_codes = generate_gray_code(num_vars)
        rows = 2 ** (num_vars // 2)
        cols = 2 ** ((num_vars + 1) // 2)
        kmap = [['-' for _ in range(cols)] for _ in range(rows)]

        for gray_code, value in truth_dict.items():
            row = get_index(gray_code[:num_vars // 2])
            col = get_index(gray_code[num_vars // 2:])
            kmap[row][col] = value
        for i, row in enumerate(kmap):
            kmap[i].insert(0, gray_codes[i])
        kmap.insert(0, gray_codes[:cols])
        kmap[0].insert(0, '       ')
        return kmap

    @classmethod
    def table_method_result(cls, snf, k):
        if k == 0:
            result = cls.table_calc_sknf(snf)
        elif k == 1:
            result = cls.table_calc_sdnf(snf)
        else:
            return ''
        return result

