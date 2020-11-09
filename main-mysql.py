#conding=utf8  
import os
import mysql.connector
import psutil
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",       # 数据库主机地址
  user="text",    # 数据库用户名
  passwd="123456",  # 数据库密码
  database="text"
)
print("Opened database successfully")
mycursor = mydb.cursor()
 
# DB = conn.cursor()
sql1="DROP TABLE IF EXISTS file"
mycursor.execute(sql1)
sql2="CREATE TABLE `file`(`id` int(11) NOT NULL AUTO_INCREMENT,`filename` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,`filerouted` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,PRIMARY KEY (`id`) USING BTREE) ENGINE = MyISAM AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;"
mycursor.execute(sql2)
print("Table created successfully")

disk=psutil.disk_partitions()
for i in range(7):
    _wake_ = disk[i][0]
#     g = os.walk([_wake_])  
    for path, file_dir, file in os.walk(_wake_):
        _vr_=path
        for file_name in file:
         _va_ = file_name
         sql3="INSERT INTO file (filename, filerouted) VALUES (%s, %s)"
         val=(_va_, _vr_)
         mycursor.execute(sql3,val)
print("数据输入完成")
mydb.commit()
