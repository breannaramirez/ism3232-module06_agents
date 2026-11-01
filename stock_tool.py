# stock_tool.py
# Author: Breanna Ramirez


class StockLookup:
    """A tool that looks up product stock quantities."""

    def __init__(self, stock):
        self.stock = stock

    def find_product(self, text):
        """Find a known product mentioned in a message."""
        for product in self.stock:
            if product.lower() in text.lower():
                return product
            return None

    def count_for(self, product):
        """Return the stock count for a product, or None."""
        return self.stock.get(product)
