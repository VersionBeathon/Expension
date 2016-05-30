class ListIter(object):
    def __init__(self, data):
        self.__data = data
        self.__count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__count < len(self.__data):
            val = self.__data[self.__count]
            self.__count += 1
            return val
        else:
            raise StopIteration
a = ListIter([1, 2, 3, 4, 5])
for i in a:
    print(i)