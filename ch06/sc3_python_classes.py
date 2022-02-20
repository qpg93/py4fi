""" python classes """

# basic of python classes
class FinancialInstrument():
    """ class demo """
    pass


fi = FinancialInstrument()
print('type fi:\n', type(fi))
print('fi:\n', fi)
print('fi.__str__():\n', fi.__str__())
fi.price = 105
print('fi.price:\n', fi.price)


class FinancialInstrument(FinancialInstrument):
    author = 'Yves Hilpisch'

    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price


print('FinancialInstrument.author:\n', FinancialInstrument.author)
aapl = FinancialInstrument('AAPL', 100)
print('aapl.symbol:\n', aapl.symbol)
print('aapl.author:\n', aapl.author)
aapl.price = 105
print('aapl.price:\n', aapl.price)


class FinancialInstrument(FinancialInstrument):
    def get_price(self):
        """ get price method encapsulation """
        return self.price

    def set_price(self, price):
        """ set price method encapsulation """
        self.price = price


fi = FinancialInstrument('AAPL', 105)
print('fi.get_price():\n', fi.get_price())
fi.set_price(105)
print('fi.get_price():\n', fi.get_price())
print('fi.price:\n', fi.price)


class FinancialInstrument():
    def __init__(self, symbol, price):
        self.symbol = symbol
        self.__price = price    # private instance attribute

    def get_price(self):
        """ get price method encapsulation """
        return self.__price

    def set_price(self, price):
        """ set price method encapsulation """
        self.__price = price


fi = FinancialInstrument('AAPL', 100)
print('fi.get_price():\n', fi.get_price())
try:
    print('fi.__price:\n', fi.__price)
except AttributeError as e:
    print('AttributeError:\n', e)

# if the class name is prepended with a single leading underscore
# direct access and manipulation are still possible
print('fi._FinancialInstrument__price:\n', fi._FinancialInstrument__price)
fi._FinancialInstrument__price = 105
print('fi.get_price():\n', fi.get_price())
fi.set_price(100)
print('fi.get_price():\n', fi.get_price())


class PortfolioPosition():
    """
    aggregate two classes
    take an instance of FinancialInstrument class as attribute value
    """
    def __init__(self, financial_instrument, position_size):
        self.position = financial_instrument
        self.__position_size = position_size

    def get_position_size(self):
        """ get position size """
        return self.__position_size

    def update_position_size(self, position_size):
        """ update position size """
        self.__position_size = position_size

    def get_position_value(self):
        """ calculate the position value """
        return self.__position_size * self.position.get_price()


pp = PortfolioPosition(fi, 10)
print('pp.get_position_size():\n', pp.get_position_size())
print('pp.get_position_value():\n', pp.get_position_value())
print('pp.position.get_price():\n', pp.position.get_price())
pp.position.set_price(105)
print('pp.get_position_value():\n', pp.get_position_value())
