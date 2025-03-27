#!C:\Python37/python.exe
print("Content-type:text/html\r\n\r\n")
import cgi
import pymysql
import os
db=pymysql.connect(host="localhost",user="root",password="root",database="b2c")
form =cgi.FieldStorage()
cname=form.getvalue('cname').strip()
cpwd=form.getvalue('cpwd').strip()
cmobile=form.getvalue('cmobile').strip()
cemail=form.getvalue('cemail').strip()
address=form.getvalue('address')
ccity=form.getvalue('ccity')
cpincode=form.getvalue('cpincode')
cdob=form.getvalue('cdob')
if db:
    try:
        cursor=db.cursor()
        query="select ifnull(max(id),0) from tbl_customer"
        if(cursor.execute(query)>0):
            results=cursor.fetchall()
            for row in results:
                poiid=row[0]
                prefix=poiid+1
            cust_id='CUST';
            customer_id=cust_id+str(prefix)

        query2="select * from tbl_customer where customer_email='%s' and customer_mobile='%s'"%(cemail,cmobile)
        if(cursor.execute(query2)>0):
            print("<script>alert('Already Registered');window.location='index.py';</script>");
        else:
            query1="insert into tbl_customer(id,customer_id,customer_name,customer_pwd,customer_email,customer_mobile,customer_address,customer_city,customer_pincode,customer_dob) values(%d,'%s','%s','%s','%s',%d,'%s','%s',%d,'%s')"%(int(prefix),customer_id,cname,cpwd,cemail,int(cmobile),address,ccity,int(cpincode),cdob)
            cursor.execute(query1)
            db.commit()
            print("<script>alert('Registered Successfully');window.location='index.py';</script>");
    except:
        db.rollback()
        print("<script>alert('Error in Inserting');window.location='index.py';</script>");
else:
    print("Database Error")
