<html>
<head>
</head>
<body>
<?php
	ob_start(); 
	session_start(); 
	require_once ("func.php"); 

	//$returnurl = urlencode(isset($_GET["returnurl"])?$_GET["returnurl"]:""); 
	//if($returnurl == "") 
	//	$returnurl = urlencode(isset($_POST["returnurl"])?$_POST["returnurl"]:""); 
	
	//$do = isset($_GET["do"])?$_GET["do"]:""; 
	//$do = strtolower($do); 
	//switch($do) 

	$username = @$_POST["username"];
	$password = @$_POST["password"];
	
	// to escape SQL injection
	//$username = stripcslashes($username);
	//$password = stripcslashes($password);
	//$username = mysql_real_escape_string($username);
	//$password = mysql_real_escape_string($password);
	
	$encpassword = md5($password);

	// Connection
	mysql_connect('localhost','root','kubamt');
	mysql_select_db('login');

	// Query
	$result = mysql_query("select * from user where username = '$username' and password = '$encpassword' ")
		or die("failed to query db " .mysql.error());
	$row = mysql_fetch_array($result);
	if ($row['username'] == $username && $row['password'] == $encpassword) {

		if (array_key_exists($username ,$_COOKIE ) == True)
		{
		echo 'Login Sucesss  Welcome ' .$row['username'];
?>
		<p align='right'>For Logout Click<a href='login.php'> Here</a></p>
<?php		
		}

		else
		{
		echo 'Something Is Broken Check Again';
?>
		<p align='left'>For login Click<a href='login.php'> Here</a></p>
<?php
		}		
	}
	else
	{
		header("location: failed.php");
		echo 'Failed TO Login';
	}


?>


</body>
</html>
