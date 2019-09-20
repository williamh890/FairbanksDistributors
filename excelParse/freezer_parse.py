import xlrd
import pprint as pp
import json


def get_names_column(sheet):
    for r in range(1, min(10, sheet.nrows)):
        for c in range(sheet.ncols):
            if str(sheet.cell_value(r, c)).lower().strip() in ['product description', 'bread type']:
                return c
    else:
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
    book = xlrd.open_workbook(xls_path)
    data = book.sheet_by_index(0)
    all_stores = {}
    names_column = get_names_column(sheet=data)
    if names_column == -1:
        print("Error with the names column")
    sheet = [[data.cell_value(r, c) for c in range(
        0, data.ncols)] for r in range(0, data.nrows)]
    all_items, current_category = {category: []
                                    for category in get_categories(sheet, names_column)}, 'Bread'
    print(get_categories(sheet, names_column))
    for row in sheet:
        if is_category(row, names_column):
            current_category = row[names_column].strip()
        elif row[names_column].lower() not in ['product description', 'bread type', '', "denny's"]:
            name, upc = row[names_column:names_column+2]
            tray = row[names_column+3] if row[names_column +
                                                3] != '' else row[names_column+2]
            # if upc:
            #     upc = upc.encode('ascii', 'ignore')
            # name = name.encode('ascii', 'ignore')
            item = {
                "name": name.strip(),
                "upc": upc if upc else '',
                "tray": tray,
            }
            all_items[current_category].append(item) 
    return {
        "categories": [
            {"name": category_name, "items": items}
            for (category_name, items) in all_items.items()
        ]
    }
    # return [{
    #     "store": store, "categories": [
    #         {"category": category, "items": items}
    #         for category, items in categories.items()
    #     ]}
    #     for store, categories in all_stores.items()
    # ]


if __name__ == "__main__":
    # print(json.dumps(get_bread_data('./bread.xlsx')))
    with open('freezerbread.json', 'w') as outfile:
        json.dump(get_bread_data('./freezer.xlsx'), outfile, indent=2)
