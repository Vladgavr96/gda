class Phone:
    color = 'Grey'
    _mark = 'Samsung'
    __model = 'Galaxy'

    @classmethod
    def show_full_name(cls):
        print(f'{cls.color} {cls._mark} {cls.__model}')

    @property
    def mark(self):
        return self._mark

    @staticmethod
    def test():
        print('Статический метод')




print(Phone.color)
print(Phone.mark)
Phone.show_full_name()
#print(dir(Phone))
print(Phone._Phone__model)
Phone.test()