<?php
     print_r($_COOKIE);    //output the contents of the cookie array variable 


	$search_array = array('first' => null, 'second' => 4);

	// returns false
	echo isset($search_array['first']);

	// returns true
	if (array_key_exists('first', $search_array)) 
	{
		echo 'dewvf';
	}
?>
