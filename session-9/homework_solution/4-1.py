def format_name(firstname, middle_initial, lastname):
    """
    Formats the firstname, single middle initial and lastname of a person

    :param firstname The first name as a string
    :param middle_initial The middle name excl. punctuation
    :param lastname The last name as a string
    :returns A formatted string of the first, middle and last names
    """
    return firstname + " " + middle_initial + ". " + lastname