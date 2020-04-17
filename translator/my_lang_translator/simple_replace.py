from . import replace_config


def replace_char(char):
    if char in replace_config.esperanto:
        return replace_config.my_lang[replace_config.esperanto.index(char)]
    else:
        return char


def replace_text(text):
    new_text = ''
    for char in text:
        new_text += replace_char(char)
    return new_text
