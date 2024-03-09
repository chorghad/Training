import pymysql as mq

mydb = mq.connect(
  host="localhost",
  user="root",
  password="root",
  database="db_hira"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE mydatabase")
# print("database is created")
# mycursor.execute("SHOW TABLES")

# for x in mycursor:
#   print(x)
# ------------------------------------------------------------------------
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
# # ----------------------------------------------------------------------------------------
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mycursor.execute(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "record inserted.")
# --------------------------------------------------------------------------------------------
# inser multile row

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = [
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]

# mycursor.executemany(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "was inserted.")
# # ---------------------------------------------------------------------------------------------
# mycursor.execute("SELECT * FROM customers")

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)
# # -----------------------------------------------------------------------------
# # select only name and address of coloumn
# mycursor.execute("SELECT name, address FROM customers")

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)
# # ----------------------------------------------------------------------------
# # Using the fetchone() Method
# # If you are only interested in one row, you can use the fetchone() method.

# # The fetchone() method will return the first row of the result:

# mycursor.execute("SELECT * FROM customers")

# myresult = mycursor.fetchone()

# print(myresult)
# # ------------------------------------------------------
# # Select With a Filter
# # When selecting records from a table, you can filter the selection by using the "WHERE" statement:
# # Select record(s) where the address is "Park Lane 38": result:

# sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)
# #   -----------------------------------------------------------------------------------------------
# # Sort the Result
# # Use the ORDER BY statement to sort the result in ascending or descending order.
# # The ORDER BY keyword sorts the result ascending by default. To sort the result in descending order, use the DESC keyword.


# sql = "SELECT * FROM customers ORDER BY name"

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)
  
# #   --------------------------------------------------------------------------------------------------

# # Use the DESC keyword to sort the result in a descending order.

# sql = "SELECT * FROM customers ORDER BY name DESC"

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)
# #   ---------------------------------------------------------------------------------------------

# # Delete any record where the address is "Mountain 21"

# sql = "DELETE FROM customers WHERE address = 'Mountain 21'"

# mycursor.execute(sql)

# mydb.commit()

# print(mycursor.rowcount, "record(s) deleted")
# # --------------------------------------------------------------------------------
# # You can delete an existing table by using the "DROP TABLE" statement:

# sql = "DROP TABLE customers"

# mycursor.execute(sql)
# # ----------------------------------------------------------------------------------
# # Overwrite the address column from "Valley 345" to "Canyon 123":
# sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"

# mycursor.execute(sql)

# mydb.commit()

# print(mycursor.rowcount, "record(s) affected")
# # --------------------------------------------------------------------------------------
# # Limit the Result
# # You can limit the number of records returned from the query, by using the "LIMIT" statement:

# mycursor.execute("SELECT * FROM customers LIMIT 5")

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)
# #   ---------------------------------------------------------------------------------------
