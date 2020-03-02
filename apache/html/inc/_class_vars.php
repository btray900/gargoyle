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
			$show = array('component','cloud','cloudVersion','releaseLabel','enabled','command','regex','resource','expected','foundationCheck','checkValue','valueLogic','fkFunction','checkTask','checkID','reportEnabled','reportLabel','info','reference','aspr');
			$display = 'Word';
		}

		if($_GET['cat'] == 'cloudzones')
		{
			$classname = 'CloudZone';
			$num_sort = 'id';
			$other_sort = 'zone';
			$order = 'ASC';
			$show = array('cloud','zone','alias','architecture','zone_release','status','prod_date','cycle');
			$display = 'Word';
		}

		if($_GET['cat'] == 'checkpatterns')
		{
			$classname = 'CheckPattern';
			$num_sort = 'id';
			$other_sort = 'components';
			$order = 'DESC';
			$show = array('cloud','pattern','components','type');
			$display = 'Word';
		}
	}
?>
