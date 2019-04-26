import xlrd
import json


def get_columns_dictionary(sheet):
    col_dic = {'tray': None}
    for r in range(1, min(10, sheet.nrows)):
        for c in range(sheet.ncols):
            if str(sheet.cell_value(r, c)).lower().strip() in ['product description', 'bread type']:
                col_dic['name'] = c
            elif str(sheet.cell_value(r, c)).lower().strip() in ['tray']:
                col_dic['tray'] = c
            elif str(sheet.cell_value(r, c)).lower().strip() in ['product', 'product code']:
                col_dic['upc'] = c
    return col_dic


def get_starting_row(sheet, names_column):
    for r in range(1, min(10, sheet.nrows)):
        if str(sheet.cell_value(r, names_column)).lower().strip() in ['bread type']:
            return r+1
    else:
        # print("No column found in ", sheet.name)
        return -1


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
        # In case we need to adjust the names, here's one implementation
        # if data.name not in name_map:
        #     continue
        columns_dictionary = get_columns_dictionary(sheet=data)
        if 'name' not in columns_dictionary.keys():
            continue
        names_column = columns_dictionary['name']
        tray_column = columns_dictionary['tray'] if columns_dictionary['tray'] else None
        upc_column = columns_dictionary['upc']
        sheet = [[data.cell_value(r, c) for c in range(0, data.ncols)] for r in range(0, data.nrows)]
        all_items, current_category = {category: [] for category in ['Bread']}, 'Bread'
        for row in sheet[get_starting_row(data, names_column):]:
            if row[names_column].lower() not in ['product description', 'bread type', '', "denny's"]:
                name = row[names_column]
                tray = row[tray_column] if tray_column else ''
                upc = row[upc_column]
                item = {
                    'name': name.strip(),
                    'upc': upc if upc else '',
                    'tray': tray,
                }
                all_items[current_category].append(item)

        all_stores[data.name] = all_items

    return [{
        "store": store, "categories": [
            {"category": category, "items": items}
            for category, items in categories.items()
        ]}
        for store, categories in all_stores.items()
    ]


if __name__ == "__main__":
    get_bread_data('./restaurant.xls')
