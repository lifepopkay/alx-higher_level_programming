#!/usr/bin/python3


def text_indentation(text):
    """
        This function prints a text with 2 new lines
        after each of these characters: ., ? and :

        arg:text: string to be formated

        Raise: TypeError : text must be string
    """
    if type(text) != str:
        raise TypeError("text must be a string")

    new_text = ""
    pun = [".", "?", ":"]

    for char in text:
        new_text += char
        if char in pun:
            new_text += "\n"
            new_text += "\n"
    lines = new_text.split('\n')
    final_text = '\n'.join(line.strip() for line in lines)
    return final_text
