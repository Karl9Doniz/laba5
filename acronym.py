import doctest
print(doctest.testmod())

def acronym(line):
    """
    Makes an acronym from a single sentence
    >>> acronym("As soon As possible")
    'ASAP'
    """
    result = ""
    result += line[0]
    for i in range(len(line)):
        if line[i] == " ":
            result += line[i + 1]
    return result.upper()

def create_acronym(message):
    """
    Function recieves a string with sentences separsted
    by a new line character and transforms each into an acronym.
    >>> create_acronym("random access memory")
    'RAM - random access memory'
    """
    sentences = message.split("\n")
    line = ""
    for i in sentences:
        line += acronym(i) +  " - " + i + "\n"
    return line.strip()
