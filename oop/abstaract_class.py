import abc
class AbstractPage(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_page(self):
        pass


class ShopPage(AbstractPage):
    def get_page(self):
        return True



shop_page = ShopPage()
print(shop_page)