"""An individual product entry in a shopping cart."""

from models.product import Product


class CartItem:
    """Associate a product with its requested quantity."""

    def __init__(self, product: Product, quantity: int) -> None:
        if type(quantity) is not int or quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        self.product: Product = product
        self.quantity: int = quantity

    def subtotal(self) -> float:
        """Calculate the price of this cart entry."""
        return self.product.price * self.quantity

    def __str__(self) -> str:
        """Show quantity, unit price and subtotal."""
        return (
            f"{self.product.name} x{self.quantity} "
            f"@ ${self.product.price:.2f} = ${self.subtotal():.2f}"
        )
