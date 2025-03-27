#!C:\Python37/python.exe
print("Content-type:text/html\r\n\r\n")
import cgi
import pymysql
db=pymysql.connect(host="localhost",user="root",password="root",database="b2c")   
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
    print("<html>")
    print("<head>")
    import head
    print("</head>")
    print("<body>")
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
    print("<h3 style='font-family:Roboto Slab;font-weight:bolder;'>Hi %s</h3>"%(LoginName))
    print("<h3 style='font-family:Roboto Slab;font-weight:bolder;'>Welcome to B2C Portal</h3>")
    print("</div>")
    print("</div>")
    print("</div>")
    print("<div class='container'>")
    print("<div class='row' style='margin-top:-8%;'>")
    #####
    if db:
        cursor=db.cursor()
        select="SELECT cat_name,cat_image FROM tbl_category"
        cursor.execute(select)
        results=cursor.fetchall()
        for row in results:
            category_name=row[0]
            category_image=row[1]
            print("<div class='col-md-4 col-xs-4 text-center fh5co-project'  data-animate-effect='fadeIn' style='float:left;' id='m_img'>")   
            print("<a href='subcategory.py?cat_name=%s'>"%(category_name))
            print("<img id='m_cat_img' src='CatImage/%s' class='img-responsive img-rounded'>"%(category_image))
            print("<div id='m_cat'>")
            print("<h3 style='color:#fff;font-weight: bold;font-family:Roboto Slab'>%s"%(category_name))
            print("</h3>")
            print("</a>")
            print("</div>")
            print("</div>")
    print("</div>")
    print("</div>")
    print("</div>")
    ##<!-- Get Enquiry -->
    print("<div class='container'>")
    print("<div id='leftSLideBar' class=' hidden-sm navbar-fixed-top'>")
    print("<div class='panel panel-default'  >")
    print("<div class='panel-leftheading' style='text-align:center;'>")
    print("<center><a href='#' ><h3 class='panel-lefttitle' >Get Enquiry&nbsp;&nbsp;&nbsp;&nbsp;</h3></a></center>")
    print("</div>")
    print("<form action='enquiry_mail.py' method='POST'>")
    print("<div class='panel-rightbody' >")
    print("<div id='page1panel' >")
    print("<div class='form-group'>")
    print("<input class='form-control input-sm'  name='name' id='inputlg' type='text' placeholder='Name'>")
    print("</div>")
    print("</div>")	
    print("<div id='page1panel' >")
    print("<div class='form-group'>")
    print("<input class='form-control input-sm' name='mobile' id='inputlg' type='text' placeholder='Mobile No'>")
    print("</div>")
    print("</div>")
    print("<div id='page1panel' >")
    print("<div class='form-group'>")
    print("<input class='form-control input-block' name='comments' id='inputlg' type='text' placeholder='Comments'>")
    print("</div>")
    print("</div>")
    print("<div style='float:left;width:90%;'>")
    print("<button type='submit' class='btn btn-primary btn-sm' style='background-color:#4286f4'>Submit Your Details</button>")
    print("</div>")	
    print("</div>")
    print("</form>")
    print("<div class='clearfix'></div>")
    print("</div>")
    print("</div>")
    print("</div>")
    print("</div>")
    print("</body>")
    print("</html>")
