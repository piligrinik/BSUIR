from BinaryOperations import BinaryOperations


def precedence(op):
    if op == '!':
        return 4
    elif op == '&':
        return 3
    elif op == '|':
        return 2
    elif op == '>' or op == '~':
        return 1
    else:
        return 0


# Функция для преобразования логической формулы в обратную польскую запись
def infix_to_rpn(formula):
    output = []
    stack = []
    operators = {'&', '|', '!', '>', '~'}
    formula = formula.replace('(', ' ( ').replace(')', ' ) ').split()

    for token in formula:
        if token not in operators and token != '(' and token != ')':
            output.append(token)
        elif token == '':
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if len(stack) != 0: stack.pop()
        else:
            while stack and precedence(stack[-1]) >= precedence(token) and stack[-1] != '(':
                output.append(stack.pop())
            stack.append(token)

    while stack:
        output.append(stack.pop())

    return output


# Функция для вычисления логической формулы в обратной польской записи
def evaluate_rpn(rpn_list):
    stack = []
    operators = {'&', '|', '!', '>', '~'}

    for token in rpn_list:
        if token not in operators:
            stack.append(token)
        elif token == '!':
            a = stack.pop()
            stack.append(BinaryOperations.negation(a))
        elif token == '&':
            b = stack.pop()
            a = stack.pop()
            stack.append(BinaryOperations.conjunction(a, b))
        elif token == '|':
            b = stack.pop()
            a = stack.pop()
            stack.append(BinaryOperations.disjunction(a, b))
        elif token == '>':
            b = stack.pop()
            a = stack.pop()
            stack.append(BinaryOperations.implication(a, b))
        elif token == '~':
            b = stack.pop()
            a = stack.pop()
            stack.append(BinaryOperations.equivalence(a, b))

    return stack[0]


def execute(formula, values) -> bool: #выполнение
    rpn_formula = infix_to_rpn(formula)
    # Значения аргументов для подстановки
    # Преобразование переменных в значения
    for i in range(len(rpn_formula)):
        if rpn_formula[i] in values:
            rpn_formula[i] = values[rpn_formula[i]]
    # Вычисление результата с подстановкой значений
    result = evaluate_rpn(rpn_formula)
    return result