<?php require_once('_header.php'); ?>

<div id=main>


<?php
	if(isset($_GET['cat']))
	{
?>

<b><?php echo strtoupper(str_replace('_', ' ', $_GET['cat'])); ?></b>

<br><a href=<?php echo $_SERVER['PHP_SELF']; ?>?cat=<?php echo $_GET['cat']; ?>&cmd=add>Add</a>

<!-- |
<a href=<?php echo $_SERVER['PHP_SELF']; ?>?cat=<?php echo $_GET['cat']; ?>&cmd=update>Update</a> |
-->

<!--
<b>SORT BY:</b>
<a href=<?php echo $_SERVER['PHP_SELF']; ?>?cat=<?php echo $_GET['cat']; ?>&cmd=update&field=numbers>Numbers</a>
<a href=<?php echo $_SERVER['PHP_SELF']; ?>?cat=<?php echo $_GET['cat']; ?>&cmd=update&field=words>Words</a>
-->
<hr>

<?php
		require_once('inc/_class_vars.php');

		if(isset($_GET['cat']))
		{
			prn_dbdata($_GET['cat'], $_GET['cat'], $classname, $num_sort, $other_sort, $order, $show, $display, $heading);
		}
	}
?>

</div>


<?php require_once('_footer.php'); ?>
