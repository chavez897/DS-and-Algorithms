class HashTable:
    def __init__(self, size):
        self.size = size
        self.data = [None] * self.size

    def __str__(self):
        return str(self.__dict__)

    def _hash(self, key):
        hash = 0
        val = str(key)
        for i in range(len(val)):
            hash = (hash + ord(val[i]) * i) % self.size
        return hash

    def set(self, key, value):
        address = self._hash(key)
        if self.data[address] is None:
            self.data[address] = []
        self.data[address].append([key, value])

    def get(self, key):
        address = self._hash(key)
        if self.data[address] is not None:
            for val in self.data[address]:
                if val[0] == key:
                    return val[1]
        return None

    def keys(self):
        keys = []
        for space in self.data:
            if space is not None:
                for item in space:
                    keys.append(item[0])
        return keys

    def values(self):
        values = []
        for space in self.data:
            if space is not None:
                for item in space:
                    values.append(item[1])
        return values


myHashTable = HashTable(10)
myHashTable.set("grapes", 10000)
myHashTable.set("grapeS", 500)
myHashTable.set("Grapesss", 20000)
myHashTable.set("oranges", 200)
print(myHashTable.get("grapes"))
print(myHashTable.keys())
print(myHashTable.values())
print(myHashTable)
