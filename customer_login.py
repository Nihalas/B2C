#!C:\Python37/python.exe
print("Content-type:text/html\r\n\r")
import cgi
import pymysql
form=cgi.FieldStorage()
customer_email=form.getvalue('cemail')
customer_pwd=form.getvalue('cpwd')
db=pymysql.connect(host="localhost",user="root",passwd="root",database="b2c")
if db:
    cursor=db.cursor()
    sql="select customer_pwd ,customer_email from tbl_customer where customer_pwd='%s' and customer_email='%s'"%(customer_pwd,customer_email)
    if(cursor.execute(sql)>0):
        results=cursor.fetchone()
        PassWord=results[0]
        LoginName=results[1]
        try:
            insert="insert into tbl_customer_session values('%s','%s')"%(LoginName,PassWord)
            cursor.execute(insert)
            db.commit()
            print("<script>alert('Login Success');window.location='customer_homepage.py';</script>")
        except:
            db.rollback()
    else:
          
            print("<script>alert('Problem in Login');window.location='index.py';</script>")
else:
    print("Error in Db Connection")
