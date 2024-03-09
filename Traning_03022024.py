# ### File handling
# ### File Read
# f=open('AI_Test.txt','r')
# print(f.read())
# f.close()

#### File Write
# g=open('Test_write.txt','w')
# print(g.write("My Name is Hira"))
# g=open('Test_write.txt','r')
# print(g.read())
# g.close()

#### File Append
# file=open('Test_write.txt','a')
# print(file.write("\n Stay in Pune"))
# file.close()
# file=open('Test_write.txt','r')
# print(file.read())

####with method
# with open('AI_Test.txt', mode='r') as f:
#     data=f.read()
#     print(data)

#### Opening a file in write mode.
# with open('AI_Test_1.txt', mode='w') as f: 
#     f.write("Data After write Operation")
# ## opening file in read mode to check the contents.
# with open('AI_Test_1.txt', mode='r') as f:
#     h=f.read()
#     print(h)

# ####Opening a file in append mode and appending data to the file.
# with open("AI_Test_1.txt",'a') as f:
#     f.write(" Appending new data to the file")
# with open("AI_Test_1.txt",mode='r') as f:
#     i=f.read()
#     print(i)

###Rename File Name 
# import os 
# os.rename('AI_Test_1.txt','hira.txt')

# ### Remove file
# os.remove('hira')

# first import library: pip install python -docx
# from docx import Document
# doc_file_path ='test_3.docx'
# doc = Document(doc_file_path)
# for paragraph in doc.paragraphs:
#     print(paragraph.text)
###

#### Database Connection

import pymysql as mq
conn = mq.connect(host='localhost', password='root', user='root')

mycursor = conn.cursor()
print("connection done sucessfully")

