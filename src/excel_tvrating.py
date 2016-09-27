#! /usr/bin/env -python
# -*- coding:utf-8 -*-
import sys
import urllib
import json
import sys
from tqdm import tqdm
import time

reload(sys)
sys.setdefaultencoding('utf-8')

sourcefile = "/home/asha/data/9.22排名.xlsx"
aimfile = "/home/asha/data/excel_rating"
# from xlrd import open_workbook
# wb = open_workbook(sourcefile)
# for s in wb.sheets():
#     print 'Sheet:',s.name
#     for row in range(s.nrows):
#         values = []
#         for col in range(s.ncols):
#             values.append(s.cell(row,col).value)
#         print ','.join(values)
#     print
# from xlrd import open_workbook
# book = open_workbook(sourcefile)
# print book.nsheets
# for sheet_index in range(book.nsheets):
#     print book.sheet_by_index(sheet_index)
# print book.sheet_names()[3]
# # for sheet_name in book.sheet_names():
# #     print book.sheet_by_name(sheet_name)
# # for sheet in book.sheets():
# #     print sheet


from xlrd import open_workbook,cellname

faim  = open(aimfile,"wb+")
book = open_workbook(sourcefile)
for sheet in book.sheets():
    for row_index in range(sheet.nrows)[6:]:
        linevalue = [sheet.name]
        for col_index in range(sheet.ncols):
            if range(sheet.ncols).index(col_index)==0 and sheet.name !="频道":
                channlename = sheet.cell(row_index,col_index).value.split(' / ')[0]
                showname = sheet.cell(row_index,col_index).value.split(' / ')[1]
                linevalue.append(channlename)
                linevalue.append(showname)
            else:
                linevalue.append(str(sheet.cell(row_index,col_index).value))
        print '\t'.join(linevalue)
        faim.write('\t'.join(linevalue)+"\n")

