import os
import mysql.connector as MySQL
import xlrd

connection = MySQL.connect(host='localhost', database='exchange', user='root', password='mysql')
cursor = connection.cursor()
folder = 'data/'
upload_files = os.listdir(folder)



query = "INSERT INTO `Si` "\
        "(`ticker`, `per`, `date`, `time`, `open`, `high`, `low`, `close`, `vol`)"\
        " VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"

file_count = 1

for up_file in upload_files:
    print file_count
    rb = xlrd.open_workbook(folder+up_file)
    sheet = rb.sheet_by_index(0)
    start = True
    for rownum in range(sheet.nrows):
        if not start and (sheet.row_values(rownum)[0] == "AR" or sheet.row_values(rownum)[0] == "ARM"):
            row = sheet.row_values(rownum)
            inp_row = tuple(row)
            print inp_row
            #cursor.execute(query, inp_row)

            #connection.commit()
        else:
            start = False

    file_count += 1

cursor.close()
connection.close()

