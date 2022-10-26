import doctest

def dyvo_insert(sentence, flag):
    """
    Inserting word "диво" before every word that starts with flag.
    >>> dyvo_insert("Кит кота по хвилях катав - кит у воді, кіт на киті", "ки")
    'дивокит кота по хвилях катав - дивокит у воді, кіт на дивокиті'
    """
    result = " "
    result += sentence.lower()
    s = result.replace(" " + flag, " " + "диво" + flag)
    return s.strip()

print(doctest.testmod())
