class MyIterator:
    def __init__(self, start, end):
        self.start = start
        self.end =end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        else:
            self.start += 1
            return (self.start-1)**2

my_iter = MyIterator(1, 100)
print(list(my_iter))