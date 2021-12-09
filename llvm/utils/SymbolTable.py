class SymbolTable:
    def __init__(self, prev=None):
        self._ST = {}
        self._prev = prev

    def insert(self, name: str, value):
        self._ST[name] = value

    def get(self, name: str):
        if name in self._ST:
            return self._ST[name]
        if self._prev:
            return self._prev.find(str)
        return None

    def prev(self):
        return self._prev
