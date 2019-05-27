import sys, os

sys.path.append(os.getcwd())


from page_sms.one_page import HomePage
from page_sms.two_page import NewPage


class Page:
    def __init__(self, driver):
        self.driver = driver

    def get_home_page_obj(self):
        return HomePage(self.driver)

    def get_new_page(self):
        return NewPage(self.driver)

# import pymysql
# 创建数据库连接对象，不能操作数据库
# con = pymysql.connect(host="192.168.30.90",user="root",password="root",database="User",port=3306)
# 游标，只有游标有执行sql权限
# cur = con.cursor()
# 1查询sql
# query_user_info_sql = "select * from User_info limit 10;"
# # 执行sql语句
# cur.execute(query_user_info_sql)
# # 读取返回数据---返回读取全部数据
# print(cur.fetchall())


# 2执行修改操作
# update_sql = "update User_info set user_sex='女' where user_name='可乐45438';"
# # 执行SQL语句
# cur.execute(update_sql)
# 回滚。清除临时空间
# con.rollback()
# # 提交数据到数据库---执行写作操作
# con.commit()


# 关闭操作
# con.close()
