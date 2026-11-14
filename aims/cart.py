"""Cart operations for the AIMS mini-store."""

MAX_NUMBERS_ORDERED = 20


class Cart:
    """Store DVDs in insertion order and calculate the total price."""

    def __init__(self):
        self.items = []

    def add_dvd(self, dvd):
        # The boundary condition is exercised in the Lab 03 bugfix flow.
        if len(self.items) > MAX_NUMBERS_ORDERED:
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


def create_cart():
    """Compatibility helper kept for the first iteration of the project."""
    return []
