import xlrd
import csv

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
    data = [[sheet.cell_value(r, c) for c in range(0, 5)] for r in range(sheet.nrows)]
    data.extend([[sheet.cell_value(r, c) for c in range(5, 10)] for r in range(sheet.nrows)])
    # Profit !
    print(data)
    # for item in data:
    #     print(item)
    print("Categories:")
    print(get_categories(data))
    print("Items:")
    print(get_items(data))


def is_category(row):
    not_categories = ['', 'DISPLAY SUPPLIES', 'Bridges', 'TMD Bottoms', 'TMD Tops', 'Clipstrips', 'Weekenders   Empty',
                      'Weekenders   Product-', '4X4 Display  Empty', '4X4 Display  Product-', 'Rolling Dip Rack']
    if '-' not in row[3]:
        if row[1] not in not_categories:
            return True
    return False


def get_categories(data):

    categories = []
    for item in data:
        if is_category(item):
            # print(item[1])
            categories.append(item[1])
    return categories


def get_items(data):
    items = []
    for row in data:
        if not is_category(row) and row[1] != '':
            items.append(row[1])
    return items


if __name__ == "__main__":
    csv_from_excel()
    parse_excel()
