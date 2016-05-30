# _*_ coding:utf-8 _*_
class ListIterable(object):
    def __int__(self, data):
        self.__data = data

    def __iter__(self):
        print("call iteranle __inter()")
        return ListIterable(self.__data)


class ListIterator(object):
    def __int__(self, data):
        self.__data = data
        self.__count = 0

    def __inter__(self):
        print("call iterator __iter__().")
        return self

    def __next__(self):
        print("call iterator __next__().")
        if self.__count < len(self.__data):
            val = self.__data[self.__count]
            self.__count += 1
            return val
        else:
            raise StopIteration
