def convert(string: str):
    string = string.replace('"', '')
    string = string.replace('\\t', '\t')
    string = string.replace('\\n', '\n')
    return string + '\0'
