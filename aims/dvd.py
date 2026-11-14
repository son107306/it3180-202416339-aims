"""DVD objects used by the AIMS mini-store."""

from math import isfinite


class DigitalVideoDisc:
    """Represent one DVD offered for sale."""

    def __init__(self, title, category="", director="", length=0, cost=0.0):
        if not isinstance(title, str) or not title.strip():
            raise ValueError("DVD title must be a non-empty string")
        try:
            valid_cost = float(cost)
        except (TypeError, ValueError) as exc:
            raise ValueError("DVD cost must be a finite nonnegative number") from exc
        if not isfinite(valid_cost) or valid_cost < 0:
            raise ValueError("DVD cost must be a finite nonnegative number")
        if length < 0:
            raise ValueError("DVD length cannot be negative")
        self.title = title
        self.category = category
        self.director = director
        self.length = length
        self.cost = valid_cost

    def __str__(self):
        return f"{self.title} ({self.category}) - {self.cost:.2f} $"


# Keep the original Lab 01 class name usable by older exercises.
DVD = DigitalVideoDisc
