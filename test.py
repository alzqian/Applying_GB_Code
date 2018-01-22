import os
import arcpy
from arcpy import env
import my_modules.utils as utils

print 'GO'
mdb_path = utils.to_unicode(
    'D:/Qian/Coding/Python/Applying_GB_Code/res/基础测绘培训数据/MDB'.replace('/', os.sep))
gdb_path = utils.to_unicode(
    'D:/Qian/Coding/Python/Applying_GB_Code/res/基础测绘培训数据/GDB'.replace('/', os.sep))
root_path = mdb_path
for roots, dirs, files in os.walk(root_path):
    for f in files:
        env.workspace = os.path.join(root_path, f)
        tables = arcpy.ListTables()
        print env.workspace + ':  ' + str(tables)
print 'DONE'
