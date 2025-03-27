#!C:\Python312/python.exe
print("Content-type:text/html")
import cgi
import pymysql
db=pymysql.connect(host="localhost",user="root",password="root",database="b2c")
if db:
           cursor=db.cursor()
           try:
                      delete="delete from tbl_customer_session"
                      cursor.execute(delete)
                      db.commit()
                      print("Location:index.py\r\n\r")
           except:
                      db.rollback()
else:
           print ("not connected")
