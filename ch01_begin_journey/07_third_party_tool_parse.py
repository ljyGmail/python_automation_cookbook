import delorean
from decimal import Decimal
import parse

LOG = '[2018-05-06T12:58:00.714611] - SALE - PRODUCT: 1345 - PRICE: $09.99'

# Analyze it and describe it as you would do when trying to print it
FORMAT = '[{date}] - SALE - PRODUCT: {product} - PRICE: ${price}'

# parse and check the results
result = parse.parse(FORMAT, LOG)
print(f'result: {result}')

# Note the results are all strings.
print(f'result["date"]: {result["date"]}, type: {type(result["date"])}')
print(
    f'result["product"]: {result["product"]}, type: {type(result["product"])}')
print(f'result["price"]: {result["price"]}, type: {type(result["price"])}')

# Define the types to be parsed.
FORMAT = '[{date:ti}] - SALE - PRODUCT: {product:d} - PRICE: ${price:05.2f}'

# Parse once again.
result = parse.parse(FORMAT, LOG)
print(f'result after specifying type: {result}')

print(f'result["date"]: {result["date"]}, type: {type(result["date"])}')
print(
    f'result["product"]: {result["product"]}, type: {type(result["product"])}')
print(f'result["price"]: {result["price"]}, type: {type(result["price"])}')

# Define a custom type for the price to avoid issues with the float type.


def price(string):
    return Decimal(string)


FORMAT = '[{date:ti}] - SALE - PRODUCT: {product:d} - PRICE: ${price:price}'
result = parse.parse(FORMAT, LOG, {'price': price})

# Parse again
print(f'result after specifying type: {result}')

print(f'result["date"]: {result["date"]}, type: {type(result["date"])}')
print(
    f'result["product"]: {result["product"]}, type: {type(result["product"])}')
print(f'result["price"]: {result["price"]}, type: {type(result["price"])}')

# The timestamp can also be translated into a delorean object for consistency.


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
        def price(string):
            return Decimal(string)

        def isodate(string):
            return delorean.parse(string)
        FORMAT = '[{timestamp:isodate}] - SALE - PRODUCT: {product:d} - PRICE: ${price:price}'
        formats = {'price': price, 'isodate': isodate}
        result = parse.parse(FORMAT, text_log, formats)
        return cls(timestamp=result['timestamp'], product_id=result['product'], price=result['price'])


log = '[2018-05-06T14:58:59.051545] - SALE - PRODUCT: 827 - PRICE: $22.25'
print(f'PriceLog.parse(): {PriceLog.parse(log)}')
