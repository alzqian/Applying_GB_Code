import os
import time
import arcpy
from arcpy import env
import my_modules.utils as utils

print 'GO'
mdb_path = utils.to_unicode(
    'D:/Qian/Coding/Python/Applying_GB_Code/res/MDB'.replace('/', os.sep))
gdb_path = utils.to_unicode(
    'D:/Qian/Coding/Python/Applying_GB_Code/res/基础测绘培训数据/GDB'.replace('/', os.sep))
data_path = mdb_path
env.workspace = data_path
for ws in arcpy.ListWorkspaces():
    # 处理一个ws的时间起点
    start_time = time.time()
    
    env.workspace = os.path.join(data_path, ws)
    print '------' + env.workspace + '------'
    for fc in arcpy.ListFeatureClasses():
        print fc + ':'
        fc_path = os.path.join(env.workspace, fc)
        desc = arcpy.Describe(fc_path)
        is_GB_Exists = False
        is_GB_Name_Exists = False
        table_all_field_names = []
        for name in [field.name for field in desc.fields]:
            table_all_field_names.append(name)
        print str(table_all_field_names)
        if 'GB' in table_all_field_names:
            if 'GB_Name' in table_all_field_names:
                print '    old GB_Name Field already exists, gonna delete it.'
                arcpy.DeleteField_management(fc, 'GB_Name')
            arcpy.AddField_management(in_table=fc, field_name='GB_Name',
                                      field_alias='地类名称', field_type='TEXT', field_length=20)
            print '    new GB_Name Field has been added.'
        '''
        if 'GB' in [field.name for field in desc.fields]:
            if 'GB_Name' in []:
                print '    old GB_Name Field already exists, gonna delete it.'
                arcpy.DeleteField_management(fc, 'GB_Name')
            arcpy.AddField_management(in_table=fc, field_name='GB_Name',
                                    field_alias='地类名称', field_type='TEXT', field_length=20)
            print '    new GB_Name Field has been added.'
            '''
    end_time = time.time()
    time_cost = (end_time - start_time)*1000
    print '耗时 {0} 毫秒'.format(time_cost)
    print '================================='
print 'DONE'
