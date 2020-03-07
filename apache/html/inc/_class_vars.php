<?php
	if(isset($_GET['cat']))
	{
		$heading = strtoupper($_GET['cat']);

		if($_GET['cat'] == 'securitychecks')
		{
			$classname = 'SecurityCheck';
			$num_sort = 'id';
			$other_sort = 'component';
			$order = 'DESC';
			$show = array('component','enabled','command','regex','resource','expected','checkValue','valueLogic','fkFunction','checkTask','checkID','info');
			$display = 'Word';
		}

		if($_GET['cat'] == 'checkpatterns')
		{
			$classname = 'CheckPattern';
			$num_sort = 'id';
			$other_sort = 'components';
			$order = 'DESC';
			$show = array('pattern','components','type');
			$display = 'Word';
		}
	}
?>
