import os
from external import xlrd
from my_package import utils
xls_path = utils.to_unicode(os.getcwd() + '/res/GB码地类名对照表.xls'.replace('/', os.sep))
print xls_path
book = xlrd.open_workbook(xls_path)
sh = book.sheet_by_index(0)
gb_dict = {}
for rx in range(sh.nrows):
    row = sh.row(rx)
    # print repr(row)
    if row[0].value.strip():
        gb_dict[row[0].value] = row[1].value
    else:
        print 'empty GB at row {0}'.format(rx)
print gb_dict
print 'DONE'