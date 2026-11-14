"""Search operations over a collection of DVDs."""


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
