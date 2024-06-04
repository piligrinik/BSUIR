from .log_ops import LogOps


class Table:
    def __init__(self):
        self.log_ops: LogOps = LogOps()
        self.table: list[list[int]] = [
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]

    def get_s(self, index: int) -> list[int]:
        s: list[int] = []

        for i in range(index, len(self.table)):
            s.append(self.table[i][index])

        for i in range(index):
            s.append(self.table[i][index])

        return s

    def new_s(self, new_s: str, index: int) -> None:
        for i in range(index, len(self.table)):
            self.table[i][index] = int(new_s[i - index])

        len_new_s = len(new_s)

        for i in range(index):
            self.table[i][index] = int(new_s[(len(self.table) - index) + i])

    def get_column(self, index: int) -> list[int]:
        column: list[int] = []

        for i in range(index, len(self.table)):
            column.append(self.table[i][i - index])

        for i in range(index):
            column.append(self.table[i][len(self.table) - index + i])

        return column

    def new_column(self, new_address_column: str, index: int) -> None:
        for i in range(index, len(self.table)):
            self.table[i][i - index] = int(new_address_column[i - index])

        for i in range(index):
            self.table[i][len(self.table) - index + i] = int(new_address_column[len(self.table) - index + i])

    def log_op(self, index1: int, index2: int, index_new_s: int, log_op: str) -> None:
        s1, s2 = self.get_s(index1), self.get_s(index2)

        new_s: list[int] = []
        for i in range(len(self.table)):
            new_s.append(self.log_ops.return_value(log_op, s1[i], s2[i]))
        new_s_str: str = ''

        for number in new_s:
            new_s_str += str(number)
        self.new_s(new_s_str, index_new_s)

    def sort(self) -> None:
        buffer1: list[tuple] = []
        for i in range(len(self.table)):
            word: list[int] = self.get_s(i)
            word_str: str = ''

            for token in word:
                word_str += str(token)
            value: int = self.convert_to_decimal(word_str)
            buffer1.append((value, word_str))

        buffer1.sort(key=lambda a: a[0])

        for i in range(len(buffer1)):
            self.new_s(buffer1[i][1], i)

    def s_sum(self, v: str) -> None:
        ses_with_v: list[tuple] = []

        for i in range(len(self.table)):
            s: list[int] = self.get_s(i)
            s_str = ''

            for token in s:
                s_str += str(token)

            if s_str[:len(v)] == v:
                ses_with_v.append((s_str, i))

        for i in range(len(ses_with_v)):
            s_with_v, index = ses_with_v[i]

            a, b = (s_with_v[len(v):len(v) + 4],
                    s_with_v[len(v) + 4:len(v) + 8])
            s: str = self.reconvert(self.convert_to_decimal(a) + self.convert_to_decimal(b))

            new_s: str = v + a + b + s
            self.new_s(new_s, index)

    def print(self) -> None:
        for i in range(len(self.table)):
            out: str = ''
            for j in range(len(self.table[i])):
                out += str(self.table[i][j]) + '  '
            print(out)

    @staticmethod
    def convert_to_decimal(binary_number: str) -> int:
        value: int = 0

        for i in range(len(binary_number) - 1, -1, -1):
            value += int(binary_number[i]) * pow(2, len(binary_number) - 1 - i)

        return value

    @staticmethod
    def reconvert(number: int) -> str:
        binary_number: str = ''

        while number > 0:
            binary_number = str(number % 2) + binary_number
            number //= 2

        while len(binary_number) != 5:
            binary_number = '0' + binary_number
        return binary_number

