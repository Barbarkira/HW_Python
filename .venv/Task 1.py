class StringList:
    def __init__(self, *things):
        self.data = [str(thing) for thing in things]
    def __iter__(self):
        return iter(self.data)


my_string_list = StringList(1, 1.0, ["a", "b", "c"])

for el in my_string_list:
    assert type(el) == str
    print('2')
