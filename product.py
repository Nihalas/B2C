#!C:\Python37/python.exe
print("Content-type:text/html\r\n\r\n") 
import cgi
import pymysql
db=pymysql.connect(host="localhost",user="root",password="root",database="b2c")
form=cgi.FieldStorage()
categoryname=form.getvalue("cat_name")
subcategoryname=form.getvalue("subcat_name")
print("<html>")
print("<head>")
import head
print("""
<style>
#producttable {
  font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
  border-collapse: collapse;
 
}

#producttable td, #producttable th {
  border: 1px solid #ddd;
  padding: 8px;
}

#producttable tr:nth-child(even){background-color:#696969;}

#producttable tr:hover {background-color: gray;color:white;}

#producttable th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #4CAF50;
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

<script>
function cleardata()
{
 document.frmproduct.product.checked=false
 document.frmproduct.qty.value=""
}
 
</script>

""")
print("</head>")
print("<body onLoad='cleardata();'>")
print("<form action='shopcartprocess.py' method='get' name=frmproduct'>")
import mainnav
print("<div id='page'>")
print("<div id='bootstrap-touch-slider1' style='max-height:600px' class='carousel bs-slider slide  control-round indicators-line' data-ride='carousel' data-pause='click' data-interval='5000'>")
print("<div class='carousel-inner' role='listbox'>")
print("<div class='item active'>")
##print("<!-- Slide Background -->"
print("<img src='images/slider1.jpg' alt='Bootstrap Touch Slider' class='slide-image' />")
print("<div class='carousel-caption'>")
print("<h3></h3>")
print("<p></p>")
print("</div>")
print("<div class='bs-slider-overlay'></div>")
##print("<!-- Slide Text Layer -->"
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
print("<h3 style='font-family:Roboto Slab;font-weight:bolder;'>Products of %s and %s</h3>"%(categoryname,subcategoryname))
print("<hr>")
print("</div>")
print("</div>")
print("</div>")
print("<div class='container'>")
print("<div class='row' style='margin-top:-75px;'>")
#####
if db:
           cursor=db.cursor()
           select="SELECT product_id,cat_name,subcat_name,product_name,product_description,product_price,product_weight_unit,product_price_unit,product_image,product_in_stock FROM tbl_product where cat_name='%s' and subcat_name='%s'"%(categoryname,subcategoryname)
##           print select
           cursor.execute(select)
           results=cursor.fetchall()
           for row in results:
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
                      if product_in_stock>0:
                          print("<div class='col-md-4 col-xs-4 text-center fh5co-project'  data-animate-effect='fadeIn' style='float:left;' id='m_img'>")   
                          print("<a href=''>")
                          print("<img id='m_cat_img' src='SubCatImage/%s' class='img-responsive img-rounded'>"%(product_image))
                          print("<div id='m_cat'>")
                          print("<h3 style='color:#fff;font-weight: bold;font-family:Roboto Slab'>%s"%(product_name))
                          print("</h3>")
                          print("</a>")
                          print("</div>")
                          print("</div>")
                          print("<div class='col-md-4 col-xs-4 text-center fh5co-project'  data-animate-effect='fadeIn' style='float:left;' id='m_img'>")
                          print("<table id='producttable' height=300px width=400px border=1>")
                          print("<tr><th colspan=2><center>Product Details</center></th></tr>")
                          print("<tr><td>Product Name:</td><td>%s</td></tr>"%(product_name))
                          print("<tr><td>Product Description:</td><td>%s</td></tr>"%(product_description))
                          print("<tr><td>Product Price per qty:</td><td>%s</td></tr>"%(product_price))
                          print("<tr><td>Product Price unit:</td><td>%s</td></tr>"%(product_price_unit))
                          print("<tr><td>Product weight:</td><td>%s</td></tr>"%(product_weight_unit))
                          print("<tr><td>Product in Stock:</td><td>%s</td></tr>"%(product_in_stock))
                          print("</table>")
                          print("</div>")
                          
          
                          print("<div style='padding-left:120px;padding-top:100px;' class='col-md-4 col-xs-4 text-center fh5co-project'  data-animate-effect='fadeIn' style='float:left;' id='m_img'>")
                          print("<table id='producttable' width='200px' border=0>")
                          print("<tr><td><input type='checkbox' name='product' value='%s'>Select the Product</td></tr>"%(product_id))
                          print("<tr><td><input type='text' name='qty' placeholder='Enter Qty'></td></tr>")
                          print("<tr><td><input id='sbutton' type='submit' value='Add to cart'></td></tr>")
                          print("<tr><td><input id='cbutton' type='submit' value='Check Out' formaction='checkoutproduct.py'></td></tr>")
                          print("</table>")
                          print("</div>")
                          print("</div><br>")
                          print("<hr>")
                          
                      else:
                          print("<div class='col-md-4 col-xs-4 text-center fh5co-project'  data-animate-effect='fadeIn' style='float:left;' id='m_img'>")
                          print("</div>")
                        
print("</div>")


print("</div>")
print("</div>")
print("</div>")

print("</form>")
##<!-- Get Enquiry -->


print("</body>")
print("</html>")
