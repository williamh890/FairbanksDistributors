import xlrd
import pprint as pp
import re
import json


def get_names_column(sheet):
    for r in range(1, min(10, sheet.nrows)):
        for c in range(sheet.ncols):
            if str(sheet.cell_value(r, c)).lower().strip() == 'product description':
                return c
    else:
        # print("No column found in ", sheet.name)
        return -1


def is_category(row, names_column):
    return str(row[names_column-1]).strip().lower() == '' and \
        str(row[names_column]).strip().lower() != ''


def get_categories(data, names_column):
    categories = [row[names_column].strip()
                  for row in data if is_category(row, names_column)]
    return categories if len(categories) != 0 else ['Tortilla']


def get_taco_loco_data(xls_path):
    # Based on sheet name, give the data a better name. Later, if it's not in this map, don't parse it.
    name_map = {'Fred Meyer': 'Fred Meyer',
                'Military': 'Military',
                'Safeway': 'Safeway',
                'Wal-Mart': 'Walmart',}
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
                                       for category in get_categories(sheet, names_column)}, 'Tortilla'
        for row in sheet:
            if is_category(row, names_column):
                current_category = row[names_column].strip()
            elif row[names_column].lower() not in ['product description', '']:
                upc, name = row[names_column-1:names_column+1]
                case = (str(row[names_column+1]).strip().lower().split("/"))
                oz = ''
                if len(case) == 2 and "oz" in case[1]:
                    oz = re.sub('[^0-9\.]','', case[1]) 
                case = re.sub('[^0-9\.]','', case[0])
                item = {
                    'name': name.strip(),
                    'oz': oz,
                    'upc': upc if upc else '',
                    'case': case,
                    
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
    get_taco_loco_data('./taco_loco.xlsx')