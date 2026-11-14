"""Cart operations for the AIMS mini-store."""

MAX_NUMBERS_ORDERED = 20


class Cart:
    """Store DVDs in insertion order and calculate the total price."""

    def __init__(self):
        self.items = []

    def add_dvd(self, dvd):
        # The boundary condition is exercised in the Lab 03 bugfix flow.
        if len(self.items) >= MAX_NUMBERS_ORDERED:
            return False
        self.items.append(dvd)
        return True

    def remove_dvd(self, dvd):
        if dvd not in self.items:
            return False
        self.items.remove(dvd)
        return True

    def total_cost(self):
        return sum(dvd.cost for dvd in self.items)

    def total_cost_with_discount(self, percent=0):
        """Apply a percentage discount to the cart total."""
        # Initial draft deliberately exposes an error for Lab 03 bugfix.
        return self.total_cost() * percent / 100

    def print_cart(self):
        """Print each DVD and the order total."""
        if not self.items:
            print("The cart is empty")
            return
        print("***********************CART***********************")
        print("Ordered Items:")
        for index, disc in enumerate(self.items, start=1):
            print(f"{index}. {disc}")
        print(f"Total cost: {self.total_cost():.2f} $")
        print("***************************************************")


def create_cart():
    """Compatibility helper kept for the first iteration of the project."""
    return []
