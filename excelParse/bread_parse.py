import xlrd
import pprint as pp
import json


def get_names_column(sheet):
    for r in range(1, min(10, sheet.nrows)):
        for c in range(sheet.ncols):
            if str(sheet.cell_value(r, c)).lower().strip() in ['product description', 'bread type']:
                return c
    else:
        # print("No column found in ", sheet.name)
        return -1


def is_category(row, names_column):
    return str(row[names_column-1]).strip().lower() in ['', 'rack'] and \
        str(row[names_column]).strip().lower() not in [
            '', "denny's", 'bread type']


def get_categories(data, names_column):
    categories = [row[names_column].strip()
                  for row in data if is_category(row, names_column)]
    return categories if len(categories) != 0 else ['Bread']


def get_bread_data(xls_path):
    # Based on sheet name, give the data a better name. Later, if it's not in this map, don't parse it.
    name_map = {'COSTCO': 'Costco',
                'WH Freezer': 'Freeze Bread',
                'Fred Meyer': 'Fred Meyer',
                'Military': 'Military',
                'Greely': 'Greely',
                'Safeway': 'Safeway',
                'WalMart': 'Walmart',
                'Fast Food - Order Only': 'Fast Food',
                "Denny's": "Denny's"}
    book = xlrd.open_workbook(xls_path)
    all_stores = {}
    for data in book.sheets():
        if data.name not in name_map:
            continue
        names_column = get_names_column(sheet=data)
        if names_column == -1:
            continue
        sheet = [[data.cell_value(r, c) for c in range(
            0, data.ncols)] for r in range(0, data.nrows)]
        all_items, current_category = {category: []
                                       for category in get_categories(sheet, names_column)}, 'Bread'
        for row in sheet:
            if is_category(row, names_column):
                current_category = row[names_column].strip()
            elif row[names_column].lower() not in ['product description', 'bread type', '', "denny's"]:
                name, upc = row[names_column:names_column+2]
                tray = row[names_column+3] if row[names_column +
                                                  3] != '' else row[names_column+2]
                item = {
                    'name': name.strip(),
                    'upc': upc if upc else '',
                    'tray': tray,
                }
                all_items[current_category].append(item)

        all_stores[name_map[data.name]] = all_items

    return [{
        "store": store, "categories": [
            {"category": category, "items": items}
            for category, items in categories.items()
        ]}
        for store, categories in all_stores.items()
    ]


if __name__ == "__main__":
    get_bread_data('./bread.xlsx')
