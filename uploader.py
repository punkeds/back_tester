import os
import mysql.connector as MySQL
import csv

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
    file_input = open(folder+up_file,'r')
    rb = csv.reader(file_input, delimiter = ',')
    start = True
    for rownum in rb:
        if not start:
            rownum[2] = rownum[2][0:4]+'-'+rownum[2][4:6]+'-'+rownum[2][6:8]
            rownum[3] = rownum[3][0:2]+':'+rownum[3][2:4]+':'+rownum[3][4:6]
            cursor.execute(query, rownum)
            connection.commit()
        else:
            start = False

    file_count += 1
cursor.close()
connection.close()

