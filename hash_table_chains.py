"""
Implement hash table with linked elements.
Implementation should support following commands
* add string - add string to the table, if the string is already exists, ignore the command
* del string - delete string from the table. If requiested string is missing, ignore the command
* find string - print "yes" if string exists, "no" otherwise
* check i - print i-th list or empty string it it is empty
"""

class HashTable(object):
    def __init__(self, m):
        self.a = [[] for _ in range(m)]
        self.m = m

    def _calc_index(self, st):
        val = 0
        for i, c in enumerate(st):
            val += (ord(c) * 263**i)
        val %= 1_000_000_007
        return val % self.m

    def add(self, st):
        i = self._calc_index(st)
        for item in self.a[i]:
            if item == st:
                break
        else:
            self.a[i] = [st] + self.a[i]

    def find(self, st):
        i = self._calc_index(st)
        for item in self.a[i]:
            if item == st:
                return "yes"
        else:
            return "no"

    def check(self, i):
        return " ".join(self.a[i])

    def delete(self, st):
        i = self._calc_index(st)
        for item in self.a[i]:
            if item == st:
                self.a[i].remove(item)
                break


if __name__ == "__main__":
    m = 5
    commands = [
        ['add', 'world'],
        ['add', 'HellO'],
        ['check', 4],
        ['find', 'World'],
        ['find', 'world'],
        ['del', 'world'],
        ['check', '4'],
        ['del', 'HellO'],
        ['add', 'luck'],
        ['add', 'GooD'],
        ['check', 2],
        ['del', 'good']
    ]

    m = 4
    commands = [
        ['add', 'test'],
        ['add', 'test'],
        ['find', 'test'],
        ['del', 'test'],
        ['find', 'test'],
        ['find', 'Test'],
        ['add', 'Test'],
        ['find', 'Test']
    ]

    ht = HashTable(m)

    for command in commands:
        if command[0] == 'add':
            ht.add(command[1])
        elif command[0] == 'find':
            print(ht.find(command[1]))
        elif command[0] == "check":
            print(ht.check(int(command[1])))
        elif command[0] == 'del':
            ht.delete(command[1])
