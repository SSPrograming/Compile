def convert(string: str):
    string.replace('\\t', '\t')
    string.replace('\\n', '\n')
    return string + '\0'
