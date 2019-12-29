class ReverseIter(list):
    def __init__(self, l=[]):
        self.i = len(l) - 1
        """ TODO should i check here if l is a list
            or does the base class take care of it? 
        """
        super().__init__(l)

    # returning the list itself reversed so we can iterate over it
    # TODO cant i just return the list reversed?
    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= 0:
            i = self.i
            self.i -= 1
            return self[i]
        else:
            raise StopIteration()


# -------------------------------------------------

def my_enumerate(container, start=0):
    """
    :param container: some iterable object
    :param start: where to start iteration
    :return: current index and the value at that index
    """
    try:
        bla = iter(container)
    except Exception:
        raise TypeError("must give an interable object")
    i = start
    length = len(container)
    for i in range(i, length):
        yield i, container[i]




class ReverseIter:
    def __init__(self, l=[]):
        self.i = len(l) - 1
        self.inner = l
        """ TODO should i check here if l is a list
            or does the base class take care of it?
            """
    # returning the list itself reversed so we can iterate over it
    # TODO cant i just return the list reversed?
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.i >= 0:
            i = self.i
            self.i -= 1
            return self.inner[i]
        else:
            raise StopIteration()


# -------------------------------------------------

def my_enumerate(container, start=0):
    """
        :param container: some iterable object
        :param start: where to start iteration
        :return: current index and the value at that index
        """
    try:
        bla = iter(container)
    except Exception:
        raise TypeError("must give an interable object")
    i = start
    length = len(container)
    for i in range(i, length):
        yield i, container[i]

