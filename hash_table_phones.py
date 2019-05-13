"""
Implement phone book by hash tables.
* add number name - add new record with the name name and phone number number. If
given number is already exist, change update name
* del number  - delete number by given name. If number is missing, do nothing.
* find number - find name with given number. If the number exist, display corresponding name,
otherwise print 'not found'
"""


class PhoneBookFuckYou(object):
    def __init__(self, size):
        self.a = [None] * size
        self.l = size-1

    def add_number(self, name, number):
        self.a[number] = name

    def find_name(self, number):
        if self.a[number] is None:
            return 'not found'
        else:
            return self.a[number]

    def del_number(self, number):
        self.a[number] = None


class PhoneBook(object):
    def __init__(self, size):
        self.a = [[] for _ in range(size)]
        self.l = size-1

    def add_number(self, name, number):
        i = self.l % (number + 1)
        for item in self.a[i]:
            if item[0] == number:
                item[1] = name
                break
        else:
            self.a[i].append([number, name])

    def find_name(self, number):
        i = self.l % (number + 1)
        for item in self.a[i]:
            if item[0] == number:
                return item[1]
        else:
            return 'not found'

    def del_number(self, number):
        i = self.l % (number + 1)
        for item in self.a[i]:
            if item[0] == number:
                self.a[i].remove(item)
                break


if __name__ == "__main__":
    commands = [
        ['add', '911', 'police'],
        ['add', '76213', 'Mom'],
        ['add', '17239', 'Bob'],
        ['find', '76213'],
        ['find', '910'],
        ['find', '911'],
        ['del', '910'],
        ['del', '911'],
        ['find', '911'],
        ['find', '76213'],
        ['add', '76213', 'daddy'],
        ['find', '76213']
    ]

    # commands = [
    #     ['find', '3839442'],
    #     ['add', '123456', 'me'],
    #     ['add', '0', 'granny'],
    #     ['find', '0'],
    #     ['find', '123456'],
    #     ['del', '0'],
    #     ['del', '0'],
    #     ['find', '0']
    # ]

    phone_book = PhoneBookFuckYou(100000)

    for command in commands:
        if command[0] == 'add':
            phone_book.add_number(name=command[2], number=int(command[1]))
        elif command[0] == 'find':
            print(phone_book.find_name(int(command[1])))
        elif command[0] == 'del':
            phone_book.del_number(int(command[1]))
