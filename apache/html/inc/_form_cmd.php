<?php
	if($_GET['cmd'] == 'delcmd')
	{
		$classvar->delete($_GET['id']);
	}

	if(isset($_POST['frmvalue']) && $_POST['frmvalue'] == 'add')
	{

		$classvar->insert($_POST);

		echo "<p>record added.";
	}

	if(isset($_POST['frmvalue']) && $_POST['frmvalue'] == 'update')
	{

		$classvar->update($_POST, $_GET['id']);

		echo "<p>record updated.";
	}
?>
