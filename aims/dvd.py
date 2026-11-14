"""DVD objects used by the AIMS mini-store."""


class DigitalVideoDisc:
    """Represent one DVD offered for sale."""

    def __init__(self, title, category="", director="", length=0, cost=0.0):
        if not isinstance(title, str) or not title.strip():
            raise ValueError("DVD title must be a non-empty string")
        if cost < 0:
            raise ValueError("DVD cost cannot be negative")
        if length < 0:
            raise ValueError("DVD length cannot be negative")
        self.title = title
        self.category = category
        self.director = director
        self.length = length
        self.cost = float(cost)

    def __str__(self):
        return f"{self.title} ({self.category}) - {self.cost:.2f} $"


# Keep the original Lab 01 class name usable by older exercises.
DVD = DigitalVideoDisc
