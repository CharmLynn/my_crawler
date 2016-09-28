#! /usr/bin/env -python
# -*- coding:utf-8 -*-

"""
excel_tvrating
~~~~~~~~~~

This model return result file  as tv rate data from excel upload

"""

import sys
import urllib
import json
import sys
from tqdm import tqdm
import time
from datetime import datetime
from xlrd import open_workbook,cellname

reload(sys)
sys.setdefaultencoding('utf-8')

class Excel_rating(object):
    """docstring for ClassName"""
    def __init__(self, date,sourcefile,aimfile):
        super(Excel_rating, self).__init__()
        self.dateday = date
        self.aimfile = aimfile
        self.sourcefile = sourcefile 

    def getdata(self):
        faim  = open(self.aimfile,"wb+")
        try:
            book = open_workbook(self.sourcefile)
        except Exception, e:
            raise e
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
                faim.write('\t'.join(linevalue)+"\n")
def main():
    if len(sys.argv) !=2:
        datecol = datetime.now().strftime("%Y%m%d")
    else:
        datecol = sys.argv[1]
    sourcefile = "/home/asha/data/9.22排名.xlsx"
    aimfile = "/home/asha/data/excel_rating"
    testaa = Excel_rating(datecol,sourcefile,aimfile)
    testaa.getdata()
if __name__ == '__main__':
        main()    
