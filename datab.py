# import pymysql as mq
# conn = mq.connect(host='localhost', password='root', user='root')

# mycursor = conn.cursor()
# print("connection done sucessfully")



import mysql.connector
conn=mysql.connector.connect(host='localhost', password='root', user='root', database="db_hira")

mycursor = conn.cursor()
print("connection done sucessfully")

# mycursor.execute("Create database db_hira")
# print("database create sucessfully")

####Table Craete
# mycursor.execute("""CREATE TABLE employee (id int primary key not null, emp_name VARCHAR(50),emp_no int)""")
# print("table is create sucessfully")

# mycursor.execute("insert into employee values('147156','Hira','1100')")
# conn.commit()
# print("record inserted")

# update_query = "UPDATE employee SET emp_name = 'sita' where id = 14716"
# mycursor.execute(update_query)
# conn.commit()
# mycursor.close()

delete_query = "DELETE FROM employee WHERE id = 147156"
mycursor.execute(delete_query)
conn.commit()
mycursor.close()
conn.close()
print("record is deleted")
