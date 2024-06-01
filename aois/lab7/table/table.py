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

    def get_word_by_index(self, index: int) -> list[int]:
        word: list[int] = []

        for i in range(index, len(self.table)):
            word.append(self.table[i][index])

        for i in range(index):
            word.append(self.table[i][index])

        return word

    def new_word_by_index(self, new_word: str, index: int) -> None:
        for i in range(index, len(self.table)):
            self.table[i][index] = int(new_word[i - index])

        len_new_word = len(new_word)

        for i in range(index):
            self.table[i][index] = int(new_word[(len(self.table) - index) + i])

    def get_column_by_index(self, index: int) -> list[int]:
        word: list[int] = []

        for i in range(index, len(self.table)):
            word.append(self.table[i][i - index])

        for i in range(index):
            word.append(self.table[i][len(self.table) - index + i])

        return word

    def new_column_by_index(self, new_address_column: str, index: int) -> None:
        for i in range(index, len(self.table)):
            self.table[i][i - index] = int(new_address_column[i - index])

        for i in range(index):
            self.table[i][len(self.table) - index + i] = int(new_address_column[len(self.table) - index + i])

    def log_op(self, index1: int, index2: int, index_where_to_write: int, operation_string: str) -> None:
        word1, word2 = self.get_word_by_index(index1), self.get_word_by_index(index2)

        new_word: list[int] = []
        for i in range(len(self.table)):
            new_word.append(self.log_ops.return_value(operation_string, word1[i], word2[i]))
        new_word_str: str = ''

        for number in new_word:
            new_word_str += str(number)
        self.new_word_by_index(new_word_str, index_where_to_write)

    def sort(self) -> None:
        sort_helper_list: list[tuple] = []
        for i in range(len(self.table)):
            word: list[int] = self.get_word_by_index(i)
            word_str: str = ''

            for token in word:
                word_str += str(token)
            value: int = self.convert_to_decimal(word_str)
            sort_helper_list.append((value, word_str))

        sort_helper_list.sort(key=lambda a: a[0])

        for i in range(len(sort_helper_list)):
            self.new_word_by_index(sort_helper_list[i][1], i)

    def word_sum(self, key_string: str) -> None:
        words_to_update: list[tuple] = []

        for i in range(len(self.table)):
            word: list[int] = self.get_word_by_index(i)
            word_str: str = ''

            for token in word:
                word_str += str(token)

            if word_str[:len(key_string)] == key_string:
                words_to_update.append((word_str, i))

        for i in range(len(words_to_update)):
            word_to_update, index = words_to_update[i]

            a, b = (word_to_update[len(key_string):len(key_string) + 4],
                    word_to_update[len(key_string) + 4:len(key_string) + 8])
            s: str = self.reconvert(self.convert_to_decimal(a) + self.convert_to_decimal(b))

            new_word: str = key_string + a + b + s
            self.new_word_by_index(new_word, index)

    def print(self) -> None:
        for i in range(len(self.table)):
            print_string: str = ''
            for j in range(len(self.table[i])):
                print_string += str(self.table[i][j]) + '  '
            print(print_string)

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

