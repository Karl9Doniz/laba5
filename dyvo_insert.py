def dyvo_insert(sentence, flag):
    """
    Inserting word "диво" before every word that starts with flag.
    """
    result = ""
    for i in sentence.split(" "):
        if i[0:2] == flag:
            result += "диво " + i + " "
        else:
            result += i + " "
    return result.strip()
