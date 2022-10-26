import doctest
import math

words_operators = {"додати": "+", "плюс": "+", "відняти":"-", "мінус":"-",
                                        "помножити":"*", "поділити":"/"}
val_set = set(words_operators.values())

def validity_check(expression):
    """
    (str) -> (bool)
    >>> calculate_expression("Скільки буде 3 в кубі?")
    'Неправильний вираз!'
    """
    count = 0
    for i in val_set:
        if i not in expression:
            count += 1
    if count == 4:
        return True

    num_count = 0
    for i in expression:
        if i.isnumeric() or '-' in i and len(i) > 1:
            num_count += 1
    if num_count == 0:
        return True

    num_operators = 0
    for i in expression:
        if i in val_set:
            num_operators += 1
    if num_operators == num_count:
        return True

    t = expression[len(expression) - 1]
    if t in val_set:
        return True

    return False

def calculate_expression(expression):
    """
    (str) -> (int)
    >>> calculate_expression("Скільки буде 8 відняти 3?")
    5
    >>> calculate_expression("Скільки буде 7 додати 3 помножити на 5?")
    50
    >>> calculate_expression("Скільки буде 10 поділити на -2 додати 11 мінус -3?")
    9
    >>> calculate_expression("Скільки буде 3 в кубі?")
    'Неправильний вираз!'
    """
    temp = expression.replace("?", '')
    temp = temp.replace("на", '')
    temp = " ".join(temp.split())
    words = temp.split(" ")
    new_expression = []

    for i in words:
        if i.isnumeric():
            new_expression.append(i)
        if '-' in i:
            new_expression.append(i)
        if i in words_operators.keys():
            new_expression.append(words_operators.get(i))

    if validity_check(new_expression):
        return 'Неправильний вираз!'
    line = ""
    result = 0
    for i in new_expression:
        line += i
        if i.isnumeric() or '-' in i and len(i) > 1:
            result = eval(line)
            line = str(result)
    return math.trunc(result)

print(doctest.testmod())