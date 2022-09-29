"""
Создайте любой класс с произвольным количеством подклассов, экземпляров, атрибутов и методов
    - как минимум один атрибут должен быть с уровнем доступа private. Соответственно, для получания значений этого атрибута
    нужно использовать методы get и set
"""

class Investments:
    def __int__(self, ticker, market):
        self.ticker = ticker
        self.market = market

    def market_price(self):
        return f'Current Market Price: {self}'


class Stocks(Investments):
    def __int__(self, ticker, market, dividends):
        super().__int__(ticker, market)
        self.dividends = dividends

    def dividend_premium(self):
        return f'Forward Dividend Yeld: {self}%'



class Bond(Investments):
    def coupons(self):
        return f'Dividend (fixed) Yeld: {self}%'


class ETF(Stocks):
    def index(self):
        return f'Included into {self}'

intel = Stocks()

sp500 = ETF('VOO', 'US')

vanguard = Bond('MAXXD', 'GLOBAL')

print(intel.market_price(35))




