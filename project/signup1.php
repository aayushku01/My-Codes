<html>
<head>
<?php
include('db.php');

$username = @$_POST['username'];
$password = @$_POST['password'];
$repeatpassword = @$_POST['repeatpassword'];
$submit = @$_POST['submit'];
$encpassword = md5($password);

if($submit) {

  if($username==true) {

    if($password==true) {

      if($password==$repeatpassword) {
      
        if (strlen($username) <50) {

          if (strlen($password) < 50 || strlen($password) > 5 ) {
            $query = mysql_query("SELECT username FROM user WHERE username='".$username."'");

            if(mysql_num_rows($query)>=1)
            {
              echo"name already exists";

            }

            else
            {
              $insert= mysql_query ("INSERT INTO user (username, password) VALUES ('$username','$encpassword')")
              or die("Error: " . mysql_error());
              setcookie($username, sha1(md5($password)), time() + 2592000, '/', 'localhost');//Edit number in this line to change the expire Time
              echo "Registration Success!!!";
            }
            
          
          }
        
        }

      }else
      echo "Passord Don't Match";

    }else
    echo "Please Enter a password";

  }else
  echo 'Please Enter a username';

};

?>
</head>
<body>
<form method='post'>
<table width="30%" bgcolor="cyan" align="center">
<tr>
<td colspan=3><center><font size=4><b>Register Here</b></font></center></td>
</tr>
  <div class="container">
    <tr>
    <td>Username: </td><td colspan="2"><input name="username" type="text" ></td>
    </tr>
    <br />
    <tr>
    <td>Password: </td><td colspan="2"><input name="password" type="Password" ></td>
    </tr>
    <br />
    <tr>
    <tr>
    <td>Repeat Password: </td><td colspan="2"><input name="repeatpassword" type="password"></td>
    </tr>
    <br />
    <tr>
    <td colspan=3><p>By creating an account you agree to our <a href="#">Terms & Privacy</a>.</p></td>
    </tr>
    <div class="clearfix">
      <tr>
      <td><button type="button"  class="cancelbtn">Cancel</button></td>
      <td><input name='submit' type="submit" ></td>
      <td><a href='login.php'><input type="button" value="Login Page" /></a></td>
      </tr>
    </div>
  </div>

</table>
</form>
</body>
</html>
