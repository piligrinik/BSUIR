from scr.table.table import Table


if __name__ == '__main__':
    table: Table = Table()
    while True:
        print('Введите номер операции, которую хотите совершить:')
        print('1 - вывод таблицы')
        print('2 - вывод слова по индексу')
        print('3 - изменение слова по индексу')
        print('4 - вывод столбца по индексу')
        print('5 - изменение столбца по индексу')
        print('6 - выполнение логических операций над двумя словами и запись в третье')
        print('7 - сортировка таблицы')
        print('8 - арифметические операции над полями слов')
        print('0 - выход')
        operation_key: str = input()
        match operation_key:
            case '1':
                table.print()
            case '2':
                print('Введите индекс слова, которое хотите получить:')
                index: int = int(input())
                word: str = ''

                for token in table.get_word_by_index(index):
                    word += str(token)
                print(f'Cлово с индексом {index}: {word}')
            case '3':
                print('Введите индекс старого слова и новое слово:')
                index: int = int(input())
                new_word: str = input()
                table.new_word_by_index(new_word, index)
                print('Операция завершена успешно')
            case '4':
                print('Введите индекс столбца, который хотите получить:')
                index: int = int(input())
                address_column: str = ''

                for token in table.get_column_by_index(index):
                    address_column += str(token)
                print(f'Столбец с индексом {index}: {address_column}')
            case '5':
                print('Введите индекс старого столбца и новый столбец:')
                index: int = int(input())
                new_address_column: str = input()
                table.new_column_by_index(new_address_column, index)
                print('Операция завершена успешно')
            case '6':
                print('Введите индексы двух слов, над которыми будут совершены операции, индекс слова, '
                      'в который будет записан результат, и номер логичсекой операции:')
                index1: int = int(input())
                index2: int = int(input())
                index3: int = int(input())
                function: str = input()
                table.log_op(index1, index2, index3, function)
                print('Операция завершена успешно')
            case '7':
                table.sort()
                print('Операция завершена успешно')
            case '8':
                print('Введите ключ V(3 бита), согласно которому будут изменены слова,'
                      ' у которых первые 3 бита совпадают с ключом:')
                key: str = input()
                table.word_sum(key)
                print('Операция завершена успешно')
            case '0':
                exit(0)
            case _:
                print('Введен неправильный номер операции, попробуйте еще раз')

