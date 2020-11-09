#conding=utf8  
import os  #导入os模块
import sqlite3  #导入sqlite模块
import psutil # 导入psutil模块
conn = sqlite3.connect('D:\\sqlite\\test.db') # 建立sqlite数据库链接 
print("Opened database successfully") # 输出数据库链接建立是否成功
DB = conn.cursor()  #将sql语句参数化
disk = psutil.disk_partitions()  #获取系统所有分区
disktop=len(disk)
for i in range(disktop):  #遍历所有分区
    _wake_ = disk[i][0] #获取分区名
    _disk_=_wake_[0][0] #提取名
    DB.execute("DROP TABLE IF EXISTS " + _disk_ + ";")  #判断分区名为命名的数据表是否存在，存在则删除
# 创建已硬盘分区名命名的数据表
    DB.execute("CREATE TABLE " + _disk_ + "(" + "ID " + "INTEGER PRIMARY KEY AUTOINCREMENT, " + "filename " + "TEXT, " + "filerouted " + "BLOB NOT NULL" + ")" + ";")
# 判断数据表是否建立成功
    print("Table created successfully to ",_disk_)
    for path, file_dir, file in os.walk(_wake_):  
        _vr_=path #将文件路径赋予变量_vr_
        for file_name in file: #获取每个文件夹下的文件名
          _va_ = file_name  #将文件名赋予变量_va_
          # 循环输入每个文件下的所有文件名，文件路径
        DB.execute("INSERT INTO " + _disk_ + " ( filename,filerouted) VALUES (?,? )", (_va_, _vr_))
    print("Records created successfully to", _disk_)
    #输入完成所有数据



conn.commit() #向数据表提交当前数据
conn.close() #释放数据库资源