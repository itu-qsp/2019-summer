def format_name(firstname, middle_initial, lastname):
    """
    Formats the firstname, lastname and optional middle initial of a person

    :param firstname The first name as a string
    :param middle_initial A middle name excl. punctuation, can be empty ('')
    :param lastname The last name as a string
    :returns A formatted string of the first, middle and last names
    """
    if middle_initial:
        middlename = middle_initial + ". "
    else:
        middlename = ''
    return firstname + " " + middlename + lastname