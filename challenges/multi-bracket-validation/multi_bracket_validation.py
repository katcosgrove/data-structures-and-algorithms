def multi_bracket_validation(input):
    """Determine whether string input has balanced brackets."""
    if type(input) is not str:
        raise ValueError('Please input a string.')

    if len(input) == 0:
        raise IndexError('Please enter a string with a length.')

    paren = 0
    curly = 0
    square = 0

    for letter in input:
        if letter is '(':
            paren += 1
        elif letter is ')':
            paren -= 1
        elif letter is '[':
            square += 1
        elif letter is ']':
            square -= 1
        elif letter is '{':
            curly += 1
        elif letter is '}':
            curly -= 1
        else:
            break

    if paren or curly or square is not 0:
        return False
    else:
        return True
