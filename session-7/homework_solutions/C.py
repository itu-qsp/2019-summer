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
    wb = openpyxl.load_workbook(filename)
    sheet = wb.get_sheet_by_name("Sheet1")

    list_of_columns = list(sheet.columns)
    column_of_interest = list_of_columns[column_number]
    cells_of_interest = column_of_interest[1:]

    country_codes = []

    for cell_object in cells_of_interest:
        country_codes.append(cell_object.value)
        
    country_codes = set(country_codes)
    country_codes = sorted(country_codes)

    return country_codes


def translate_code_to_text(code):
    # TODO: Implement me in Ex E
    pass


def main():
    cph_person_codes = country_codes_data('sess7/befkbhalderstatkode_small.xlsx', 3)
    complete_codes = country_codes_data('sess7/country_codes.xlsx', 0)

    print("Country codes in Copenhagen")
    print(cph_person_codes, "\n")
    print("All country codes")
    print(complete_codes, "\n")

    descriptive_string = translate_code_to_text(5126)
    print("The country for 5126 is:")
    print(descriptive_string)

if __name__ == "__main__":
    main()