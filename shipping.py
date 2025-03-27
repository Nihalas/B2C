#!C:\Python37/python.exe
print("Content-type:text/html\r\n\r\n") 
import cgi
import pymysql
import hashlib,time
import datetime
db=pymysql.connect(host="localhost",user="root",password="root",database="b2c")
form=cgi.FieldStorage()
if db:
    cursor=db.cursor()
    sql="select * from tbl_customer_session"
    if(cursor.execute(sql)>0):
        results=cursor.fetchall()
        for row in results:
            LoginName=row[0]
            PassWord=row[1]
    else:
        print("<script type='text/javascript'>location.href='index.py'</script>")
else:
    print("db not connected")
if(LoginName=="" and PassWord==""):
    print("<script type='text/javascript'>location.href='index.py'</script>")
else:
    result=hashlib.md5(LoginName.encode())
    now = datetime.datetime.now()
    sessionid=result.hexdigest()+now.strftime("%Y-%m-%d")
    if db:
        cursor=db.cursor()
        orderidSql="select ifnull(max(order_id),0) from tbl_order_details"
        cursor.execute(orderidSql)
        results=cursor.fetchone()
        order_id=results[0]+1
    else:
        print("db not connected")
    if db:
        cursor=db.cursor()
        selectCustomer="select customer_address,customer_city,customer_pincode from tbl_customer where customer_email='%s'"%(LoginName)
        cursor.execute(selectCustomer)
        results=cursor.fetchone()
        customer_address=results[0]
        customer_city=results[1]
        customer_pincode=results[2]

        cursor=db.cursor()
        shoppingQuery="select product_id,product_name,product_price,product_price_unit,product_weight_unit,qty from tbl_shopcart where sessionid='%s' and user_id='%s'"%(sessionid,LoginName)
        cursor.execute(shoppingQuery)
        results=cursor.fetchall()
        for row in results:
            product_id=row[0]
            product_name=row[1]
            product_price=row[2]
            product_price_unit=row[3]
            product_weight_unit=row[4]
            product_qty=row[5]
            insertQuery="insert into tbl_order_details(order_id,product_id,product_name,price,qty,price_unit,weight_unit) values(%d,%d,'%s',%d,%d,'%s','%s')"%(int(order_id),int(product_id),product_name,int(product_price),int(product_qty),product_price_unit,product_weight_unit)
            delete="delete from tbl_shopcart where sessionid='%s' and user_id='%s'"%(sessionid,LoginName)
            try:
                cursor.execute(insertQuery)
                cursor.execute(delete)
                db.commit()
            except:
                db.rollback()

        cursor=db.cursor()
        lastQuery="select price,qty from tbl_order_details where order_id=%d"%(int(order_id))
        cursor.execute(lastQuery)
        results=cursor.fetchall()
        net_total=0
        for row in results:
            p_price=row[0]
            p_qty=row[1]
            gross_total=p_price * p_qty
            net_total+=gross_total
          

        cursor=db.cursor()
        confirmQuery="insert into tbl_order_tbl values(%d,'%s','%s','%s','%s','%s','%s',%d)"%(int(order_id),LoginName,now.strftime("%Y-%m-%d"),customer_address,customer_pincode,customer_city,sessionid,int(net_total))
        try:
            cursor.execute(confirmQuery)
            db.commit()
            print("<script type='text/javascript'>alert('Order id Confirmed');location.href='customer_homepage.py'</script>")
        except:
            db.rollback()
            print("<script type='text/javascript'>alert('Order id Not Confirmed Try Later');location.href='customer_homepage.py'</script>")
    else:
        print("db not connected")
