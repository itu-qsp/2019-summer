import stat_codes
import openpyxl


def country_codes_data(filename, column_number):
    """Read country code data from a given Excel file,
    in which entire columns contain country codes and
    the first row is a header row without values.

    :param filename: str
        Path to the Excel (.xslx) file containg a row
        with country codes
    :param column_number: int
        The index number of the column containing the
        country codes.
    :return: list
        A list of country code numbers.
    """

    # TODO: Implement me!
    pass


def translate_code_to_text(code):
    # TODO: Implement me!
    pass


def translate_many_codes_to_text(codes):
    """Translate many country into human-readable strings with the help of the
    `stat_codes` module

    :param codes: list
        A list of numerical country codes.
    :return: list
        A list of strings with human readable country codes.
    """

    # TODO: Implement me!
    pass


def filter_for_not_living_in_cph(codes_1, codes_2):
    """Removes all elements from codes_1 which do not appear in codes_2.

    :param codes_1: list
        For example a list of numerical values.
    :param codes_2: list
        For example a list of numerical values.
    :return: list
        A set of elements, which appear in codes_1 but not in codes_2.
    """

    # TODO: Implement me!
    pass


def main():
    cph_person_codes = country_codes_data('befkbhalderstatkode_small.xlsx', 3)
    complete_codes = country_codes_data('country_codes.xlsx', 0)

    print('-----------------')
    print('Persons from the following countries live in Copenhagen:')
    print(translate_many_codes_to_text(cph_person_codes))

    not_living_in_cph = filter_for_not_living_in_cph(complete_codes,
                                                     cph_person_codes)

    print('-----------------')
    print('Persons from the following countries do not live in Copenhagen:')
    print(translate_many_codes_to_text(not_living_in_cph))


if __name__ == "__main__":
    main()
