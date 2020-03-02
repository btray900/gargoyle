<?php
	$pimage_fld = '';

	require_once('inc/_form_cmd.php');

	if(!$_POST[frmvalue] && $_GET[cmd] != 'delcmd')
	{

		prn_frm_top();

		frm_txt($classvar, 'Cloud', 'cloud', '200');
		frm_txt($classvar, 'Zone', 'zone', '200');
		frm_txt($classvar, 'Alias', 'alias', '200');
		frm_txt($classvar, 'Architecture', 'architecture', '200');
		frm_txt($classvar, 'Release', 'zone_release', '200');
		frm_txt($classvar, 'Status', 'status', '200');
		frm_txt($classvar, 'Prod Date', 'prod_date', '200');
		frm_txt($classvar, 'Cycle', 'cycle', '200');

		prn_frm_end();
}?>
