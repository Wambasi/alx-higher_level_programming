#!/usr/bin/python3

"""Creating a function."""


def text_indentation(text):
    """Defining a function that prints a text with
    2 new lines after each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    s = text[:]
    for d in ".?:":
        list_ = s.split(d)
        s = ""
        for i in list_:
            i = i.strip(" ")
            s = i + d if s == "" else s + "\n\n" + i + d
    print(s[:-3], end="")
