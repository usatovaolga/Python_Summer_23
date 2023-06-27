import psycopg2
con = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="qwerty",
    host="localhost",
    port="5432")


cur = con.cursor()
#cur.execute("SELECT * from book")
cur.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'book'")
rows = cur.fetchall()

import openpyxl
wb = openpyxl.Workbook()
wb.save('test2364.xlsx')
ws = wb['Лист1']
for i in range(1,len(rows)):#до последней строки где есть какое-то значение
    for j in range(1,len(rows)):
        ws['A1']='qq'

wb.save('test236.xlsx')
con.close()