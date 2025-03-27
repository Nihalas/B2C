#!C:\Python37/python.exe
print("Content-type:text/html\r\n\r\n") 
import cgi
import pymysql
import hashlib,time
import datetime
db=pymysql.connect(host="localhost",user="root",password="root",database="b2c")
form=cgi.FieldStorage()
pid=form.getvalue("product")
qty=form.getvalue("qty")
if db:
    cursor=db.cursor()
    sql="select * from tbl_customer_session"
    if(cursor.execute(sql)>0):
        results=cursor.fetchall()
        for row in results:
            LoginName=row[0]
            PassWord=row[1]
    result=hashlib.md5(LoginName.encode())
    now = datetime.datetime.now()
    sessionid=result.hexdigest()+now.strftime("%Y-%m-%d")
    print(type(pid))
    selectQuery="select * from tbl_product where product_id=%d"%(int(pid))
    
    cursor.execute(selectQuery)
    row=cursor.fetchone()
    product_id=row[0] 
    category_name=row[1]
    subcategory_name=row[2]
    product_name=row[3]
    product_description=row[4]
    product_price=row[5]
    product_weight_unit=row[6]
    product_price_unit=row[7]
    product_image=row[8]
    product_in_stock=row[9]
    deltab=row[10]
    if(int(qty)>int(product_in_stock)):
        print("<script>alert('Product out of Stock');window.location='product.py?cat_name=%s&subcat_name=%s';</script>"%(category_name,subcategory_name))
    else:
        selectQuery1="select * from tbl_shopcart where product_id=%d and sessionid='%s' and user_id='%s'"%(int(product_id),sessionid,LoginName)
        if(cursor.execute(selectQuery1)>0):
            results=cursor.fetchall()
            for row in results:
                rqty=row[8]
                updateQuery="update tbl_shopcart set qty=%d where product_id=%d and sessionid='%s' and user_id='%s'"%(int(rqty),product_id,sessionid,LoginName)
                cursor.execute(updateQuery)
                db.commit()
                print("<script>alert('Added to cart Successfuly');window.location='product.py?cat_name=%s&subcat_name=%s';</script>"%(category_name,subcategory_name))
        else:
            try:
                insertQuery="insert into tbl_shopcart values(%d,'%s','%s','%s',%d,'%s','%s','%s',%d,'%s','%s')"%(int(product_id),product_name,category_name,subcategory_name,int(product_price),product_price_unit,product_weight_unit,product_image,int(qty),sessionid,LoginName)
                cursor.execute(insertQuery)
                db.commit()
                print("<script>alert('Added to cart Successfuly');window.location='product.py?cat_name=%s&subcat_name=%s';</script>"%(category_name,subcategory_name))
            except:
                db.rollback()
                print("<script>alert('Error in Adding to Cart');window.location='product.py?cat_name=%s&subcat_name=%s';</script>"%(category_name,subcategory_name))
    db.close()
else:
    print("<script>alert('Not Connected with Database');window.location='product.py?cat_name=%s&subcat_name=%s';</script>"%(category_name,subcategory_name))
