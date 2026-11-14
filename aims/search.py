"""Search operations over a collection of DVDs."""


def search_by_category(items, category):
    """Return DVDs matching a category substring without changing the input."""
    if not isinstance(category, str):
        raise TypeError("category must be a string")
    if not category:
        return list(items)
    needle = category.casefold()
    return [dvd for dvd in items if needle in dvd.category.casefold()]



def search_by_title(items, keyword):
    """Return DVDs whose titles contain keyword, ignoring case.

    An empty keyword matches all DVDs. Do not modify the input list.
    """
    if not isinstance(keyword, str):
        raise TypeError("keyword must be a string")
    if not keyword:
        return list(items)
    needle = keyword.casefold()
    return [dvd for dvd in items if needle in dvd.title.casefold()]
