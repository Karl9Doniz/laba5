import sys

Zero = ["  ***  ",
        " *   * ",
        "*     *",
        "*     *",
        "*     *",
        " *   * ",
        "  ***  "]
One = [" * ", "** ", " * ", " * ", " * ", " * ", "***"]
Two = [" *** ", "*   *", "*  * ", "  *  ", " *   ", "*    ", "*****"]
Three = [" *** ", "*   *", "    *", "  ** ", "    *", "*   *", " *** "]
Four = ["   *  ", "  **  ", " * *  ", "*  *  ", "******", "   *  ", "   *  "]
Five = ["*****", "*    ", "*    ", " *** ", "    *", "*   *", " *** "]
Six = [" *** ", "*    ", "*    ", "**** ", "*   *", "*   *", " *** "]
Seven = ["*****", "    *", "   * ", "  *  ", " *   ", "*    ", "*    "]
Eight = [" *** ", "*   *", "*   *", " *** ", "*   *", "*   *", " *** "]
Nine = [" ****", "*   *", "*   *", " ****", "    *", "    *", "    *"]
Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]

def return_digits(number):
    """
    Prints number pattern formed from digits
    >>> return_digits(1)
    ' 1 \\n11 \\n 1 \\n 1 \\n 1 \\n 1 \\n111'
    """

    digits_new = str(number)
    row = 0
    text = ""
    while row < 7:
        line = ""
        column = 0
        while column < len(digits_new):
            number = int(digits_new[column])
            digit = Digits[number]
            line += digit[row].replace('*', str(number))
            column += 1
        row += 1
        if row == 7:
            text += line
        else:
            text += line + "\n"
    return text

try:
    digits = sys.argv[1]
    print(return_digits(digits))
except IndexError:
    print("usage: bigdigits.py <number>")
except ValueError as err:
    print(err, "in", digits)

