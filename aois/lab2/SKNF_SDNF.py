class SKNF_SDNF:
    def __init__(self):
        pass

    @classmethod
    def normal_sknf(cls, variables: list[str], values: list[list], result: list):
        transposed_values = [list(row) for row in zip(*values)]
        elements: str = ''
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
        elements: str = ''
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
                            elements += '(' + variables[j] + ' & '
                        elif variables[j] == variables[-1]:
                            elements += '!' + variables[j] + ') | '
                        else:
                            elements += '!' + variables[j] + ' & '
            sdnf_old += elements
            sdnf = sdnf_old[:-2]
        return sdnf

    @classmethod
    def num_sknf(cls, variables: list[str], values: list[list], result: list):
        transposed_values = [list(row) for row in zip(*values)]
        elements: str = ''
        sknf_num = []
        for i in range(len(result)):
            elements = ''
            if result[i] == 0:
                sknf_num.append(i)
        return sknf_num

    @classmethod
    def num_sdnf(cls, variables: list[str], values: list[list], result: list):
        transposed_values = [list(row) for row in zip(*values)]
        elements: str = ''
        sdnf_num = []
        for i in range(len(result)):
            elements = ''
            if result[i] == 1:
                sdnf_num.append(i)
        return sdnf_num

    @classmethod
    def index_form(cls, binary):
        decimal_value = 0
        for i in range(len(binary)):
            decimal_value += binary[i] * 2 ** (len(binary) - i - 1)
        return decimal_value

