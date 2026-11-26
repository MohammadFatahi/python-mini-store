"""Store product model."""

from math import isfinite


class Product:
    """Keep the name, unit price and available stock of a product."""

    def __init__(self, name: str, price: float, stock: int) -> None:
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Product name cannot be empty.")
        if isinstance(price, bool) or not isinstance(price, (int, float)):
            raise ValueError("Price must be a number.")
        if not isfinite(price) or price <= 0:
            raise ValueError("Price must be a positive, finite number.")
        if type(stock) is not int or stock < 0:
            raise ValueError("Stock must be a non-negative integer.")
        self.name: str = name.strip()
        self.price: float = float(price)
        self.stock: int = stock

    def __str__(self) -> str:
        """Return product information for the console."""
        return f"{self.name} - ${self.price:.2f} (Stock: {self.stock})"
