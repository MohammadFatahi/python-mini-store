"""Store product collection and lookup operations."""

from models.product import Product


class Store:
    """Manage the products shared by the manager and customer menus."""

    def __init__(self) -> None:
        self.products: list[Product] = []

    def add_product(self, name: str, price: float, stock: int) -> Product:
        """Validate and add a product with a unique name."""
        product = Product(name, price, stock)
        if self.find_product(product.name) is not None:
            raise ValueError("A product with this name already exists.")
        self.products.append(product)
        return product

    def list_products(self) -> str:
        """Return numbered products for display in the console."""
        if not self.products:
            return "No products are available."
        return "\n".join(
            f"[{index}] {product}"
            for index, product in enumerate(self.products, start=1)
        )

    def find_product(self, name: str) -> Product | None:
        """Find a product by name, ignoring surrounding spaces and case."""
        for product in self.products:
            if product.name.casefold() == name.strip().casefold():
                return product
        return None
