<?php
	require_once('inc/db.class/_class.load_all.php');
	require_once('inc/db/_db_connect.php');

	require_once('inc/_backend_functions.php');

	$gen = new Gen;
?>

<html>
<head>
<title><?php echo $_SERVER['QUERY_STRING']; ?></title>
<link rel="stylesheet" href="./rsc/_main_style.css" type="text/css" media="screen">
</head>
<body>

<div id="container">

<div id="nav">

<br><b>DB Tables: </b>
<?php
	$dir = opendir('inc/');
	while (false !== ($fname = readdir( $dir )))
	{
		if(preg_match('/_form.php/', $fname))
		{
			$aint = str_replace('_form.php', '', $fname);
			echo "<br><a href=\"".$_SERVER['PHP_SELF']."?cat=".trim($aint, '_')."&cmd=update\">".trim($aint, '_')."</a>";
		}
	}

	closedir($dir);
?>
<p>
<br>

</div>

