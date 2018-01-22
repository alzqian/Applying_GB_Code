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
env.workspace = root_path
for pgdb in arcpy.ListWorkspaces():
    env.workspace = os.path.join(root_path, pgdb)
    print '------' + env.workspace + '------'
    for fc in arcpy.ListFeatureClasses():
        print fc
    print '================================='
print 'DONE'
