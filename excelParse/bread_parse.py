import xlrd


def get_data(book, store):
    sheet = book.sheet_by_name(store)
    return_data = []  # Product Description, UPC, Tray
    return return_data


def get_freeze_items():

    return None


def get_names_column(sheet):
    for r in range(1, 4):
        for c in range(sheet.ncols):
            if str(sheet.cell_value(r, c)).lower().strip() in ['product description', 'bread type']:
                return c
    else:
        print("No column found")
        return -1



def is_category(row):
    not_categories = ['', 'Bridges', 'TMD Bottoms', 'TMD Tops', 'Clipstrips', 'Weekenders   Empty',
                      'Weekenders   Product-', '4X4 Display  Empty', '4X4 Display  Product-', 'Rolling Dip Rack']
    return row[3].strip() != '' and row[2] not in not_categories


def get_categories(data):
    return [row[1].strip() for row in data if is_category(row)]

def get_bread_data(xls_path):
    # Store names should match those in the excel sheet
    # stores = ['COSTCO', 'WH Freezer', 'Fred Meyer', 'Military', 'Safeway', 'Walmart']
    book = xlrd.open_workbook(xls_path)
    print([sheet.name for sheet in book.sheets()])
    for data in book.sheets():
        names_column = get_names_column(sheet=data)
        all_items, current_category = {category: []
                                       for category in get_categories(data)}, None
        for row in data:
            if is_category(row):
                current_category = row[names_column].strip()
            elif row[1] != '':
                name, oz, upc, case = row[1:]
                print(name.strip())

                item = {
                    'name': name.strip(),
                    'oz': oz,
                    'upc': upc,
                    'case': case
                }

                all_items[current_category].append(item)
    # return_data = []
    # for store in stores:
    #     return_data.append(get_data(book, store))


if __name__ == "__main__":
    get_bread_data('./bread.xlsx')