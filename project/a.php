<?php
	setcookie("user_name", sha1(md5('user_name')), time()+ 10,'/'); // expires after 60 seconds
	echo 'the cookie has been set for 30 seconds';

	$arr = array(1, 2, 3);
	echo '<pre>';
	print_r($arr);
	echo '</pre>';
	print_r($arr); 

	echo '<pre>';
	echo $_COOKIE['user_name'];
	echo '</pre>';
?>
