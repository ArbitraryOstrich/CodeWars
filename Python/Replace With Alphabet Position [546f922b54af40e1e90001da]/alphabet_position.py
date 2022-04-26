def alphabet_position(string):
    new_string = ""
    for a in (
        ord(character) - 64 for character in string.upper() if character.isalpha()
    ):
        new_string += " " + str(a)
    return new_string[1::]
    pass
