<?php

$mysql_hostname = '127.0.0.1';
$mysql_username = ''; //mysql username
$mysql_password = ''; //mysql password
$mysql_database = 'login'; //database named login
$db = mysql_connect ($mysql_hostname, $mysql_username, $mysql_password)

or die ('Something Is Broken');

mysql_select_db($mysql_database, $db) or die('Couldn\'t Find database');


?>
