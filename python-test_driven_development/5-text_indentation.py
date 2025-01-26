#!/usr/bin/python3
"""
Print un texte
"""


def text_indentation(text):
    """
    Print un text et faire des sauts de ligne en fonction de caractere spéciaux
    Args:
        text (str): le text à print
    Returns:
        None
    Exemple:
        >>> text_indentation("Bonjour. Je vais: Bien?")
        Bonjour.
        <BLANKLINE>
        Je vais:
        <BLANKLINE>
        Bien?
        <BLANKLINE>
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    forbidden_char = ['.', ':', '?']
    forbidden_char_found = False

    for i in range(len(text)):
        if forbidden_char_found:
            forbidden_char_found = False
            if text[i] == " ":
                continue
        for j in range(len(forbidden_char)):
            if text[i] == forbidden_char[j]:
                forbidden_char_found = True
                break
        print("{}".format(text[i]), end="")
        if forbidden_char_found:
            print("\n")

text_indentation("Holberton. School? How are you: John")