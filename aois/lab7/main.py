from scr.table.table import Table


if __name__ == '__main__':
    table: Table = Table()
    table.print()
    print('Enter the index of the word(S):')
    index: int = int(input())
    word: str = ''
    for token in table.get_s(index):
        word += str(token)
    print(f'Word(S) with index {index}: {word}')
    print('Enter the index of the old word and the new word:')
    index: int = int(input())
    new_word: str = input()
    table.new_s(new_word, index)
    print('Succeed')
    table.print()
    print('Enter the index of the column:')
    index: int = int(input())
    column: str = ''
    for token in table.get_column(index):
        column += str(token)
    print(f'Column with index{index}: {column}')
    print('Enter the index of the old column and the new column:')
    index: int = int(input())
    new_column: str = input()
    table.new_column(new_column, index)
    print('Succeed')
    table.print()
    print("Enter two words' indexes for logical function, index of the word where the result will be stored, "
          "and the number of logical function(4, 6, 9, 11):")
    index1: int = int(input())
    index2: int = int(input())
    index3: int = int(input())
    function: str = input()
    table.log_op(index1, index2, index3, function)
    print('Succeed')
    table.print()
    table.sort()
    print('Succeed')
    table.print()
    print('Enter V key(3 bits), by which the words'
          'that have the same first three bits will be changed,')
    key: str = input()
    table.s_sum(key)
    print('Succeed')
    table.print()

