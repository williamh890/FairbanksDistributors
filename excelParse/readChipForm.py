import xlrd
import csv
import math
import json

import xlrd
import csv


def csv_from_excel():
    wb = xlrd.open_workbook('chipForm.xls')
    sh = wb.sheet_by_index(0)
    your_csv_file = open('output.csv', 'w', encoding='utf8')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

    for rownum in range(sh.nrows):
        wr.writerow(sh.row_values(rownum))

    your_csv_file.close()


def parse_excel():
    book = xlrd.open_workbook('chipForm.xls')
    sheet = book.sheet_by_index(0)
    num_pages = math.ceil(sheet.nrows / 70)
    print("Number of pages:")
    print(num_pages)
    data = []
    # for pages in range(num_pages):
    data = [[sheet.cell_value(r, c) for c in range(0, 5)] for r in range(sheet.nrows)]
    data.extend([[sheet.cell_value(r, c) for c in range(5, 10)] for r in range(sheet.nrows)])
    # Profit !
    print(data)
    # for item in data:
    #     print(item)
    print("Categories:")
    print(get_categories(data))
    print("Items:")
    for item in get_items(data):
        print(item)
    print("Json:")
    print(make_json(data))


def is_category(row):
    not_categories = ['', 'Bridges', 'TMD Bottoms', 'TMD Tops', 'Clipstrips', 'Weekenders   Empty',
                      'Weekenders   Product-', '4X4 Display  Empty', '4X4 Display  Product-', 'Rolling Dip Rack']
    return True if '-' not in row[3] and row[1] not in not_categories else False


def get_categories(data):
    return [row[1] for row in data if is_category(row)]


def get_items(data):
    return [row[1] for row in data if not is_category(row) and row[1] != '']


def make_json(data):
    all_items, current_category = {category: [] for category in get_categories(data)}, None
    for row in data:
        if is_category(row):
            current_category = row[1]
        elif row[1] != '':
            all_items[current_category].append(row[1:])
    print(json.dumps(all_items))


if __name__ == "__main__":
    csv_from_excel()
    parse_excel()
