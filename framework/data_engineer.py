# coding=utf-8

import xlrd
import os
from framework.logger import Logger

logger = Logger(logger="ExcelUtil").getlog()


class ExcelUtil():
    def __init__(self, excelPath, sheetName):
        self.data = xlrd.open_workbook(excelPath)
        logger.info("open the login data excel")
        self.table = self.data.sheet_by_name(sheetName)  #
        logger.info(u"获取sheet1")
        self.keys = self.table.row_values(0)    # 获取第一行作为KEY值
        self.rowNum = self.table.nrows          # 获取总行数
        logger.info(u"总行数是 %d" % self.rowNum)
        self.colNum = self.table.ncols          # 获取总列数
        logger.info(u"总列数是 %d" % self.colNum)

    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            r = []
            j = 1
            for i in range(self.rowNum-1):
                s = {}
                values = self.table.row_values(j)
                for x in range(self.colNum):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j += 1
            return r


if __name__ == "__main__":
    filePath = os.path.dirname(os.path.abspath('.')) + "/config/test_data.xlsx"
    sheetName = "login"
    data = ExcelUtil(filePath, sheetName)
    print(data.dict_data())




