import delorean
from decimal import Decimal

# [<Timestamp in iso format>] - SALE - PRODUCT: <product id> - PRICE: $<price of the sale>
log = '[2018-05-05T11:07:12.267897] - SALE - PRODUCT: 1345 - PRICE: $09.00'

divide_it = log.split(' - ')

timestamp_string, _, product_string, price_string = divide_it

timestamp = delorean.parse(timestamp_string.strip('[]'))

product_id = int(product_string.split(':')[-1])

price = Decimal(price_string.split('$')[-1])

print(f'timestamp, product_id, price: {timestamp}, {product_id}, {price}')

print(Decimal('.123'))

# these log elements can be combined together into a single object


class PriceLog(object):
    def __init__(self, timestamp, product_id, price):
        self.timestamp = timestamp
        self.product_id = product_id
        self.price = price

    def __repr__(self):
        return '<PriceLog ({}, {}, {})>'.format(self.timestamp, self.product_id, self.price)

    @classmethod
    def parse(cls, text_log):
        '''
        Parse from a text log with the format
        [<Timestamp>] - SALE - PRODUCT: <product id> - PRICE: $<price>
        to a PriceLog object
        '''
        divide_it = text_log.split(' - ')
        tmp_string, _, product_string, price_string = divide_it
        timestamp = delorean.parse(tmp_string.strip('[]'))
        product_id = int(product_string.split(':')[-1])
        price = Decimal(price_string.split('$')[-1])
        return PriceLog(timestamp=timestamp, product_id=product_id, price=price)


log = '[2018-05-05T12:58:59.998903] - SALE - PRODUCT: 897 - PRICE: $17.99'

print(f'PriceLog.parse(): {PriceLog.parse(log)}')

# Avoid using float types for prices.
print(f'0.1 + 0.1 + 0.1: {0.1 + 0.1 + 0.1}')
