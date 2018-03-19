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

          if (strlen($password) < 50 || strlen($password)>5 ) {
              $insert= mysql_query ("INSERT INTO user (username, password) VALUES ('$username','$encpassword')")
              //setcookie($username, $username, time() + 2592000, '/');
              or die("Error: " . mysql_error());
              
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
Username: <input name="username" type="text" >
<br />
Password: <input name="password" type="Password" >
<br />
Repeat Password: <input name="repeatpassword" type="password">
<br />
<input name='submit' type="submit" >
</form>
</body>
</html>
