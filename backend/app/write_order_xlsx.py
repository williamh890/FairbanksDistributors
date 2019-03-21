from openpyxl import Workbook
from datetime import datetime, date, timedelta
from openpyxl.styles import PatternFill, Font, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# set fonts for sheet
small_font = Font(b=True, name='Arial', size=8)
medium_font = Font(b=True, name='Arial', size=10)
large_font = Font(b=True, name='Arial', size=12)
note_font = Font(name='Arial', size=12)

thin = Side(border_style="thin", color="000000")

box_border = Border(top=thin, left=thin, right=thin, bottom=thin)
side_border = Border(left=thin, right=thin)
side_with_bot_border = Border(left=thin, right=thin, bottom=thin)
center =  Alignment(horizontal='center')

catagory_color = PatternFill("solid", fgColor="dddddd")
top_color = PatternFill("solid", fgColor="999999")

def write_xlsx(dest_dir, order_info):

    wb = Workbook()
    ws = wb.active
    ws.title = "Order"
    
    make_top(ws)
    left_row, right_row = write_catagories(ws,order_info)
    write_header(ws,order_info)
    write_footer(ws,order_info)

    format_xlsx(ws)

    write_note(ws, order_info, max(left_row, right_row)+1)

    wb.save(filename = dest_dir)

def make_top(worksheet):
    for col in range(1,11):
        for row in [1,2]:
            cell = worksheet.cell(column = col, row = row)
            cell.fill = top_color
            cell.border = box_border 
    for col in [1,6]:
        wt_cell = worksheet.cell(column = col, row = 2)
        wt_cell.value = "ORDER \n QTY"
        wt_cell.font = medium_font
        wt_cell.alignment = center
    for col in [2,7]:
        pro_cell = worksheet.cell(column = col, row = 2)
        pro_cell.value = "PRODUCT"
        pro_cell.font = large_font
        pro_cell.alignment = center
    for col in [3,8]:
        for row_index in [1,2]:
            weight_cell = worksheet.cell(column = col, row = row_index)
            if row_index == 2:
                weight_cell.value = "OZ"
            else:
                weight_cell.value = "WT."
            weight_cell.font = small_font
            weight_cell.alignment = center
    for col in [4,9]:
        for row_index in [1,2]:
            pack_cell = worksheet.cell(column = col, row = row_index)
            if row_index == 1:
                pack_cell.value = "PACK"
                pack_cell.font = small_font
                worksheet.merge_cells(start_row=1, start_column=col, end_row=1, end_column=col+1)
            else:
                pack_cell.value = "UPC"
                pack_cell.font = medium_font
            pack_cell.alignment = center
    for col in [5,10]:
        case_cell = worksheet.cell(column = col, row = 2)
        case_cell.value = "CASE"
        case_cell.font = small_font
        case_cell.alignment = center

def write_catagories(worksheet, order_info):
    catagories = make_catagories(order_info)
    left_row = 3
    right_row = 3
    for catagory in catagories:
        if left_row <= right_row:
            left_row = write_catagory(worksheet, catagories[catagory], left_row, "left")
        else: 
            right_row = write_catagory(worksheet, catagories[catagory], right_row, "right")
    return (left_row, right_row)

def make_catagories(order_info):
    catagories = {}
    for item in order_info['items']:
        if item['type'] in catagories:
            catagories[item['type']].append(item)
        else:
            catagories[item['type']] = [item]
    return catagories

def write_catagory(worksheet, catagory, row_index, column):
    if column == "left":
        col = 1
    if column == "right":
        col = 6
    cat = catagory[0]['type']
    catagory_cell = worksheet.cell(column = col+1, row = row_index)
    catagory_cell.value = cat
    catagory_cell.font = large_font
    catagory_cell.alignment = center
    catagory_cell.fill = catagory_color

    for cols in range(col,col+5):
        cell = worksheet.cell(column = cols, row = row_index)
        cell.border = box_border
        cell.fill = catagory_color

    row_increase = 1
    for item in catagory:
        for col_increase in range(5):
            cell = worksheet.cell(column = col+col_increase, row = row_index+row_increase)
            if col_increase in [0,1,3]:
                cell.font = medium_font
            else:
                cell.font = small_font
            cell.border = side_border
            if col_increase == 0:
                cell.value = item['amount']
            elif col_increase == 1:
                cell.value = item['name']
            elif col_increase == 2:
                cell.value = item['oz']
            elif col_increase == 3:
                cell.value = item['upc']
            elif col_increase == 4:
                cell.value = item['case']
            if col_increase != 1:
                cell.alignment = center
        row_increase+=1

    for cols in range(col,col+5):
        cell = worksheet.cell(column = cols, row = row_index+row_increase)
        cell.border = side_with_bot_border

    return row_index + row_increase + 1

def format_date(date_iso):
    delivery_date = date(int(date_iso[0:4]),int(date_iso[5:7]), int(date_iso[8:10]))
    delivery_date_str = delivery_date.strftime("%a")
    if is_next_week(delivery_date):
        delivery_date_str = delivery_date.strftime("%a %m/%d")
    return delivery_date_str

def is_next_week(delivery_date):
    today = date.today()
    return ((delivery_date - today) + timedelta(days=today.weekday())>=timedelta(days=7))

def write_header(worksheet, order_info):
    worksheet.oddHeader.left.text = format_date(str(date.today())).upper()
    worksheet.oddHeader.left.size = "12"
    worksheet.oddHeader.left.font = "Arial"
    worksheet.oddHeader.center.text = "CUSTOMER: " + order_info['store']
    worksheet.oddHeader.center.size = "14"
    worksheet.oddHeader.center.font = "Arial"
    worksheet.oddHeader.right.text = "DATE ORDER TAKEN: " + str(date.today())
    worksheet.oddHeader.right.size = "10"
    worksheet.oddHeader.right.font = "Arial"

def write_footer(worksheet, order_info):
    worksheet.oddFooter.left.text = "PULLED BY:____________"
    worksheet.oddFooter.left.size = "12"
    worksheet.oddFooter.left.font = "Arial"
    worksheet.oddFooter.center.text = "FOR DELIVERY ON: " + \
        format_date(order_info['date']).upper()  
    worksheet.oddFooter.center.size = "12"
    worksheet.oddFooter.center.font = "Arial"
    worksheet.oddFooter.right.text = "DELIVERED BY:____________"
    worksheet.oddFooter.right.size = "12"
    worksheet.oddFooter.right.font = "Arial" 

def write_note(worksheet, order_info, row_index):
    for col in range(1,11):
        cell = worksheet.cell(column = col, row = row_index)
        cell.fill = catagory_color
    cell = worksheet.cell(column = 1, row = row_index)
    cell.value = "NOTE:"
    cell.font = medium_font

    cell = worksheet.cell(column = 1, row = row_index+1)
    note = list(order_info['notes'])
    index = 1
    rows = 2
    while index < len(note):
        if index%100 == 0:
            while note[index] != " ":
                index +=1
            note[index] = '\n'
            rows+=1
        index += 1
    wrap_alignment = Alignment(wrap_text=True, vertical="top")
    cell.alignment = wrap_alignment 
    cell.value = "".join(note)
    worksheet.merge_cells(start_row=row_index+1, start_column=1, end_row=row_index+rows, end_column=10)
    cell.font = note_font

def format_xlsx(worksheet):
    col2_length = 0
    col7_length = 0
    for col, column_cells in enumerate(worksheet.columns):
        length = max(len(str(cell.value) or "") for cell in column_cells)*1.1
        if col == 1:
            col2_length = length 
        if col == 6:
            col7_length = length
        worksheet.column_dimensions[get_column_letter(column_cells[0].column)].width = length
    
    ## give both product columns the same width
    prod_len = max(col2_length,col7_length)
    worksheet.column_dimensions[get_column_letter(2)].width = prod_len
    worksheet.column_dimensions[get_column_letter(7)].width = prod_len

    ## set scaling for to fit page and left and right margins to zero
    worksheet.sheet_properties.pageSetUpPr.fitToPage = True
    worksheet.page_setup.fitToWidth = True
    worksheet.page_setup.fitToHeight = False
    worksheet.page_margins.left = 0
    worksheet.page_margins.right = 0 

