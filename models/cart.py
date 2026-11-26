"""Shopping cart operations and stock reservation."""

from models.cartitem import CartItem
from models.product import Product


class Cart:
    """Manage cart entries and keep their quantities consistent with stock."""

    def __init__(self) -> None:
        self.items: list[CartItem] = []

    def add_to_cart(self, product: Product, quantity: int) -> None:
        """Reserve stock and merge repeated additions into one entry."""
        if type(quantity) is not int or quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        if quantity > product.stock:
            raise ValueError(f"Insufficient stock. Available: {product.stock}.")
        for item in self.items:
            if item.product is product:
                item.quantity += quantity
                break
        else:
            self.items.append(CartItem(product, quantity))
        product.stock -= quantity

    def remove_from_cart(self, product_name: str) -> None:
        """Remove an entire entry and restore its reserved stock."""
        for item in self.items:
            if item.product.name.casefold() == product_name.strip().casefold():
                item.product.stock += item.quantity
                self.items.remove(item)
                return
        raise ValueError("Product was not found in your cart.")

    def view_cart(self) -> str:
        """Return cart details without handling console input or output."""
        if not self.items:
            return "Your cart is empty."
        lines = [str(item) for item in self.items]
        lines.append(f"Total: ${self.total_price():.2f}")
        return "\n".join(lines)

    def total_price(self) -> float:
        """Return the sum of all item subtotals."""
        return sum((item.subtotal() for item in self.items), 0.0)

    def checkout(self) -> str:
        """Return the final invoice and complete a non-empty purchase."""
        if not self.items:
            raise ValueError("Cannot checkout with an empty cart.")
        invoice = "Final Checkout:\n" + self.view_cart()
        # Stock was already reserved when items were added.
        self.items.clear()
        return invoice

    def clear(self) -> None:
        """Release reserved stock when a customer leaves without purchasing."""
        for item in self.items:
            item.product.stock += item.quantity
        self.items.clear()
