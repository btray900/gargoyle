<?php
	$pimage_fld = '';

	require_once('inc/_form_cmd.php');

	if(!$_POST[frmvalue] && $_GET[cmd] != 'delcmd')
	{

		prn_frm_top();

		frm_txt($classvar, 'Cloud', 'cloud', '200');
		frm_txt($classvar, 'Components', 'components', '200');
		frm_txt($classvar, 'Pattern', 'pattern', '200');
		frm_txt($classvar, 'Type', 'type', '200');

		prn_frm_end();
}?>
