import doctest
print(doctest.testmod())

def caesar_encode(message, key):
    """
    Recieves a message and a key and returns encoded
    message with a shift value of 'key'.
    >>> caesar_encode("computer", 3)
    'frpsxwhu'
    """
    encoded_message = ""
    for i in message:
        if i == " ":
            encoded_message += i
        else:
            encoded_message += chr((ord(i) - 97 + key) % 26 + 97)
    return encoded_message

def caesar_decode(message, key):
    """
    Recieves a message and a key and returns decoded
    message with a shift value of 'key'.
    >>> caesar_decode("frpsxwhu", 3)
    'computer'
    """
    encoded_message = ""
    for i in message:
        if i == " ":
            encoded_message += i
        else:
            encoded_message += chr((ord(i) - 97 - key) % 26 + 97)
    return encoded_message

print(caesar_decode("oddzwsr gqwsbqs", 40))

