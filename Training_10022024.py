# #### Extarc data to csv fill.

# import pandas as pd
# import mysql.connector
# #### Connnect to mySQL database
# conn=mysql.connector.connect(host='localhost', password='root', user='root', database="db_hira")

# # ### Execute SQL query:
# # df=pd.read_sql('SELECT * FROM customers', con=conn )

# # ### Save datafram to excel:
# # df.to_excel('C:/Hiraman/AI_ML_Traning/Python_Traning/Python_Training/customers.xlsx', index=False)

# ###Execute SQL query to select  only one column
# column_name= 'name'
# df=pd.read_sql(f"SELECT {column_name} FROM customers", con=conn )

# ### Difine the output Excel file path.
# output_file='output.xlsx'

# #### Store the dsta from the selected colum in the excel file.
# df.to_excel(output_file, index=False)

# ##### Print Confirmation message.
# print(f"Data from column '{column_name}' store in '{output_file}'")

# #### Close the database connection
# conn.close()


