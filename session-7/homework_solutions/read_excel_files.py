import openpyxl


def country_codes_in_kbh_data():
    filename = 'sess7/befkbhalderstatkode_small.xlsx'
    wb = openpyxl.load_workbook(filename)
    print(type(wb), wb)
    sheet = wb.get_sheet_by_name("Sheet1")
    print(type(sheet))
    
    list_of_columns = list(sheet.columns)
    print(type(list_of_columns))
    column_of_interest = list_of_columns[3]
    print(type(column_of_interest))
    cells_of_interest = column_of_interest[1:]
    print(type(cells_of_interest))
    
    country_codes = []

    for cell_object in cells_of_interest:
        country_codes.append(cell_object.value)

    return country_codes


def country_codes_in_stats_data():
    filename = 'sess7/country_codes.xlsx'
    wb = openpyxl.load_workbook(filename)
    sheet = wb.get_sheet_by_name("Sheet1")

    list_of_columns = list(sheet.columns)
    column_of_interest = list_of_columns[0]
    cells_of_interest = column_of_interest[1:]

    country_codes = []

    for cell_object in cells_of_interest:
        country_codes.append(cell_object.value)

    return country_codes


def main():
    cph_person_codes = country_codes_in_kbh_data()
    complete_codes = country_codes_in_stats_data()
#     print(cph_person_codes)
#     print(complete_codes)


if __name__ == "__main__":
    main()