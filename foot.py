import cgi
print("<div style='margin-top:1%;z-index:-1;'>"
##<!-- Footer -->
print("<footer id='fh5co-footer' >"
print("<div class='container'>"
print("<div class='row'>"
print("<div class='col-md-8 col-sm-8 col-xs-8' style='margin-top:5%;'>"
print("<ul>"
print("<ol><a href='index.py'  id='footerhlink'>Home</a><a href='#add_your_list' id='footerhlink' data-toggle='modal'>Contact</a><a href='T&C.py' id='footerhlink' data-toggle='modal'>Terms &amp; Condition</a></ol>"
print("</ul>"
print("</div>"
print("<div class='col-md-4 col-sm-4 col-xs-4' style='margin-top:2%;'>"
print("<p>"
print("<div class='foot-item'>"
print("<div class='brand-bg'>"
## <!-- Social Media Icons -->
print("<a href='#android' data-toggle='modal'><img src='./images/Googleplay.png' alt='Google Play Store' style='width:20%;'></a>"
print("<a href='#'><img src='./images/apple.png' alt='App Store' style='width:20%;'></a>"
print("<a href='#'><img src='./images/windows.png' alt='Windows Store' style='width:20%;'></a>"
print("<a href='#'><img src='./images/BlackBerry.png' alt='Blackerry App World' style='width:20%;'></a>"
print("</div>"
print("</div>"
print("</p>"
print("</div>"
print("</div>"
print("<div class='row'>"
print("<div class='copyright'>"	  
print("<p class='block' style='color:#4286f4;padding:10px;text-align:center;font-weight:bolder;'>&copy; All Rights Resrved @ DoEmart 2017.</p>"
print("</div>")
print("</div>")
print("</div>")
print("</footer>")
print("<div class='gototop js-top'>")
print("<a href='#' class='js-gotop'><i class='icon-arrow-up'></i></a>")
print("</div>")
print("</div>")
##<!-- End of Footer -->"
##print(" <!-- add List Modal-->"
print("<div class='modal' id='add_your_list' role='dialog'>")
print("<div class='modal-dialog modal-lg'>")
print("<div class='modal-content' style='background: #000000;'>")
print("<div class='modal-header'>")
print("<button type='button' class='close' data-dismiss='modal'>&times;</button>")
print("<div class='row'>")
print("<div class='col-md-3'>")
print("<h4 class='modal-title'>")
print("<img src='images/logo.png' class='img-responsive' style='width: 15vw; height: 20vh; margin-left: 70%;'></h4>")
print("</div>")
print("<div class='col-md-9'>")
print("<h2 class='pull-right' style='color: #ffc80c; margin-top: %;'> ADD YOUR BUSINESS HERE </h2>")
print("</div>")
print("</div>")
print("</div>")
print("<div class='modal-body'>")
print("<div class='row'>")
print("<div class='col-md-6'>")
print("<img src='images/online.png' style='width: 700px; margin-left: -30%;'>")
print("</div>")
print("<div class='col-md-6' style='margin-top: ;'>")
print("<form class='form-horizontal' role='form' action='business_register.py'>")
print("<div class='form-group'>")
print("<label class='col-sm-3 control-label' for='name' style='color: white;'>Name <span style='color: red;'> * </span>")
print("</label>")
print("<div class='col-sm-9'>")
print("<input type='text' class='form-control' id='name' name='name' placeholder='Your Name' autofocus='' required>")
print("</div>")
print("</div> <br>")
print("<div class='form-group'>")
print("<label class='col-sm-3 control-label' for='phone' style='color: white;'>Mobile <span style='color: red;'> * </span>")
print("</label>")
print("<div class='col-sm-9'>")
print("<input type='text' name='mobile' class='form-control' id='phone' placeholder='Your Mobile No.' maxlength='10' pattern='[0-9]{10}' required>")
print("</div>")
print("</div> <br>")
print("<div class='form-group'>")
print("<label class='col-sm-3 control-label' for='email' style='color: white;'>Email <span style='color: red;'> * </span>")
print("</label>")
print("<div class='col-sm-9'>")
print("<input type='email' name='email' class='form-control' id='email' placeholder='Your Email' required>")
print("</div>")
print("</div><br>")
print("<div class='form-group'>")
print("<label class='col-sm-3 control-label' for='msg' style='color: white;'>Message</label>")
print("<div class='col-sm-9'>")
print("<textarea class='form-control' row='8' name='msg' id='msg' placeholder='Message' style='height: 100px;'></textarea>")
print("</div>")
print("</div><br>")
print("<div class='form-group'>")
print("<div class='text-center'>")
print("<input type='submit' class='btn btn-success btn-sm' value='Submit' style='margin-left: 27%; margin-top: %;'>")
print("</div>")
print("</div>")
print("</form>")
print("</div>")
print("</div>")
print("</div>")
print("<div class='modal-footer'>")
print("<button type='button' class='btn btn-default'  onclick='close_modal()' data-dismiss='modal'> Close </button>")
print("</div>")
print("</div>")
print("</div>")
print("</div>")
##print(" <!-- android link Modal-->")
print("<div class='modal' id='android' role='dialog'>")
print("<div class='modal-dialog modal-md'>")
print("<div class='modal-content'>")
print("<div class='modal-header'>")
print("<button type='button' class='close' data-dismiss='modal'>&times;</button>")
print("<h3 style='text-align:center;'>Download Link from Google PlayStore</h3>")
print("</div>")
print("<div class='modal-body'>")
print("<div class='row'>")
print("<div class='col-md-1 col-sm-1'></div>")
print("<div class='col-md-11 col-sm-11'>")
print("<form class='form-inline'>")
print("<div class='form-group'>")
print("<label for='android_link'>Enter Your Email Id : </label>")
print("<input class='form-control' type='text' id='android_link'>")
print("<input type='button' class='btn btn-success btn-sm' value='Submit' onclick='link()'>")
print("</div>")	  
print("</form>")  
print("</div>")
print("</div>")
print("</div>")  
print("</div>")
print("</div>")
print("</div>")
print("""<script type='text/javascript'>)
function link()
{
var xmlhttp = new XMLHttpRequest();
xmlhttp.onreadystatechange = function() {
if (this.readyState == 4 && this.status == 200) {
}
};
var email = document.getElementById('android_link').value;
var msg = 'Please Click the link below to download DoEmart App : https://play.google.com/store/apps/details?id=com.DoEmartindia&hl=en';
var url = 'SendLink.py?email='+email;
xmlhttp.open('GET',url, true);
xmlhttp.send();
alert('Link shared to your Email\nThank You..!');
document.getElementById('android_link').value = '';
}"""
print("</script>")
print("</body>")
print("</html>")
