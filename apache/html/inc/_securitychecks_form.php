<?php
	$pimage_fld = '';

	require_once('inc/_form_cmd.php');

	if(!$_POST[frmvalue] && $_GET[cmd] != 'delcmd')
	{

		prn_frm_top();

		frm_txt($classvar, 'Component', 'component', '200');
		frm_txt($classvar, 'checkID', 'checkID', '200');
		frm_txt($classvar, 'Task', 'checkTask', '200');
		frm_txt($classvar, 'command', 'command', '200');
		frm_txt($classvar, 'regex', 'regex', '200');
		frm_txt($classvar, 'resource/file', 'resource', '200');
		frm_txt($classvar, 'expected setting', 'expected', '200');
		frm_txt($classvar, 'Compare value', 'checkValue', '200');
		frm_txt($classvar, 'Value Logic', 'valueLogic', '200');
		frm_txt($classvar, 'Function FK', 'fkFunction', '200');
		frm_txt($classvar, 'info', 'info', '200');
		frm_txt($classvar, 'enabled', 'enabled', '200');

		prn_frm_end();
}?>
