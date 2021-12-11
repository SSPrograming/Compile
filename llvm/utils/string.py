def convert_str(string: str):
    string = string.replace('"', '')
    string = string.replace('\\t', '\t')
    string = string.replace('\\n', '\n')
    return string + '\0'


def convert_char(char: str):
    char = char.replace('\'', '')
    char = char.replace('\\t', '\t')
    char = char.replace('\\n', '\n')
    char = char.replace('\\0', '\0')
    return char
