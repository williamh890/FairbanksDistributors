import xlrd
import csv

import xlrd
import csv

def csv_from_excel():
    wb = xlrd.open_workbook('chipForm.xls')
    sh = wb.sheet_by_name('Sheet1')
    your_csv_file = open('output.csv', 'w', encoding='utf8')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

    for rownum in range(sh.nrows):
        wr.writerow(sh.row_values(rownum))

    your_csv_file.close()

def readExcel():
    book = xlrd.open_workbook('chipForm.xls')
    sheet = book.sheet_by_name('Sheet1')
    data = [[sheet.cell_value(r, c) for c in range(0, 5)] for r in range(sheet.nrows)]
    data.extend([[sheet.cell_value(r, c) for c in range(5, 10)] for r in range(sheet.nrows)])
    # Profit !
    print(data)
    for item in data:
        print(item)
    print("Categories:")

    notCategories = ['', 'DISPLAY SUPPLIES','Bridges', 'TMD Bottoms', 'TMD Tops', 'Clipstrips', 'Weekenders   Empty',
                     'Weekenders   Product-', '4X4 Display  Empty', '4X4 Display  Product-']
    for item in data:
        if '-' not in item[3]:
            if item[1] not in notCategories:
                print(item[1])


if __name__ == "__main__":
    csv_from_excel()
    readExcel()
