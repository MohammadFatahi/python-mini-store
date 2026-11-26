"""Console menus and user input handling."""

from math import isfinite

from models.cart import Cart
from store import Store


def read_name(prompt: str) -> str:
    """Read a non-empty product name."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Name cannot be empty.")


def read_integer(prompt: str, minimum: int) -> int:
    """Read an integer at or above the supplied minimum."""
    while True:
        try:
            value = int(input(prompt))
            if value >= minimum:
                return value
        except ValueError:
            pass
        print(f"Enter a whole number of at least {minimum}.")


def read_price() -> float:
    """Read a positive, finite product price."""
    while True:
        try:
            value = float(input("Enter product price: "))
            if isfinite(value) and value > 0:
                return value
        except ValueError:
            pass
        print("Enter a positive, finite price.")


def manager_menu(store: Store) -> None:
    """Authenticate the manager and provide product management actions."""
    print("\nStore Manager Login")
    username = input("Username: ").strip()
    password = input("Password: ")
    if username != "admin" or password != "1234":
        print("Login failed. Returning to main menu.")
        return
    print("Login successful! Welcome, Manager.")
    while True:
        print("\n1. Add products\n2. List products\n3. Return to main menu")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            while True:
                name = read_name("Enter product name (or 'done' to finish): ")
                if name.casefold() == "done":
                    break
                price = read_price()
                stock = read_integer("Enter product stock quantity: ", 0)
                try:
                    product = store.add_product(name, price, stock)
                    print(f"Product added: {product}")
                except ValueError as error:
                    print(error)
        elif choice == "2":
            print(store.list_products())
        elif choice == "3":
            return
        else:
            print("Invalid menu choice.")


def customer_menu(store: Store) -> None:
    """Provide cart actions for one customer visit."""
    cart = Cart()
    try:
        while True:
            print("\nCUSTOMER PORTAL\nAvailable products:")
            print(store.list_products())
            print(
                "\n1. Add item to cart\n2. Remove item from cart"
                "\n3. View cart\n4. Checkout\n5. Return to main menu"
            )
            choice = input("Enter choice: ").strip()
            try:
                if choice == "1":
                    name = read_name("Enter product name: ")
                    product = store.find_product(name)
                    if product is None:
                        raise ValueError("Product was not found in the store.")
                    quantity = read_integer("Enter quantity: ", 1)
                    cart.add_to_cart(product, quantity)
                    print(f"Added {quantity} x {product.name} to cart.")
                elif choice == "2":
                    name = read_name("Enter product name to remove: ")
                    cart.remove_from_cart(name)
                    print(f"Removed {name} from cart.")
                elif choice == "3":
                    print(cart.view_cart())
                elif choice == "4":
                    print(cart.checkout())
                    print("Thank you for shopping with us!")
                elif choice == "5":
                    if cart.items:
                        print("Unpurchased items returned to stock.")
                    return
                else:
                    print("Invalid menu choice.")
            except ValueError as error:
                print(error)
    finally:
        cart.clear()


def run() -> None:
    """Run role selection until the user exits."""
    store = Store()
    print("=================================\nMINI STORE MANAGEMENT SYSTEM")
    print("=================================")
    try:
        while True:
            print("\n1. Store Manager\n2. Customer\n3. Exit Program")
            choice = input("Enter choice: ").strip()
            if choice == "1":
                manager_menu(store)
            elif choice == "2":
                customer_menu(store)
            elif choice == "3":
                print("Goodbye! See you next time.")
                return
            else:
                print("Invalid menu choice.")
    except (EOFError, KeyboardInterrupt):
        print("\nProgram closed.")
