import collections

class From:
    'provides functionality that is comparable to Microsoft LINQ framework'

    #pass through functions
    def __str__(self):
        return str(self._source)

    def append(self, item):
        self._source.append(item)

    def __getitem__(self, key):
        return self._source.__getitem__(key)

    def __setitem__(self, key):
        self._source.__setitem__(key)

    def __delitem__(self, key):
        self._source.__delitem__(key)

    #checks
    def _is_not_list(self, _input):
        return isinstance(_input, collections.Iterable) == False

    def _is_not_lambda(self, _input):
        LAMBDA = lambda:0
        return (isinstance(_input, type(LAMBDA)) and _input.__name__ == LAMBDA.__name__) == False

    #constructor
    def __init__(self, source):
        if self._is_not_list(source):
            return source
        self._source = source

    #linq functions
    def where(self, exp):
        if(self._is_not_lambda(exp)):
            return self
        localList = []
        for item in self._source:
            if(exp(item)):
                localList.append(item)
        self._source = localList
        return self

    def select(self, exp):
        if(self._is_not_lambda(exp)):
            return self
        localList = []
        for item in self._source:
            localList.append(exp(item))
        self._source = localList
        return self
pass