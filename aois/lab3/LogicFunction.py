from sources import execute
import numpy as np


class LogicFunction:

    def __init__(self, function: str):
        self._function = function

    def find_sub_formulas(self):
        sub_formulas = []
        new_sub_formula: list = []
        for i in range(len(self._function)):
            new_sub_formula.clear()
            buffer = 0
            if self._function[i] == ')':
                for j in self._function[i::-1]:
                    if j != '(' and j != ')':
                        new_sub_formula.append(j)
                    elif j == ')':
                        buffer += 1
                        new_sub_formula.append(j)
                    elif j == '(':
                        if buffer > 1:
                            buffer -= 1
                            new_sub_formula.append(j)
                        elif buffer <= 1:
                            new_sub_formula.append(j)
                            break
                new_sub_formula.reverse()
                str_sub_formula = ''.join(new_sub_formula)
                sub_formulas.append(str_sub_formula)
        return sub_formulas

    def find_variables(self):
        variables = []
        for token in self._function:
            if token.isalpha():
                if token not in variables:
                    variables.append(token)
        return variables

    def _truth_table(self, num_args):
        arguments = [False, True]
        table = []

        def generate_combinations(index, current):
            if index == num_args:
                table.append(tuple(current))
                return
            for arg in arguments:
                current[index] = arg
                generate_combinations(index + 1, current)

        generate_combinations(0, [None] * num_args)
        return table

    def _solve(self):
        values = {}
        result = []
        variables = self.find_variables()
        sub_formulas = self.find_sub_formulas()
        result_table: list[list] = []
        var_table = self._truth_table(len(variables))
        for k in range(len(sub_formulas)):
            result.clear()
            for i in range(len(var_table)):
                values.clear()

                for j in range(len(variables)):
                    values[variables[j]] = var_table[i][j]
                result.append(execute(sub_formulas[k], values))
            result_table.append(result.copy())
        transposed_matrix = [list(row) for row in zip(*result_table)]
        return transposed_matrix

    def result(self):
        variables = self.find_variables()
        table1 = self._truth_table(len(variables))
        line = []
        for i in range(len(table1)):
            line.clear()
            for j in table1[i]:
                out = int(j)
                line.append(out)
            table1[i] = line.copy()

        results = self._solve()
        for i in range(len(results)):
            line.clear()
            for j in results[i]:
                out = int(j)
                line.append(out)
            results[i] = line.copy()

        for j in range(len(results)):
            for k in range(len(results[j])):
                table1[j].append(results[j][k])
        return table1

    def make_vars_table(self):
        variables = self.find_variables()
        table = self.result()
        transposed_table = [list(row) for row in zip(*table)]
        return transposed_table[:len(variables)][:]

    def make_final_result_column(self):
        table = self.result()
        transposed_table = [list(row) for row in zip(*table)]
        return transposed_table[-1][:]

    def make_truth_dict(self, table_vars, result):
        truth_dict = {}
        transposed_table_vars = [list(row) for row in zip(*table_vars)]
        for index, row in enumerate(transposed_table_vars):
            truth_dict[''.join(str(x) for x in row)] = str(result[index])
        return truth_dict

