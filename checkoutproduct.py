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
    print("<html>")
    print("<head>")
    import head
    print("""
    <style>
    #oproducttable {
      font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
      border-collapse: collapse;
     
    }

    #oproducttable td, #oproducttable th {
      border: 1px solid #ddd;
      padding: 8px;
    }

    #oproducttable tr:nth-child(even){background-color:#FFFFFF;}

    

    #oproducttable th {
      padding-top: 12px;
      padding-bottom: 12px;
      text-align: left;
      background-color: #434F50;
      color: white;
    }

    #sbutton {
      background-color: #4CAF50;
      border: none;
      color: white;
      padding: 15px 32px;
      text-align: center;
      text-decoration: none;
      display: inline-block;
      font-size: 16px;
      margin: 4px 2px;
      cursor: pointer;
    }
    </style>

   

    """)
    print("</head>")
    print("<body onLoad='cleardata();'>")
    import mainnav
    print("<div id='page'>")
    print("<div id='bootstrap-touch-slider1' style='max-height:300px' class='carousel bs-slider slide  control-round indicators-line' data-ride='carousel' data-pause='click' data-interval='5000'>")
    print("<div class='carousel-inner' role='listbox'>")
    print("<div class='item active'>")
    ##print("<!-- Slide Background -->")
    print("<img src='images/slider1.jpg' alt='Bootstrap Touch Slider' class='slide-image' />")
    print("<div class='carousel-caption'>")
    print("<h3></h3>")
    print("<p></p>")
    print("</div>")
    print("<div class='bs-slider-overlay'></div>")
    ##print("<!-- Slide Text Layer -->")
    print("<div class='slide-text slide_style_right'>")

    print("</div>")
    print("</div>")
    print("<div class='item'>")
    print("<img src='images/slider2.jpg' alt='Bootstrap Touch Slider'  class='slide-image'/>")
    print("<div class='carousel-caption'>")
    print("<h3></h3>")
    print("<p></p>")
    print("</div>")
    print("<div class='bs-slider-overlay'></div>")
    print("<div class='slide-text slide_style_right'>")

    print("</div>")
    print("</div>")
    print("<div class='item'>")
    print("<img src='images/slider3.jpg' alt='Bootstrap Touch Slider'  class='slide-image'/>")
    print("<div class='bs-slider-overlay'></div>")
    print("<div class='slide-text slide_style_right'>")

    print("</div>")
    print("</div>")
    print("</div>")
    ##<!-- End of Wrapper For Slides -->
    #print("</div>")
    print("</div>")


    print("<div class='container'>")
    print("<div class='row '>")
    print("<div class='col-md-8 col-md-offset-2 text-center fh5co-heading' id='m_content'>")
    print("<h3 style='font-family:Roboto Slab;font-weight:bolder;'>Your Cart</h3>")
    print("<hr>")
    print("</div>")
    print("</div>")
    print("</div>")
    print("<div class='container'>")
    print("<div class='row' style='margin-top:-100px;'>")
    
    #####
    if db:
        cursor=db.cursor()
        select="SELECT product_id,product_name,product_price,product_price_unit,product_weight_unit,product_image,qty FROM tbl_shopcart where sessionid='%s' and user_id='%s'"%(sessionid,LoginName)
        cursor.execute(select)
        results=cursor.fetchall()
        print("<div   data-animate-effect='fadeIn' style='float:left;' id='m_img'>")
        print("<table id='oproducttable'  width='100%' border=1>")
        print("<tr><th colspan=7><center>Your Cart Details</center></th></tr>")
        print("<tr><th>Product ID</th><th>Product Name</th><th>Product Price per qty & unit</th><th>Product weight</th><th>")
        print("Product Image</th><th>Product Qty</th><th>Product Amount</th></tr>")
        for row in results:
            product_id=row[0] 
            product_name=row[1]
            product_price=row[2]
            product_price_unit=row[3]
            product_weight_unit=row[4]
            product_image=row[5]
            product_qty=row[6]
            product_amount=int(product_qty) * int(product_price)
            
            
            print("<tr><td>%s</td>"%(product_id))
            print("<td>%s</td>"%(product_name))
            print("<td>%s   %s</td>"%(product_price,product_price_unit))
            print("<td>%s</td>"%(product_weight_unit))
            print("<td><img src='SubCatImage/%s' width=100 height=100></td>"%(product_image))
            print("<td>%s</td>"%(product_qty))
            print("<td>%d</td>"%(product_amount))
            print("</tr>")
        print("</table>")
        print("</div>")
    else:
        print("<script type='text/javascript'>alert('Db is not Connected')</script>")                          
      
    print("</div>")
 
    print("</div>")
    
    print("<br><br><br>")
    print("<div>")
    print("<form action='shipping.py' method='post'>")
    print("<center><input id='sbutton' type='submit' value='Confirm Order'></center>")
    print("</form>")
    print("<br><br><br>")
    print("</div>")
    print("</body>")
    print("</html>")
