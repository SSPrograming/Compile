class SymbolTable:
    def __init__(self, prev=None):
        self._ST = {}
        self._prev = prev

    def __str__(self):
        return str(self._ST)

    def insert(self, name: str, value):
        if name in self._ST:
            print('变量重定义：' + name)
            raise Exception('panic: insert')
        self._ST[name] = value

    def get(self, name: str):
        if name in self._ST:
            return self._ST[name]
        if self._prev:
            return self._prev.get(name)
        return None

    def prev(self):
        return self._prev
