import sqlite3  # import sqlite

###########Python & SqlLite 插入操作：#############
tableName = 'django_migrations'
tempArray01 = ['zs','ls']

# conn = sqlite3.connect("db.sqlite3")  # 连接数据库，数据库文件通过firefox上的sqlitemanager手动构建
# sql = "INSERT INTO %s VALUES('%s','%s')" % (tableName, tempArray01[0], tempArray01[1])
# # 以上是构建sql语句，其中"%s"是数据类型，双引号后"%"是将括号中的变量按物理顺序匹配到前面的数据类型中去
# c = conn.cursor()  # 游标指向到待连接的数据库；类似与要将鼠标点到需要执行的数据库上的意思
# c.execute(sql)  # 执行sql语句
# conn.commit()  # commit，执行完毕。这操作可以操作多条sql语句后做一次即可
###########Python & SqlLite 删除操作：#############
# conn = sqlite3.connect("E:\Python\MyDjangoProject\db.sqlite3")
# c = conn.cursor()  # 获取游标对象
# c.execute("INSERT INTO  sqlite_sequence(name,seq) VALUES ('zs','001')")
# c.execute("INSERT INTO  sqlite_sequence(name,seq) VALUES ('ls','002')")
# c.execute("SELECT  * FROM  sqlite_sequence")
# res = c.fetchall()
# print("sqlite_sequence", res)
# for line in res:
#     for f in line:
#         print(f)
#     print()
# c.close()
# conn.close()
# sql = "DELETE FROM TestTable01"  # 构建delete的sql语句，TestTable01为要删除的表名
# c.execute(sql)
# sql = "DELETE FROM TestTable02"  # 连接上数据库后，可以连续的构建sql语句并execute
# c.execute(sql)
# conn.commit()
# ##########Python & SqlLite 查询操作：#############
# 这里我举了一个我应用中的三表联合查询的实例，“\”是python中的接行号
# 查询是不需要commit的，最后一个for是打印查询的内容，其他应该不解释了吧
# conn = sqlite3.connect("D:/testf.sqlite")
# sql = "SELECT TestCase.ID,TestCase.Subject,ReportTestCase.State,TimeList.ePCPrintState\
# FROM TestCase,ReportTestCase,TimeList\
# WHERE TestCase.ID = ReportTestCase.ID AND TestCase.Subject = TimeList.Subject"
